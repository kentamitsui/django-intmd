from django.apps import AppConfig


class MatchingAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "matching_app"
    verbose_name = "Matching App"

    def ready(self):
        import matching_app.models  # noqa
