from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrichmentAPIView

urlpatterns = [
    path('enrichment/', EnrichmentAPIView.as_view(), name='enrichment'),
]
