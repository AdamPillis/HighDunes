from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """configuartion for user_profile app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    def ready(self):
        """
        function import signals to
        create new profile for new users
        """
        import user_profile.signals
