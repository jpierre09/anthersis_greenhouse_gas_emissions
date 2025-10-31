from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from emissions_app.models import Country, EmissionType, Emission


class TestEmissionEndpoints(APITestCase):
    def setUp(self):
        self.country, _ = Country.objects.get_or_create(
            country_name="Colombia", country_code="COL"
        )

        self.emission_type, _ = EmissionType.objects.get_or_create(
            emission_code="CO2", description="Carbon Dioxide"
        )

        self.emission, _ = Emission.objects.get_or_create(
            emission_type=self.emission_type,
            country=self.country,
            activity="Transportation",
            year=2021,
            defaults={"emissions": 8.1},
        )

        self.url_list = reverse("lista-emisiones")
        self.url_detail = reverse("detalle-emisiones", args=[self.emission.id])

    def test_api_is_alive(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_emission_returns_200(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["activity"], "Transportation")

    def test_detail_emission_not_found(self):
        url_not_found = reverse("detalle-emisiones", args=[999])
        response = self.client.get(url_not_found)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
