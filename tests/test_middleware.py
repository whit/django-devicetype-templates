from django.test.client import RequestFactory
from unittest import TestCase

from devicetype.middleware import DeviceTypeMiddleware
from devicetype.context_processors import devicetype as devicetype_context_processor
from devicetype import conf


class MockResponse(object):

    def __init__(self, template_name='test.html'):
        self.template_name = template_name

    def set_cookie(self, *args, **kwargs):
        return True


class TestDeviceTypeMiddleware(TestCase):

    def setUp(self):
        self.rf = RequestFactory()
        self.m = DeviceTypeMiddleware()
        super(TestDeviceTypeMiddleware, self).setUp()

    def test_no_user_agent(self):
        req = self.rf.get('/')
        self.m.process_request(req)

        self.assertEqual(conf.DEFAULT_TYPE, req.devicetype)

    def test_with_template_list(self):
        req = self.rf.get('/', HTTP_USER_AGENT='android 4 tablet')
        self.m.process_request(req)

        resp = self.m.process_template_response(req, MockResponse(template_name=['A', 'B']))
        self.assertEqual(['tablet/A', 'tablet/B', 'A', 'B'], resp.template_name)

    def test_tablet(self):
        req = self.rf.get('/', HTTP_USER_AGENT='android 4 tablet')
        self.m.process_request(req)

        resp = self.m.process_template_response(req, MockResponse())
        self.assertEqual(['tablet/test.html', 'test.html'], resp.template_name)

    def test_tablet_basename_prefix(self):
        conf.PREFIX_BASENAME = True
        req = self.rf.get('/', HTTP_USER_AGENT='android 4 tablet')
        self.m.process_request(req)

        resp = self.m.process_template_response(req, MockResponse('A/B.html'))
        conf.PREFIX_BASENAME = False
        self.assertEqual(['A/tablet/B.html', 'A/B.html'], resp.template_name)

    def test_tablet_no_folder(self):
        conf.TEMPLATE_PREFIX['tablet'] = 't-'
        req = self.rf.get('/', HTTP_USER_AGENT='android 4 tablet')
        self.m.process_request(req)

        resp = self.m.process_template_response(req, MockResponse('A/B.html'))
        conf.TEMPLATE_PREFIX['tablet'] = 'tablet/'
        self.assertEqual(['A/t-B.html', 'A/B.html'], resp.template_name)

    def test_mobile(self):
        req = self.rf.get('/', HTTP_USER_AGENT='android mobile')
        self.m.process_request(req)

        resp = self.m.process_template_response(req, MockResponse())
        self.assertEqual(['mobile/test.html', 'test.html'], resp.template_name)

    def test_browser(self):
        req = self.rf.get('/', HTTP_USER_AGENT='some browser')
        self.m.process_request(req)

        resp = self.m.process_template_response(req, MockResponse())
        self.assertEqual(['test.html'], resp.template_name)

    def test_direct_switch_redirect(self):
        req = self.rf.get('/', data={'devicetype': 'tablet'}, HTTP_USER_AGENT='some browser')
        resp = self.m.process_request(req)

        self.assertEqual(resp.status_code, 302)

    def test_get_from_cookie_first(self):
        req = self.rf.get('/', HTTP_USER_AGENT='some browser', COOKIES={'devicetype': 'tablet'})
        req.COOKIES['devicetype'] = 'tablet'
        self.m.process_request(req)

        resp = self.m.process_template_response(req, MockResponse())
        self.assertEqual(['tablet/test.html', 'test.html'], resp.template_name)

    def test_context_processor(self):
        req = self.rf.get('/', HTTP_USER_AGENT='Linux Android 3 Unknown Device')
        self.m.process_request(req)

        ctx = devicetype_context_processor(req)
        self.assertEqual('tablet', ctx['devicetype'])
        self.assertTrue(ctx['is_mobile'])
