import uuid
from django.db import models

class UUIDPrimaryKey(models.Model):
    """
    An abstract base class model that provides
    primary key id as uuid.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Category(UUIDPrimaryKey):
    EXPENSE = 'expense'
    INCOME = 'income'
    CATEGORY_TYPE_CHOICES = [
        (EXPENSE, 'Expense'),
        (INCOME, 'Income'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=CATEGORY_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Commerce(UUIDPrimaryKey):
    merchant_name = models.CharField(max_length=255)
    merchant_logo = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='commerces')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Commerce'
        verbose_name_plural = 'Commerces'

    def __str__(self):
        return self.merchant_name


class Keyword(UUIDPrimaryKey):
    keyword = models.CharField(max_length=255)
    merchant = models.ForeignKey(Commerce, on_delete=models.CASCADE, related_name='keywords')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'

    def __str__(self):
        return self.keyword

class Transaction(UUIDPrimaryKey):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    merchant = models.ForeignKey(Commerce, on_delete=models.SET_NULL, null=True, related_name='transactions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return self.description