import os

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

# Instantiates a client
client = SpeechClient()

# The output path of the transcription result.
workspace = "gs://himanshu-data/transcripts"

# The name of the audio file to transcribe:
gcs_uri = "gs://himanshu-data/callcenterEng.wav"

# Recognizer resource name:
name = "projects/speechtxt34303/locations/asia-south1/recognizers/_"

config = cloud_speech.RecognitionConfig(
  explicit_decoding_config=cloud_speech.ExplicitDecodingConfig(
    encoding=cloud_speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    audio_channel_count=1,
  ),
  model="long",
  language_codes=["en-IN","hi-IN"],
  features=cloud_speech.RecognitionFeatures(
  enable_word_time_offsets=True,
  enable_word_confidence=True,
  enable_automatic_punctuation=True,
  enable_spoken_punctuation=True,
  ),
)

output_config = cloud_speech.RecognitionOutputConfig(
  gcs_output_config=cloud_speech.GcsOutputConfig(
    uri=workspace),
)

files = [cloud_speech.BatchRecognizeFileMetadata(
    uri=gcs_uri
)]

request = cloud_speech.BatchRecognizeRequest(
    recognizer=name, config=config, files=files, recognition_output_config=output_config
)
operation = client.batch_recognize(request=request)
print(operation.result())