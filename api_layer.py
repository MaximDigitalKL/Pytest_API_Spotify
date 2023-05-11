import requests
from functools import cache

TOKEN_HOST = "https://accounts.spotify.com"
API_HOST = "https://api.spotify.com/v1"


def call_api(api: str, method: str, payload: dict, headers=dict()):
    method_fn = dict(
        GET=requests.get,
        POST=requests.post,
        PUT=requests.put,
        DELETE=requests.delete,
    )
    api_url = f"{API_HOST}/{api}"
    actual_headers = headers | {"Content-Type": "application/json"}
    response = method_fn[method](api_url, json=payload, headers=actual_headers)
    return response
