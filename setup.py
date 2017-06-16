from setuptools import setup, find_packages
import devicetype

setup_requires = ['setuptools']

install_requires = [
    'Django>=1.7,<1.12',
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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require
)

