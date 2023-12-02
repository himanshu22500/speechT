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

# name = '3766977151366770035'
# name = '4340018846644737943'
# name = '427810133907832591'
# name = '135234390829225826'
# name = '7194737779870531350'
name = '4291281005382917963'

get_text_from_name(name=name)
