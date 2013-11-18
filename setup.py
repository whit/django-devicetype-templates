from setuptools import setup, find_packages
import devicetype

install_requires = [
    'setuptools>=0.6b1',
    'Django>=1.3.1,<1.7',
]

tests_require = [
    'nose',
    'coverage',
]

long_description = open('README.rst').read()

setup(
    name='django-devicetype-templates',
    version=devicetype.__versionstr__,
    description='Django library to serve different templates for different device types',
    long_description=long_description,
    author='Vitek Pliska',
    author_email='whit@jizak.cz',
    license='BSD',
    url='https://github.com/whit/django-devicetype-templates',

    packages=find_packages(
        where='.',
        exclude=('docs', 'tests', 'example',)
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose.collector',
)

