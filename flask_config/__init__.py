# -*- coding:utf8 -*-
"""
Flask Extended Config
"""

import os
import yaml
from flask import Config as BaseConfig


class Config(object):
    app = None

    def __init__(self, app=None):
        self.config = self._make_config(app)

        if app:
            self.init_app(app)

    def __setattr__(self, key, value):
        if key in ['app', 'config']:
            super(Config, self).__setattr__(key, value)

        self.config[key] = value

    def __getattr__(self, item):
        if item in ('app', 'config', 'init_app', '_make_config', ):
            super(Config, self).__getattr__(item)

        try:
            return self.config[item]
        except:
            raise AttributeError()

    def _make_config(self, app, instance_relative=False):
        root_path = None
        default_config = {}
        if app:
            root_path = app.root_path
            default_config = app.default_config

            if instance_relative:
                root_path = app.instance_path

        return ExtendedConfig(root_path, default_config)

    def init_app(self, app):
        self.app = app
        self.config.root_path = app.root_path

        for k in app.config.iterkeys():
            self.config[k] = app.config[k]

        self.app.config = self.config


class ExtendedConfig(BaseConfig):
    def from_yaml(self, config_name=None, file_name='config.yaml'):
        env = os.environ.get('FLASK_ENV', 'development').upper()
        self['ENVIRONMENT'] = env.lower()

        if not config_name:
            config_name = env

        config_name = config_name.upper()

        for path in ('/etc', self.root_path,):
            config_file = os.path.join(path, file_name)

            try:
                with open(config_file) as f:
                    c = yaml.load(f)

                for key, value in c[config_name].iteritems():
                    if key.isupper():
                        self[key] = value
            except Exception as e:
                pass
