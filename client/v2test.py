from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

# Instantiates a client
client = SpeechClient()

# The output path of the transcription result.
workspace = "gs://himanshu-data/transcripts"

# The name of the audio file to transcribe:
gcs_uri = "gs://himanshu-data/audio-files/callcenterEng.wav"

# Recognizer resource name:
name = "projects/speechtxt34303/locations/global/recognizers/_"

# noinspection PyTypeChecker
config = cloud_speech.RecognitionConfig(
    auto_decoding_config={},
    model="long",
    language_codes=["hi-IN"],
    features=cloud_speech.RecognitionFeatures(
        enable_word_time_offsets=True,
        enable_word_confidence=True,
    ),
)

# noinspection PyTypeChecker
output_config = cloud_speech.RecognitionOutputConfig(
    gcs_output_config=cloud_speech.GcsOutputConfig(
        uri=workspace),
)

# noinspection PyTypeChecker
files = [cloud_speech.BatchRecognizeFileMetadata(
    uri=gcs_uri
)]

# noinspection PyTypeChecker
request = cloud_speech.BatchRecognizeRequest(
    recognizer=name, config=config, files=files, recognition_output_config=output_config
)
operation = client.batch_recognize(request=request)
print(operation.result())
