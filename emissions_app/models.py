from django.db import models


class EmissionType(models.Model):
    emission_code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.emission_code


class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.country_name


class Emission(models.Model):
    emissions = models.FloatField()
    emission_type = models.ForeignKey(
        EmissionType, on_delete=models.CASCADE, related_name="emissions"
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="emissions"
    )
    activity = models.CharField(max_length=100)
    year = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("year", "country", "emission_type", "activity")
        ordering = ["-year"]

    def __str__(self):
        return f"{self.emissions} ({self.year} - {self.emission_type})"
