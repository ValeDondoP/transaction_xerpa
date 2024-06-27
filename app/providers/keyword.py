from app.models import Keyword


def get_keywords_by_description_words(description_words):
    return Keyword.objects.filter(keyword__in=description_words).select_related('merchant__category')
