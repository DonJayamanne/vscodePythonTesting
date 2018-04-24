#!/usr/bin/env python
import os
import sys

SCRIPT_DIR, SCRIPT_FILE = os.path.split(os.path.abspath(__file__))
os.environ.update({
    'APP_MODULE': 'namet',
    'APP_SETTINGS': 'namet.config.base',
    'APP_DIR': os.path.join(SCRIPT_DIR, 'namet'),
    'PUBLIC_DIR': os.path.join(SCRIPT_DIR, 'public'),
    'SCRIPT_DIR': SCRIPT_DIR
})
os.chdir(os.environ['APP_DIR'])

try:
    from watson.framework import applications
    from watson.common import imports
except:
    sys.stdout.write(
        'You must have Watson installed, please run `pip install watson-framework`\n')
    sys.exit(1)


if __name__ == '__main__':
    config = imports.import_module(os.environ['APP_SETTINGS'])
    application = applications.Console(config)
    application()
