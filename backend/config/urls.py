from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import VagaViewSet

router = routers.DefaultRouter()
router.register(r'vagas', VagaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
