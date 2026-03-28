from TTS.api import TTS
import uuid

# load model (once)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

def generate_tts(text):
    output_path = f"output_{uuid.uuid4()}.wav"

    tts.tts_to_file(
        text=text,
        file_path=output_path
    )

    return output_path