from app.providers import transaction as transaction_provider
from app.providers import keyword as keyword_provider

def enrich_transactions(transactions):
        enriched_transactions = []
        unique_words = set()
        total_transactions = len(transactions)
        categorized_count = 0
        identified_merchant_count = 0

        # Collect unique words from all descriptions
        for transaction in transactions:
            description = transaction['description'].lower()
            unique_words.update(description.split())

        # Retrieve matched keywords in bulk
        matched_keywords = keyword_provider.get_keywords_by_description_words(unique_words)

        # Create a mapping for fast access
        keyword_to_merchant = {keyword.keyword: keyword.merchant for keyword in matched_keywords}
        keyword_to_category = {keyword.keyword: keyword.merchant.category for keyword in matched_keywords}

        for transaction in transactions:
            description = transaction['description'].lower()
            words = description.split()

            merchant = None
            category = None

            # Find the first matching
            for word in words:
                if word in keyword_to_merchant:
                    merchant = keyword_to_merchant[word]
                    category = keyword_to_category[word]
                    break

            # Prepare data for bulk creation
            transaction['category_id'] = category.id if category else None
            transaction['merchant_id'] = merchant.id if merchant else None

            if category:
                categorized_count += 1
            if merchant:
                identified_merchant_count += 1

            enriched_transactions.append(transaction)

        # Calculate metrics
        categorization_rate = (categorized_count / total_transactions) * 100 if total_transactions > 0 else 0
        identification_rate = (identified_merchant_count / total_transactions) * 100 if total_transactions > 0 else 0

        metrics = {
            'total_transactions': total_transactions,
            'categorization_rate': categorization_rate,
            'identification_rate': identification_rate
        }

        return enriched_transactions, metrics


def create_enriched_transactions(transactions):
    try:
        created_transactions = transaction_provider.bulk_create_transactions(transactions)
        return created_transactions
    except Exception as e:
        print(f"Error creating enriched transactions: {e}")
        return []