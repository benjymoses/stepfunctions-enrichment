
def lambda_handler(event, context):
    # Mocking returning an order's details
    # In reality you would ingest the order ID
    # from the event object and return details
    # from an orders system.
    
    order = {
        "id": 1234,
        "customerName": "John Doe",
        "productId": 1,
        "keepPdf": True
    }
    return {
        'statusCode': 200,
        'order': order
    }
