import json
import boto3
from app.usecase import cnj_validator


sqs = boto3.client('sqs')

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/086266612675/cnj-queue'


def lambda_handler(event, context):
    headers = event.get('headers', {})
    auth_header = headers.get('Authorization', '')
    expected_token = os.environ.get('AUTH_TOKEN')

    if not auth_header.startswith('Bearer ') or auth_header.split(' ')[1] != expected_token:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Unauthorized'})
        }
        
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