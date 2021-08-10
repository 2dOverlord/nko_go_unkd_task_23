import json

def lambda_handler(event, context):
    # TODO implement
    text = "Hello World"
    return {
        'statusCode': 200,
        'body': json.dumps(text)
    }
