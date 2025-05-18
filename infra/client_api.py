import requests


def fetch_data(cnj: str) -> dict:
    response = requests.get('https://api.teste/{cjn}')

    return response.json() if response.status_code == 200 else {'error': response.status_code}
