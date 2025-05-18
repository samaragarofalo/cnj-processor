import json
import boto3
from app.usecase import cnj_validator


sqs = boto3.client('sqs')

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/086266612675/cnj-queue'


def lambda_handler(event, context):
    body = json.loads(event['body'])
    cnj = body.get('cnj')

    if not cnj_validator(cnj):
        return {
            'statusCode': 400, 
            'body': json.dumps(
                {'error': 'Invalid CNJ format'}
            )
        }
    
    sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=cnj)

    return {
        'statusCode': 202,
        'body': json.dumps({
                'message': f'Proccess initiated for CNJ: {cnj}', 
                'status': 'queued'
        })
    }