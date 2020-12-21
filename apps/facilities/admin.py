from django.contrib import admin
from django.contrib.admin import ModelAdmin

from ..facilities.models import Facility


@admin.register(Facility)
class FacilityAdmin(ModelAdmin):
    model = Facility
    list_display = ('icao', 'name')
