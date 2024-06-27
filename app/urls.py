from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrichmentAPIView


router = DefaultRouter()

router.register(r'enrichment', EnrichmentAPIView, basename='enrichment')

urlpatterns = [
    path('', include(router.urls)),
]