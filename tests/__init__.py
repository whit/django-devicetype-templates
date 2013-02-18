import os

test_runner = None
old_config = None

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

def setup():
    global test_runner
    global old_config
    from django.test.simple import DjangoTestSuiteRunner
    test_runner = DjangoTestSuiteRunner()
    test_runner.setup_test_environment()


def teardown():
    test_runner.teardown_test_environment()
