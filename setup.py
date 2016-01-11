"""
Flask-Config
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-Config',
    version='0.1',
    url='http://github.com/yoophi/flask-config/',
    license='BSD',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    description='Very short description',
    long_description=__doc__,
    packages=['flask_config'],
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

