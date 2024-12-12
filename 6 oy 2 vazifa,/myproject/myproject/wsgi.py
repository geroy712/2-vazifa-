"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bu App sahifasi!")
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('app4/', include('app4.urls')),
    path('app5/', include('app5.urls')),
    path('app6/', include('app6.urls')),
    path('app7/', include('app7.urls')),
    path('app8/', include('app8.urls')),
    path('app9/', include('app9.urls')),
    path('app10/', include('app10.urls')),
]
