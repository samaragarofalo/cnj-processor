from protocol import lambda_handler
import json
import os

os.environ["AWS_REGION"] = "us-east-1"

def test_lambda_handler_valid_event(monkeypatch):
    class MockSQS:
        def send_message(self, QueueUrl, MessageBody):
            return {'MessageId': '12345'}

    monkeypatch.setattr(lambda_handler, 'sqs', MockSQS())
    monkeypatch.setenv('AUTH_TOKEN', 'meu-token-secreto')

    event = {
        'headers': {'Authorization': 'Bearer meu-token-secreto'},
        'body': json.dumps({'cnj': '0000001-00.2023.1.01.0001'})
    }

    response = lambda_handler.lambda_handler(event, None)

    assert response['statusCode'] == 202