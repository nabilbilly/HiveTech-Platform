from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Accounts'

def ready(self):
        # Import the signals to ensure they're registered
        import Accounts.signals