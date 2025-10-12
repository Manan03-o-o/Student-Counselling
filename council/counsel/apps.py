from django.apps import AppConfig

class CounselConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'counsel'

    def ready(self):
        # Import User inside ready() to avoid AppRegistryNotReady
        from django.contrib.auth.models import User

        # Create default admin if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
