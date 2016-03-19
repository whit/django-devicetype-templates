django-devicetype-templates
===========================

django-devicetype-templates is a library that detect device type by browser's user agent string
and serves different templates for each type.

If standard responsive layouts does not fit all of your needs
and if you do not want to use some hacky template loaders with thread locals,
you may find this library useful.


Requirements
------------

    * Django >= 1.7
    * Tested with Python versions 2.7, 3.3, 3.4, 3.5
    * It uses `process_template_response`_ middleware method, so your views should returns ``TemplateResponse``.


Installation
------------

Install from PyPi::

    pip install django-devicetype-templates


Install development version to virtualenv::

    git clone https://github.com/whit/django-devicetype-templates.git
    cd django-devicetype-templates
    python setup.py develop

Run tests::

    pip intsall -r requirements-dev.txt
    py.test

.. _process_template_response: https://docs.djangoproject.com/en/dev/topics/http/middleware/#process_template_response


Configuration
-------------

Add middleware::

    MIDDLEWARE_CLASSES = (
        ...
        'devicetype.middleware.DeviceTypeMiddleware',
    )

If you need to use some variables in your templates, you can add devicetype context processor::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'devicetype.context_processors.devicetype',
    )

Then, in templates will be available these variables: ``devicetype``, ``is_mobile``, ``is_tablet``
and ``big_resolution`` (not implemented yet).


Other settings
--------------

``DEBUG_DEVICETYPE_NOCOOKIE``
-----------------------------

For development purposes if you want to switch user agents oftenly.
Cookie max age wil be set to 5 seconds.


``DEVICETYPE_TEMPLATE_PREFIX``
------------------------------

Prefixes are variable. When you need prefix template file name, use something like ``tablet-``. If you want to have
device-specific templates in subfolders, you can use ``tablet/`` prefix for example.

Default::

    {
        'desktop': '',
        'mobile': 'mobile/',
        'tablet': 'tablet/',
    }

``DEVICETYPE_PREFIX_BASENAME``
------------------------------

When you use folder-like prefix, like `tablet/` and `mobile/`, with this setting
you can select how subfolders will be detected.

With ``DEVICETYPE_PREFIX_BASENAME = False`` (default)::

    tablet/base.html
    tablet/app/app_base.html
    tablet/layout/three-cols.html
    ...

With ``DEVICETYPE_PREFIX_BASENAME = True``::

    tablet/base.html
    app/tablet/app_base.html
    layout/tablet/three-cols.html
    ...


``DEVICETYPE_MOBILE_PATTERNS`` and ``DEVICETYPE_TABLET_PATTERNS``
-----------------------------------------------------------------

You can override default search patterns. It search in tablet patterns first.


Build status
------------

:Master branch:

  .. image:: https://secure.travis-ci.org/whit/django-devicetype-templates.png?branch=master
     :alt: Travis CI - Distributed build platform for the open source community
     :target: http://travis-ci.org/#!/whit/django-devicetype-templates
