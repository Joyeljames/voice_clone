from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from tts import generate_tts
from stt import speech_to_text

app = FastAPI()

# ✅ serve ONLY CSS & JS
app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")


# ✅ load index.html
@app.get("/")
async def home():
    return FileResponse("../frontend/index.html")


# ✅ TEXT → SPEECH
@app.post("/tts/")
async def tts_api(text: str = Form(...)):
    output = generate_tts(text)
    return FileResponse(output, media_type="audio/wav")


# ✅ SPEECH → TEXT
@app.post("/stt/")
async def stt_api(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = speech_to_text(file_path)
    return {"text": text}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)