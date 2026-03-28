from transformers import pipeline

asr = pipeline("automatic-speech-recognition")

def speech_to_text(file_path):
    result = asr(file_path)
    return result["text"]