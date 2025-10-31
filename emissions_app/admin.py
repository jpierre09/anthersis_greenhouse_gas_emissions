from django.contrib import admin
from .models import EmissionType, Country, Emission


@admin.register(EmissionType)
class EmissionTypeAdmin(admin.ModelAdmin):
    list_display = ("emission_code", "description")
    search_fields = ("emission_code", "description")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_name", "country_code")
    search_fields = ("country_name", "country_code")


@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):
    list_display = ("year", "emission_type", "country", "activity", "emissions")
    list_filter = ("year", "country", "emission_type")
    search_fields = ("activity",)
    ordering = ("-year",)
