from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Emission
from .serializers import EmissionSerializer


class EmissionListAPIView(APIView):
    def get(self, request):
        try:
            country = request.query_params.get("country")
            emission_type = request.query_params.get("emission_type")
            year = request.query_params.get("year")
            activity = request.query_params.get("activity")

            queryset = Emission.objects.select_related("country", "emission_type").all()

            if country:
                queryset = queryset.filter(country__country_name__icontains=country)
            if emission_type:
                queryset = queryset.filter(
                    emission_type__emission_code__iexact=emission_type
                )

            if year:
                try:
                    year = int(year)
                    queryset = queryset.filter(year=year)
                except ValueError:
                    return Response(
                        {"detail": "El parámetro 'year' debe ser un número entero."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            if activity:
                queryset = queryset.filter(activity__icontains=activity)

            queryset = queryset.order_by("year")

            serializer = EmissionSerializer(queryset, many=True)

            return Response(
                {
                    "count": queryset.count(),
                    "results": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"detail": "Error interno del servidor", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EmissionDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            emission = (
                Emission.objects.select_related("country", "emission_type")
                .filter(pk=pk)
                .first()
            )

            if not emission:
                return Response(
                    {"detail": f"No se encontró la emisión con id={pk}."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = EmissionSerializer(emission)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"detail": "Error interno del servidor", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
