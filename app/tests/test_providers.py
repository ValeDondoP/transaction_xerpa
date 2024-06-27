import pytest
from app.providers import keyword as keyword_providers
from django.test import TestCase


@pytest.mark.django_db
def test_get_keywords_by_description_words(setup_keywords_commerces_categories):
    description_words = ['keyword1', 'keyword2']

    keywords = keyword_providers.get_keywords_by_description_words(description_words)

    assert keywords.count() == 2
    for keyword in keywords:
        assert keyword.merchant.category is not None