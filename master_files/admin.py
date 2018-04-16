from django.contrib import admin
from django.apps import apps
from .models import *

from django.contrib.admin.sites import AlreadyRegistered

app_models = apps.get_app_config('master_files').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass


# Register your models here.
