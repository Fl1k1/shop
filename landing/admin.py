from django.contrib import admin
from .models import *

class LandingAdminModel(admin.ModelAdmin):
    list_display = ["first_name", "second_name", "email"]
    list_filter = ["email"]
    search_fields = ["email"]
    #fields = ["email"]
    #exclude = [""]

    class Meta:
        model = Landing


admin.site.register(Landing, LandingAdminModel)


