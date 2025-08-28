import torch
import torchaudio
import sounddevice as sd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification

# 1. Load the pretrained emotion recognition model
model_name = "superb/hubert-large-superb-er"
extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = AutoModelForAudioClassification.from_pretrained(model_name)

# 2. Record audio from microphone
def record_audio(duration=4, sample_rate=16000):
    print(f"🎤 Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    print("✅ Recording complete.")
    return torch.tensor(audio).squeeze()

# 3. Predict emotion from audio
def predict_emotion(audio_tensor, sample_rate=16000):
    inputs = extractor(audio_tensor, sampling_rate=sample_rate, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    return model.config.id2label[predicted_id]

# 4. GUI Functionality
def start_recording():
    try:
        audio_tensor = record_audio(duration=4)
        emotion = predict_emotion(audio_tensor)
        result_label.config(text=f"🎯 Detected Emotion: {emotion}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# 5. Tkinter GUI setup
window = tk.Tk()
window.title("Emotion Recognition from Audio")
window.geometry("400x200")

title_label = tk.Label(window, text="🎤 Emotion Detector", font=("Arial", 18))
title_label.pack(pady=10)

record_button = tk.Button(window, text="Start Recording", font=("Arial", 14), command=start_recording)
record_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack(pady=10)

window.mainloop()
