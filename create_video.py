from gtts import gTTS
import pyttsx3
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip

def text_to_speech_gtts(text, audio_filename="summary.mp3"):
    tts = gTTS(text)
    tts.save(audio_filename)
    return audio_filename

def text_to_speech_pyttsx3(text, audio_filename="summary.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, audio_filename)
    engine.runAndWait()
    return audio_filename

def create_video_summary(image_path, audio_path, output_path="summary_video.mp4", duration=30):
    clip = ImageClip(image_path).set_duration(duration)
    audio = AudioFileClip(audio_path)
    
    video = clip.set_duration(audio.duration).set_audio(audio)
    
    video.write_videofile(output_path, fps=24)
    return output_path
