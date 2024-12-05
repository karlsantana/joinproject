# targets/api_views.py
from rest_framework import viewsets
from .models import Alvo
from .serializers import AlvoSerializer

class AlvoViewSet(viewsets.ModelViewSet):
    queryset = Alvo.objects.all()
    serializer_class = AlvoSerializer
