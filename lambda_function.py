import json

def lambda_handler(event, context):
    # TODO implement
    text = "Hello You 2"
    return {
        'statusCode': 200,
        'body': json.dumps(text)
    }
