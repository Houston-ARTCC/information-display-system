from django.apps import AppConfig


class FlightsConfig(AppConfig):
    name = 'flights'

    def ready(self):
        from . import signals
        from .updater import update_scheduler
        update_scheduler()