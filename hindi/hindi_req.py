import json
from pprint import pprint

import requests
alternativeLanguageCodes = ['en-IN']

# diarizationConfig = {
#     "enableSpeakerDiarization": True,
#     "minSpeakerCount": 1,
#     "maxSpeakerCount": 2
# }
def make_request_get_name_hindi():
    url = (
        "https://speech.googleapis.com/v1p1beta1/speech:longrunningrecognize?key=AIzaSyA0afzOhl0U3k78SQIzskM9iMg5UnVcNi4"
    )
    uri = 'gs://himanshu-data/callcenter.mp3'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "config": {"languageCode": "hi-IN",
                   "encoding":"MP3",
                   "audioChannelCount": 2,
                   "alternativeLanguageCodes": alternativeLanguageCodes,
                   "maxAlternatives": 1,
                   "useEnhanced": True
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

make_request_get_name_hindi()
