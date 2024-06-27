from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrichmentAPIView, KeywordListAPIView, CategoryListAPIView, CommerceListAPIView

urlpatterns = [
    path('enrichment/', EnrichmentAPIView.as_view(), name='enrichment'),
    path('keywords/', KeywordListAPIView.as_view(), name='keyword-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('commerce/', CommerceListAPIView.as_view(), name='commerce-list'),
]
