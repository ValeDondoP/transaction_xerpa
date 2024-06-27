from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
from app import services as transaction_services

class EnrichmentAPIView(APIView):

    def post(self, request):
        transactions = request.data
        enriched_transactions, metrics = transaction_services.enrich_transactions(transactions)

        created_transactions = transaction_services.create_enriched_transactions(enriched_transactions)

        serializer = TransactionSerializer(created_transactions, many=True)

        return Response({
            'created_transactions': serializer.data,
            'metrics': metrics
        }, status=status.HTTP_201_CREATED)
