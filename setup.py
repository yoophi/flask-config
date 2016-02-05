"""
Flask-Config-Helper
-------------------

This is the description for that library
"""
import os
import re
from setuptools import setup


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version(os.path.join("flask_config_helper", "__init__.py"))

setup(
    name='Flask-Config',
    version=__version__,
    url='http://github.com/yoophi/flask-config-helper/',
    license='BSD',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    description='Very short description',
    long_description=__doc__,
    packages=['flask_config_helper'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'click==6.2',
        'Flask',
        'Flask-Script',
        'PyYAML==3.11',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
