import pyttsx3
import os

def generate_audio(slides, outdir='outputs'):
    engine = pyttsx3.init()
    audio_dir = os.path.join(outdir, 'audio')
    os.makedirs(audio_dir, exist_ok=True)
    for i, s in enumerate(slides):
        path = os.path.join(audio_dir, f'slide_{i+1:02d}.mp3')
        engine.save_to_file(s['title'], path)
    engine.runAndWait()
