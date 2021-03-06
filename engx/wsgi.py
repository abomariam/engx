"""
WSGI config for engx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, project)

activate_this = os.path.join(project, '../engx_env/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))


os.environ["DJANGO_SETTINGS_MODULE"] = "engx.settings"



from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("engx"))

application = get_wsgi_application()
