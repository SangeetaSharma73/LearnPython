import torch
import torchaudio
import sounddevice as sd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification, AutoTokenizer, AutoModelForSequenceClassification

# ----------------------------
# 1. Load models
# ----------------------------

# Audio emotion model
audio_model_name = "superb/hubert-large-superb-er"
extractor = AutoFeatureExtractor.from_pretrained(audio_model_name)
audio_model = AutoModelForAudioClassification.from_pretrained(audio_model_name)

# Text emotion model
text_model_name = "j-hartmann/emotion-english-distilroberta-base"
tokenizer = AutoTokenizer.from_pretrained(text_model_name)
text_model = AutoModelForSequenceClassification.from_pretrained(text_model_name)

# ----------------------------
# 2. Record audio
# ----------------------------
def record_audio(duration=4, sample_rate=16000):
    print(f"🎤 Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    print("✅ Recording complete.")
    return torch.tensor(audio).squeeze()

# ----------------------------
# 3. Predict emotion from audio
# ----------------------------
def predict_emotion_audio(audio_tensor, sample_rate=16000):
    inputs = extractor(audio_tensor, sampling_rate=sample_rate, return_tensors="pt")
    with torch.no_grad():
        logits = audio_model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    return audio_model.config.id2label[predicted_id]

# ----------------------------
# 4. Predict emotion from text
# ----------------------------
def predict_emotion_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = text_model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    return text_model.config.id2label[predicted_id]

# ----------------------------
# 5. Generate custom response
# ----------------------------
def generate_response(emotion):
    responses = {
        "joy": "😊 That's great to hear! Keep up the positive vibes!",
        "sadness": "💙 I'm here for you. Remember, tough times don't last forever.",
        "anger": "😠 I understand you're upset. Take a deep breath.",
        "fear": "😨 It’s okay to feel scared. You’re not alone.",
        "surprise": "😲 Wow! That’s unexpected.",
        "love": "❤️ Love makes the world brighter.",
        "neutral": "🙂 Got it."
    }
    return responses.get(emotion.lower(), f"I sense you're feeling {emotion.lower()}.")

# ----------------------------
# 6. GUI Functions
# ----------------------------
def start_recording():
    try:
        audio_tensor = record_audio(duration=4)
        emotion = predict_emotion_audio(audio_tensor)
        response = generate_response(emotion)
        result_label.config(text=f"🎯 Audio Emotion: {emotion}\n💬 Response: {response}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def analyze_text():
    try:
        text = text_entry.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text.")
            return
        emotion = predict_emotion_text(text)
        response = generate_response(emotion)
        result_label.config(text=f"📄 Text Emotion: {emotion}\n💬 Response: {response}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# ----------------------------
# 7. Tkinter GUI setup
# ----------------------------
window = tk.Tk()
window.title("Emotion Recognition (Audio + Text)")
window.geometry("500x400")

title_label = tk.Label(window, text="🎤📝 Emotion Detector", font=("Arial", 18))
title_label.pack(pady=10)

# Audio section
record_button = tk.Button(window, text="Start Recording (Audio)", font=("Arial", 14), command=start_recording)
record_button.pack(pady=10)

# Text section
text_label = tk.Label(window, text="Enter text to analyze:", font=("Arial", 14))
text_label.pack(pady=5)

text_entry = tk.Text(window, height=4, width=40, font=("Arial", 12))
text_entry.pack(pady=5)

analyze_button = tk.Button(window, text="Analyze Text", font=("Arial", 14), command=analyze_text)
analyze_button.pack(pady=10)

# Result
result_label = tk.Label(window, text="", font=("Arial", 14), wraplength=450, justify="left")
result_label.pack(pady=10)

window.mainloop()
