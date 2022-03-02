from dataclasses import field, fields
from email.policy import default
from enum import auto
from django import forms
from .models import Book
# from django.forms import ModelForm
from django.utils import timezone



# class studForm(forms.Form):
#     name = forms.CharField(max_length= 100)
#     roll_no = forms.IntegerField(help_text="Enter 6 digit no")
#     password = forms.CharField(widget=forms.PasswordInput())


class BookForm(forms.ModelForm):
    # author = forms.CharField(max_length=100)
    # file = forms.FileField()
  

    class Meta:
        model = Book
        fields = "__all__"     # you can give the specific name of field but should be in tuple 
        # exclude = ("qty",)    # should all be in tuple
