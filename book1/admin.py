from django.contrib import admin
from .models import Book
print( "in admin.py")
# Register your models here.
admin.site.register(Book)