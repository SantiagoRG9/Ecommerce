from django.apps import AppConfig

AppConfig.default = False

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
