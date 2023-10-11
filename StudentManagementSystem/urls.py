from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()