from django.apps import AppConfig

AppConfig.default = False

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
