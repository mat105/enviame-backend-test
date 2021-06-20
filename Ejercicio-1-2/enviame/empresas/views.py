from rest_framework import viewsets

from empresas.models import Company
from empresas.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.order_by('pk')
    serializer_class = CompanySerializer
