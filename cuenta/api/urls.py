from django.urls import path
from cuenta.api.views import CuentaList,CuentaDetail

urlpatterns = [
    path('list/',CuentaList.as_view(), name='cuentalist'),
    path('<int:pk>', CuentaDetail.as_view())
]

