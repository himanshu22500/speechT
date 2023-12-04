curl -X POST -H "Content-Type: application/json; charset=utf-8" \
-H "Authorization: Bearer ya29.a0AfB_byCHvXGuQ4bm-HMrkx-YmWfx7e1ZYos-OZwYGeNAyuVUmQiw02XHAB5qug0mMnuK-E6Wu1Hd4Ygs0g4QAK9bC84NYbtoCAcG5DBSfgRDzlcxn5evCpRRIzfIrlojjcLIgLtzLQ932R8bPLpzbEVEniKQ7BU5oam60RZoXQaCgYKATkSARISFQHGX2Mie9mgVp02aeUqwz9CLMPjBQ0177" \
https://speech.googleapis.com/v2/projects/speechtxt34303/locations/global/recognizers/_:batchRecognize \
--data '{
  "files": [{
    "uri": "gs://himanshu-data/audio-files/callcenterEng.wav"
  }],
  "config": {
    "features": {
      "enableWordTimeOffsets": true,
      "enableWordConfidence": true,
      "enableAutomaticPunctuation": true,
      "enableSpokenPunctuation": true
    },
    "explicitDecodingConfig": {
      "encoding": "LINEAR16",
      "sampleRateHertz": 48000,
      "audioChannelCount": 1
    },
    "model": "long",
    "languageCodes": ["en-IN"]
  },
  "recognitionOutputConfig": {
    "gcsOutputConfig": {
      "uri": "gs://himanshu-data/transcripts"
    }
  }
}'