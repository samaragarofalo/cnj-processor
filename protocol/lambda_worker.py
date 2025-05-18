import json
from infra.client_api import fetch_data
from infra.db import save_response


def lambda_worker(event, context):
    for record in event['Records']:
        cnj = record['body']
        data = fetch_data(cnj)

        save_response(cnj, data)
