import pytest
from django.test import Client
from app.models import Category, Commerce, Keyword

@pytest.fixture
def setup_keywords_commerces_categories():
    category1 = Category.objects.create(name='Category 1', type='expense')
    category2 = Category.objects.create(name='Category 2', type='income')

    commerce1 = Commerce.objects.create(merchant_name='Commerce 1', merchant_logo='http://example.com/logo1.png', category=category1)
    commerce2 = Commerce.objects.create(merchant_name='Commerce 2', merchant_logo='http://example.com/logo2.png', category=category2)

    Keyword.objects.create(keyword='keyword1', merchant=commerce1)
    Keyword.objects.create(keyword='keyword2', merchant=commerce2)


@pytest.fixture
def client():
    return Client()
