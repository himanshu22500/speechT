import json
from pprint import pprint

import requests
alternativeLanguageCodes = ['en-IN']


diarizationConfig = {
  "enableSpeakerDiarization": True,
  "minSpeakerCount": 1,
  "maxSpeakerCount":2,
}


def make_request_get_name_english():
    url = (
        "https://speech.googleapis.com/v2/speech:longrunningrecognize?key=AIzaSyA0afzOhl0U3k78SQIzskM9iMg5UnVcNi4"
    )
    uri = 'gs://himanshu-data/callcenterEng.wav'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "config": {"languageCode": "en-IN",
                   "audioChannelCount": 1,
                   "alternativeLanguageCodes": alternativeLanguageCodes,
                   "diarizationConfig" : diarizationConfig,
                   "enableSpokenPunctuation": True
                   },
        "audio": {"uri": uri},
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

    # print(dir(response))
    print(response.content)
    # if response.status_code == 200:
    #     print("POST request successful")
    #     print(response.json())
    # else:
    #     print(response.json())

make_request_get_name_english()
