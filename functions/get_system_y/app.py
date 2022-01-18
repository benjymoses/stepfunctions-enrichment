def lambda_handler(event, context):
    # Mocking returning more info from system Y
    
    customerInfo = {
        "contactPref": "email",
        "email": "johndoe@example.com"

    }
    return {
        'statusCode': 200,
        'order': customerInfo
    }
