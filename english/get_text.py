from pprint import pprint

import requests


def get_text_from_name(name: str):
    headers = {
        "charset": "utf-8",
        "Content-Type": "application/json",
    }
    url = f"https://speech.googleapis.com/v1/operations/{name}?key=AIzaSyA0afzOhl0U3k78SQIzskM9iMg5UnVcNi4"
    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        pprint(data)

name = '1695386727389269488'

get_text_from_name(name=name)
