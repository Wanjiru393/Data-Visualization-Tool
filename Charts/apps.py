from django.apps import AppConfig


class ChartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Charts'
 
    def ready(self):
        from Charts import signals