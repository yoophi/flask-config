import os
from flask_script import Manager
from flask_config_helper import InitConfig
from . import app


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


manager = Manager(app)
manager.add_command("init", InitConfig(directory='/tmp/example',
                                       config_contents=read('config.yaml.default')))

if __name__ == "__main__":
    manager.run()
