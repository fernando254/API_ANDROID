from django.shortcuts import render

from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializers

# Create your views here.

def home(request):
    return render(request, "core/home.html")


class UsuariViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers