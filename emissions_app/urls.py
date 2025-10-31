from django.urls import path
from .views import EmissionListAPIView, EmissionDetailAPIView

urlpatterns = [
    path("emissions/", EmissionListAPIView.as_view(), name="lista-emisiones"),
    path(
        "emissions/<int:pk>/", EmissionDetailAPIView.as_view(), name="detalle-emisiones"
    ),
]
