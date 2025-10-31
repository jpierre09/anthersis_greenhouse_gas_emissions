from django.apps import AppConfig


class EmissionsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emissions_app"

    def ready(self):
        import emissions_app.signals
