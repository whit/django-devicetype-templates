from setuptools import setup, find_packages
import responsive

setup(
    name='Django-Responsive',
    version=responsive.__versionstr__,
    description='Django library to detect mobile/tablet browsers',
    long_description='\n'.join((
        'Django browsecap',
        '',
        'helper module to process browseap.ini',
        'designed mainly to detect mobile browsers and crawlers.',
        '',
        'Based Heavily on django snippet 267',
        'Thanks!',
    )),
    author='Vitek Pliska',
    author_email='whit@jizak.cz',
    license='BSD',
    url='http://www.github.com/whit/django-responsive',

    packages=find_packages(
        where='.',
        exclude=('docs', 'tests', 'example', )
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'Django>=1.3.1',
    ],
)
