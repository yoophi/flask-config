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
        if app:
            self.init_app(app)

    def _make_config(self, app, instance_relative=False):
        root_path = app.root_path
        if instance_relative:
            root_path = app.instance_path

        config = ExtendedConfig(root_path, app.default_config)
        for k in app.config.iterkeys():
            config[k] = app.config[k]

        app.config = config

    def init_app(self, app):
        self.app = app
        self._make_config(app)


class ExtendedConfig(BaseConfig):
    def from_yaml(self, config_name=None, file_name=None):
        env = os.environ.get('FLASK_ENV', 'development').upper()
        self['ENVIRONMENT'] = env.lower()

        if not config_name:
            config_name = env

        config_name = config_name.upper()
        file_name = file_name if file_name else 'config.yaml'

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
