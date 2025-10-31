from rest_framework import serializers
from .models import Emission, EmissionType, Country


class EmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionType
        fields = ["emission_code", "description"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name", "country_code"]


class EmissionSerializer(serializers.ModelSerializer):
    emission_type = EmissionTypeSerializer(read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Emission
        fields = [
            "id",
            "emissions",
            "emission_type",
            "country",
            "activity",
            "year",
        ]
