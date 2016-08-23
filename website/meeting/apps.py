from django.apps import AppConfig


class MeetingConfig(AppConfig):
    name = 'website.meeting'
    verbose_name = "Meeting"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
