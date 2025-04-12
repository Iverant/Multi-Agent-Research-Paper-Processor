from gtts import gTTS
import os

def text_to_audio(text:str, filename: str = "podcast.mp3"):
    
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)  

    out_path = f"{output_dir}/{filename}"
    tts = gTTS(text=text, lang="en")
    tts.save(out_path)

