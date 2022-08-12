from django.apps import AppConfig


class FetchMetaDataAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fetch_Meta_Data_App'

    def ready(self):
        import Fetch_Meta_Data_App.signals
