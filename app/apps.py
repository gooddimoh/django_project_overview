from django.apps import AppConfig as AppConfigImported


class AppConfig(AppConfigImported):
    name = 'app'