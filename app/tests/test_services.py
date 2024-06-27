import pytest
from unittest.mock import patch
from app.services import create_enriched_transactions

@pytest.mark.django_db
class TestCreateEnrichedTransactions:
    @patch('app.services.transaction_provider.bulk_create_transactions')
    def test_create_enriched_transactions_happy_path(self, mock_bulk_create_transaction):
        fake_transactions = ["transaction1", "transaction2"]

        mock_bulk_create_transaction.return_value = fake_transactions

        result = create_enriched_transactions(fake_transactions)

        assert result is not None
        assert  mock_bulk_create_transaction.called_once()

    @patch('app.services.transaction_provider.bulk_create_transactions')
    def test_create_enriched_transactions_error(self, mock_bulk_create_transaction):
        mock_bulk_create_transaction.side_effect = Exception("Error")
        fake_transactions = ["transaction1", "transaction2"]

        assert create_enriched_transactions(fake_transactions) == []