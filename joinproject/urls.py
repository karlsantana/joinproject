from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from targets.api_views import AlvoViewSet
from targets import views


router = routers.DefaultRouter()
router.register(r'alvos', AlvoViewSet)

urlpatterns = [
    path('', views.mapa_view, name='mapa'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
