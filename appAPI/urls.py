from django.urls import path, include
from rest_framework import routers
from .views import BukuViewSet, PenulisViewSet

router = routers.DefaultRouter()
router.register(r'^buku', BukuViewSet)
router.register(r'^penulis', PenulisViewSet)

app_name = 'appAPI'

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
