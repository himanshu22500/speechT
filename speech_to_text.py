import json
from pprint import pprint

import requests

# name = "6083325727205717507"
# name = "2865392937490163172"
# name = "5997399694986126409"
# name = "1828657378938287790"
# name = "7426413194461813845"
# name = "397449988648339781"

alternativeLanguageCodes = ['te-IN', 'hi-IN', 'en-IN']

diarizationConfig = {
    "enableSpeakerDiarization": True,
    "minSpeakerCount": 1,
    "maxSpeakerCount": 2
}


def make_request_get_name_english():
    url = (
        "https://speech.googleapis.com/v1p1beta1/speech:longrunningrecognize?key=AIzaSyA0afzOhl0U3k78SQIzskM9iMg5UnVcNi4"
    )
    uri = 'gs://himanshu-data/2peopleTest.flac'
    storage_uri = "gs://himanshu-data/empty"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "config": {"languageCode": "en-US",
                   "audioChannelCount": 2,
                   "alternativeLanguageCodes": alternativeLanguageCodes,
                   "diarizationConfig": diarizationConfig
                   },
        "audio": {"uri": uri},
        "outputConfig": {
            "gcsUri": storage_uri
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

    if response.status_code == 200:
        print("POST request successful")
        print(response.json())
    else:
        print("Error:", response.status_code)
        print(response.json())


def make_request_get_name_hindi():
    url = (
        "https://speech.googleapis.com/v1p1beta1/speech:longrunningrecognize?key=AIzaSyA0afzOhl0U3k78SQIzskM9iMg5UnVcNi4"
    )
    uri = 'gs://himanshu-data/hindi2people.flac'
    storage_uri = "gs://himanshu-data/empty"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "config": {"languageCode": "hi-IN",
                   "audioChannelCount": 2,
                   "enableSeparateRecognitionPerChannel": True,
                   "alternativeLanguageCodes": alternativeLanguageCodes,
                   "maxAlternatives": 1
                   },
        "audio": {"uri": uri},
        "outputConfig": {
            "gcsUri": storage_uri
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

    if response.status_code == 200:
        print("POST request successful")
        print(response.json())
    else:
        print("Error:", response.status_code)
        print(response.json())


def make_request_get_name_telugu():
    url = (
        "https://speech.googleapis.com/v1p1beta1/speech:longrunningrecognize?key=AIzaSyA0afzOhl0U3k78SQIzskM9iMg5UnVcNi4"
    )
    uri = 'gs://himanshu-data/telegu2people.flac'
    storage_uri = "gs://himanshu-data/empty"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "config": {"languageCode": "te-IN",
                   "audioChannelCount": 2,
                   "enableSeparateRecognitionPerChannel": True
                   },
        "audio": {"uri": uri},
        "outputConfig": {
            "gcsUri": storage_uri
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

    if response.status_code == 200:
        print("POST request successful")
        print(response.json())
    else:
        print("Error:", response.status_code)
        print(response.json())


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
        ans = ''
        for alternative in data['response']['results']:
            ans += alternative['alternatives'][0]['transcript'] + " "
            # pprint(alternative['alternatives'][0]['transcript'])
        # print(ans)
    else:
        pprint(data)


# name = '417634131836681070'
name = '9180200529766432720'
# make_request_get_name_hindi()
# make_request_get_name_telugu()
make_request_get_name_english()
get_text_from_name(name=name)
