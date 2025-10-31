import json
import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.conf import settings
from .models import EmissionType, Country, Emission


@receiver(post_migrate)
def populate_initial_data(sender, **kwargs):
    if sender.name != "emissions_app":
        return

    data_file = os.path.join(settings.BASE_DIR, "data", "emissions.json")
    if not os.path.exists(data_file):
        return

    if Emission.objects.exists():
        return

    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for et in data.get("emission_types", []):
        EmissionType.objects.get_or_create(**et)

    for c in data.get("countries", []):
        Country.objects.get_or_create(**c)

    for e in data.get("emissions", []):
        emission_type = EmissionType.objects.get(emission_code=e["emission_type"])
        country = Country.objects.get(country_name=e["country"])
        Emission.objects.get_or_create(
            emissions=e["emissions"],
            emission_type=emission_type,
            country=country,
            activity=e["activity"],
            year=e["year"],
        )

    print("Datos iniciales cargados")
