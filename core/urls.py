from django.urls import path, include
from .views import home, UsuariViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'usuarios', UsuariViewSet)

urlpatterns = [
    path('',home, name="home"),
    path('api/', include(router.urls)),
]
