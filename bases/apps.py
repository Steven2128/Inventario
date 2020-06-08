from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'bases'

    def ready(self):
        import users.signals