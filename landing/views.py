from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

class LandingPageView(CreateView):
    template_name = 'html/landing.html'
    form_class = LandingForm
    success_url = reverse_lazy('landing_url')



