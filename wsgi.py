import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arch_calc_squares.settings')
application = get_wsgi_application()
