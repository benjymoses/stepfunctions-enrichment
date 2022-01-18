def lambda_handler(event, context):
    # In reality, you would perform work to
    # create the end PDF and store it in S3
    # then return the Bucket name and object
    # key for StepFunctions to carry on using.

    return {
        'statusCode': 200,
        's3PDF-uri': "s3://bucket/pdfKeyValue.pdf"
    }
