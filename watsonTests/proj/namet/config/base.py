# -*- coding: utf-8 -*-
"""Define and extend configuration settings for your application.
"""

import os
from namet.config.routes import routes  # noqa
from namet.config.dependencies import dependencies  # noqa


debug = {
    'enabled': os.environ.get('DEV_ENV', False)
}
