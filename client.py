"""Google Cloud Speech API sample that demonstrates enhanced models
and recognition metadata.

Example usage:
    python beta_snippets.py diarization
    python beta_snippets.py multi-channel
    python beta_snippets.py multi-language
"""

import argparse

from google.cloud import speech_v1p1beta1 as speech

def transcribe_file_with_diarization() -> speech.RecognizeResponse:
    """Transcribe the given audio file synchronously with diarization."""
    # [START speech_transcribe_diarization_beta]
    from google.cloud import speech_v1p1beta1 as speech

    client = speech.SpeechClient()

    speech_file = "/home/flowwai-dev-nw05/Downloads/callcenter.mp3"

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    diarization_config = speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        min_speaker_count=2,
        max_speaker_count=10,
    )

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=48000,
        language_code="hi-IN",
        diarization_config=diarization_config,
    )

    print("Waiting for operation to complete...")
    response = client.recognize(config=config, audio=audio)

    # The transcript within each result is separate and sequential per result.
    # However, the words list within an alternative includes all the words
    # from all the results thus far. Thus, to get all the words with speaker
    # tags, you only have to take the words list from the last result:
    result = response.results[-1]

    words_info = result.alternatives[0].words

    # Printing out the output:
    for word_info in words_info:
        print(f"word: '{word_info.word}', speaker_tag: {word_info.speaker_tag}")

    return result
    # [END speech_transcribe_diarization_beta]


def transcribe_file_with_multichannel() -> speech.RecognizeResponse:
    """Transcribe the given audio file synchronously with
    multi channel."""
    # [START speech_transcribe_multichannel_beta]
    from google.cloud import speech_v1p1beta1 as speech

    client = speech.SpeechClient()

    speech_file = "resources/Google_Gnome.wav"

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        audio_channel_count=1,
        enable_separate_recognition_per_channel=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
        print(f"Channel Tag: {result.channel_tag}")

    return response.results
    # [END speech_transcribe_multichannel_beta]

def transcribe_file_with_multilanguage() -> speech.RecognizeResponse:
    """Transcribe the given audio file synchronously with
    multi language."""
    # [START speech_transcribe_multilanguage_beta]
    from google.cloud import speech_v1p1beta1 as speech

    client = speech.SpeechClient()

    speech_file = "resources/multi.wav"
    first_lang = "en-US"
    second_lang = "es"

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        audio_channel_count=2,
        language_code=first_lang,
        alternative_language_codes=[second_lang],
    )

    print("Waiting for operation to complete...")
    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}: {alternative}")
        print(f"Transcript: {alternative.transcript}")

    return response.results
    # [END speech_transcribe_multilanguage_beta]

if __name__ == "__main__":
    transcribe_file_with_diarization()
    # transcribe_file_with_multichannel()
    # transcribe_file_with_multilanguage()