from django.apps import AppConfig


class PosfinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posFin'

    def ready(self):
        import posFin.signals