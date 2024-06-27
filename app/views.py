import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer, TransactionListSerializer, KeywordSerializer, CategorySerializer, CommerceSerializer
from app import services as transaction_services
from rest_framework import generics, pagination
from .models import Keyword, Category, Commerce
class EnrichmentAPIView(APIView):
    """
    Endpoint to enrich a transaction
    """
    def post(self, request):
        serializer = TransactionListSerializer(data={'transactions': request.data['transactions']})
        if serializer.is_valid():
            transactions = serializer.validated_data['transactions']

            enriched_transactions, metrics = transaction_services.enrich_transactions(transactions)
            created_transactions = transaction_services.create_enriched_transactions(enriched_transactions)
            response_serializer = TransactionSerializer(created_transactions, many=True)

            return Response({
                'created_transactions': response_serializer.data,
                'metrics': metrics
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeywordListAPIView(generics.ListAPIView):
    """
    Endpoint to get every Keyword in db
    """
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    pagination_class = pagination.PageNumberPagination


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = pagination.PageNumberPagination


class CommerceListAPIView(generics.ListAPIView):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    pagination_class = pagination.PageNumberPagination