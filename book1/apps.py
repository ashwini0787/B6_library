from django.apps import AppConfig

print( "in apps.py")
class Book1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book1'
