from django.apps import AppConfig


class PresentationConfig(AppConfig):
    name = 'website.presentation'
    verbose_name = "Presentation"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
