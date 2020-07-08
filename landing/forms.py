from django import forms
from .models import *


class LandingForm(forms.ModelForm):
    class Meta:
        model = Landing
        exclude = []
