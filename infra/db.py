import boto3
import os


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE', 'cnj'))

def save_response(cnj: str, data: dict):
    table.put_item(
        Item={
            'cnj': cnj,
            'status': 'processed',
            'data': data
        }
    )

