import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import torch
import torchaudio
import sounddevice as sd
import numpy as np
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification, pipeline
from fer import FER
from moviepy.editor import *

# ---------------------------
# Load models
# ---------------------------
face_detector = FER(mtcnn=True)

audio_model_name = "superb/hubert-large-superb-er"
audio_extractor = AutoFeatureExtractor.from_pretrained(audio_model_name)
audio_model = AutoModelForAudioClassification.from_pretrained(audio_model_name)

text_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# ---------------------------
# Voice recording and analysis
# ---------------------------
def record_audio(duration=4, sample_rate=16000):
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    return torch.tensor(audio).squeeze()

def predict_emotion_audio(audio_tensor, sample_rate=16000):
    inputs = audio_extractor(audio_tensor, sampling_rate=sample_rate, return_tensors="pt")
    with torch.no_grad():
        logits = audio_model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    return audio_model.config.id2label[predicted_id]

# ---------------------------
# GUI Application
# ---------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multimodal Mood Recognition")
        self.geometry("700x500")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Tabs
        self.face_tab = ttk.Frame(self.notebook)
        self.voice_tab = ttk.Frame(self.notebook)
        self.text_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.face_tab, text="Face")
        self.notebook.add(self.voice_tab, text="Voice")
        self.notebook.add(self.text_tab, text="Text")

        # Face tab
        self.cap = None
        self.face_label = tk.Label(self.face_tab)
        self.face_label.pack()
        self.start_face_btn = tk.Button(self.face_tab, text="Start Webcam", command=self.start_webcam)
        self.start_face_btn.pack(pady=10)
        self.stop_face_btn = tk.Button(self.face_tab, text="Stop Webcam", command=self.stop_webcam)
        self.stop_face_btn.pack(pady=5)

        # Voice tab
        self.voice_result = tk.Label(self.voice_tab, text="", font=("Arial", 16))
        self.voice_result.pack(pady=20)
        self.record_btn = tk.Button(self.voice_tab, text="Record & Analyze", command=self.analyze_voice)
        self.record_btn.pack()

        # Text tab
        self.text_input = tk.Text(self.text_tab, height=5, width=50)
        self.text_input.pack(pady=10)
        self.text_result = tk.Label(self.text_tab, text="", font=("Arial", 14))
        self.text_result.pack(pady=10)
        self.text_btn = tk.Button(self.text_tab, text="Analyze Text", command=self.analyze_text)
        self.text_btn.pack()

    # Face
    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def stop_webcam(self):
        if self.cap:
            self.cap.release()
        self.face_label.config(image="")

    def update_frame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                emotion_data = face_detector.detect_emotions(frame)
                if emotion_data:
                    top_emotion = max(emotion_data[0]['emotions'], key=emotion_data[0]['emotions'].get)
                    cv2.putText(frame, top_emotion, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = ImageTk.PhotoImage(Image.fromarray(rgb_frame))
                self.face_label.config(image=img)
                self.face_label.image = img
            self.after(10, self.update_frame)

    # Voice
    def analyze_voice(self):
        try:
            audio_tensor = record_audio()
            emotion = predict_emotion_audio(audio_tensor)
            self.voice_result.config(text=f"Detected Emotion: {emotion}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Text
    def analyze_text(self):
        try:
            text = self.text_input.get("1.0", tk.END).strip()
            if not text:
                return
            results = text_model(text)[0]
            best_emotion = max(results, key=lambda x: x['score'])['label']
            self.text_result.config(text=f"Detected Emotion: {best_emotion}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# ---------------------------
# Run the app
# ---------------------------
if __name__ == "__main__":
    try:
        App().mainloop()
    except KeyboardInterrupt:
        pass
