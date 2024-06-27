import pytest
import uuid
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from app.models import Transaction
from app.serializers import TransactionListSerializer


@pytest.mark.django_db
class TestEnrichmentAPIView:
    def test_enrichment_api_view_happy_path(self, setup_keywords_commerces_categories):
        client = APIClient()
        url = reverse('enrichment')

        transactions_data = [
            {'id': str(uuid.uuid4()), 'description': 'keyword1', 'amount': 100.0, 'date': '2024-06-28'},
            {'id': str(uuid.uuid4()), 'description': 'KEYWORD2 * BLAH', 'amount': 150.0, 'date': '2024-06-28'},
        ]

        response = client.post(url, data={'transactions': transactions_data}, format='json')


        assert response.status_code == status.HTTP_201_CREATED


        response_data = response.data
        assert 'created_transactions' in response_data
        assert 'metrics' in response_data


        created_transactions = response_data['created_transactions']

        assert len(created_transactions) == 2

    def test_enrichment_api_view_error(self, setup_keywords_commerces_categories):
        client = APIClient()
        url = reverse('enrichment')

        transactions_data = [
            {'id': str(uuid.uuid4()), 'description': 'keyword1', 'amount': 100.0, 'date': '2024-06-28'},
            { 'description': 'KEYWORD2 * BLAH', 'amount': 150.0, 'date': '2024-06-28'},
        ]

        response = client.post(url, data={'transactions': transactions_data}, format='json')


        assert response.status_code == status.HTTP_400_BAD_REQUEST
