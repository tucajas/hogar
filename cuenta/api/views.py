from rest_framework import generics
from cuenta.api.serializers import CuentaSerializer
from cuenta.models import Cuenta

class CuentaList(generics.ListCreateAPIView):
    queryset            = Cuenta.objects.all()
    serializer_class    = CuentaSerializer

class CuentaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset            = Cuenta.objects.all()
    serializer_class    = CuentaSerializer