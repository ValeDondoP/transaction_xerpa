from app.models import Transaction

def bulk_create_transactions(transactions):
    created_transactions = []
    for transaction_data in transactions:
        try:
            # Extracting fields with default to None if not provided
            category_id = transaction_data.get('category_id')
            merchant_id = transaction_data.get('merchant_id')

            transaction = Transaction.objects.create(
                id=transaction_data['id'],
                description=transaction_data['description'],
                amount=transaction_data['amount'],
                date=transaction_data['date'],
                category_id=category_id,
                merchant_id=merchant_id
            )
            created_transactions.append(transaction)
        except Exception as e:
            print(f"Error creating transaction: {e}")


    return created_transactions
