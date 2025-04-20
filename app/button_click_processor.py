import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['BUTTON_CLICKS_TABLE'])

def handler(event, context):
    print("Button click event received:", event)
    for record in event['Records']:
        # Decode the Kinesis record
        payload = json.loads(record['kinesis']['data'])

        # Save data to DynamoDB
        table.put_item(
            Item={
                'id': payload['id'],
                'timestamp': payload['timestamp'],
                'clickData': payload['clickData']
            }
        )
    return {
        "statusCode": 200,
        "body": "Button click recorded!"
    }
