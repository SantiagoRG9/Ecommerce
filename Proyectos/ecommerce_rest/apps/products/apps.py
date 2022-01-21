from django.apps import AppConfig

AppConfig.default = False

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
