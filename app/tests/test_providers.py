import pytest
import uuid
from datetime import datetime
from app.providers import keyword as keyword_providers
from app.providers import transaction as transaction_providers
from app.models import Commerce


@pytest.mark.django_db
def test_get_keywords_by_description_words(setup_keywords_commerces_categories):
    description_words = ['keyword1', 'keyword2']

    keywords = keyword_providers.get_keywords_by_description_words(description_words)

    assert keywords.count() == 2
    for keyword in keywords:
        assert keyword.merchant.category is not None


@pytest.mark.django_db
def test_get_keywords_by_description_words_no_data():
    description_words = ['keyword1', 'keyword2']

    keywords = keyword_providers.get_keywords_by_description_words(description_words)

    assert keywords.count() == 0


@pytest.mark.django_db
class TestTransactionService:
    def test_bulk_create_transactions_no_merchant(self):
        transactions_data = [
            {
                'id': uuid.uuid4(),
                'description': 'Test Transaction 1',
                'amount': 100.0,
                'date': '2024-06-28',
                'category_id': None,
                'merchant_id': None
            },
            {
                'id': uuid.uuid4(),
                'description': 'Test Transaction 2',
                'amount': 150.0,
                'date': '2024-06-29',
                'category_id': None,
                'merchant_id': None
            }
        ]

        created_transactions = transaction_providers.bulk_create_transactions(transactions_data)


        assert len(created_transactions) == len(transactions_data)
        for transaction, transaction_data in zip(created_transactions, transactions_data):
            assert transaction.id == transaction_data['id']
            assert transaction.description == transaction_data['description']
            assert transaction.amount == transaction_data['amount']

            assert transaction.date == transaction_data['date']


    def test_bulk_create_transactions_with_merchant(self, setup_keywords_commerces_categories):
        commerce = Commerce.objects.first()
        transactions_data = [
            {
                'id': uuid.uuid4(),
                'description': 'Test Transaction 1',
                'amount': 100.0,
                'date': '2024-06-28',
                'category_id': commerce.category_id,
                'merchant_id': commerce.id
            }
        ]

        created_transactions = transaction_providers.bulk_create_transactions(transactions_data)


        assert len(created_transactions) == len(transactions_data)
        for transaction, transaction_data in zip(created_transactions, transactions_data):
            assert transaction.merchant_id == transaction_data['merchant_id']
            assert transaction.category_id == transaction_data['category_id']

