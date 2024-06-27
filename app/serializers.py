from rest_framework import serializers
from .models import Transaction, Category, Commerce


class TransactionSerializerInput(serializers.Serializer):
    id = serializers.UUIDField()
    description = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

class CommerceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Commerce
        fields = ['id', 'merchant_name', 'merchant_logo', 'category']

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    merchant = CommerceSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'description', 'amount', 'date', 'category', 'merchant', 'created_at', 'updated_at']