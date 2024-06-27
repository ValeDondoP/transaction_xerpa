from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer, TransactionListSerializer
from app import services as transaction_services

class EnrichmentAPIView(APIView):

    def post(self, request):
        serializer = TransactionListSerializer(data={'transactions': request.data})

        if serializer.is_valid():
            transactions = serializer.validated_data['transactions']
            breakpoint()
            enriched_transactions, metrics = transaction_services.enrich_transactions(transactions)
            created_transactions = transaction_services.create_enriched_transactions(enriched_transactions)
            response_serializer = TransactionSerializer(created_transactions, many=True)

            return Response({
                'created_transactions': response_serializer.data,
                'metrics': metrics
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
