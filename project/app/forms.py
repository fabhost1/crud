from dataclasses import fields
from django.forms import ModelForm
from .models import employee


class update(ModelForm):
    class Meta:
        model=employee
        fields='__all__'
        