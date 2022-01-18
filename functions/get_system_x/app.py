def lambda_handler(event, context):
    # Mocking returning more info from system X
    
    marketingDetails = {
        "rewardTier": "Silver",
        "loyaltyPoints": 200

    }
    return {
        'statusCode': 200,
        'order': marketingDetails
    }
