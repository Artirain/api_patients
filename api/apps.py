from django.apps import AppConfig
from django.db.models.signals import post_migrate

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.contrib.auth.management import create_permissions

        def add_permissions(sender, **kwargs):
            create_permissions(get_user_model()._meta.app_config, verbosity=0)

        post_migrate.connect(add_permissions, sender=self)