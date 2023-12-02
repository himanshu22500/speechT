import json
from pprint import pprint

import requests


def make_request_get_name_english():
    alternativeLanguageCodes = ['en-IN']
    url = (
        "https://speech.googleapis.com/v1p1beta1/speech:longrunningrecognize?key=AIzaSyA0afzOhl0U3k78SQIzskM9iMg5UnVcNi4"
    )

    uri = 'gs://himanshu-data/teleenglish.mp3'

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    diarizationConfig = {
        "enableSpeakerDiarization": True,
        "minSpeakerCount": 1,
        "maxSpeakerCount": 2
    }

    data = {
        "config": {"languageCode": "en-US",
                   "audioChannelCount": 1,
                   "diarizationConfig": diarizationConfig,
                   "encoding": "MP3"
                   },
        "audio": {"uri": uri},
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

    if response.status_code == 200:
        print("POST request successful")
        print(response.json())
    else:
        print("Error:", response.status_code)
        print(response.json())


def make_request_get_name_hindi():
    alternativeLanguageCodes = ['hi-IN', 'en-IN']
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
    alternativeLanguageCodes = ['te-IN', 'en-IN']
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


# make_request_get_name_hindi()
# make_request_get_name_telugu()
make_request_get_name_english()
