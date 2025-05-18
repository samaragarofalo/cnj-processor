from protocol import lambda_handler
import json


def test_lambda_handler_valid_event(monkeypatch):
    def mock_send_message(QueueUrl, MessageBody):
        return {'MessageId': '12345'}
    
    monkeypatch.setattr(lambda_handler.sqs, 'send_message', mock_send_message)

    event = {
        'body': json.dumps({
            'cnj': '0000001-00.2023.1.01.0001'
        })
    }

    response = lambda_handler.lambda_handler(event, None)

    assert response['statusCode'] == 202

