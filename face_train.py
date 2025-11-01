import os, cv2, numpy as np
from PIL import Image
import tkinter as tk
from tkinter import messagebox

def getImagesAndLabels(path):
    imagePaths = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith('.jpg') or f.lower().endswith('.png'):
                imagePaths.append(os.path.join(root, f))
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        try:
            parts = os.path.basename(imagePath).split('_')
            Id = int(parts[1])
        except Exception:
            continue
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

def train_faces(ROOT):
    train_path = os.path.join(ROOT, "data", "TrainingImage")
    label_dir = os.path.join(ROOT, "models")
    os.makedirs(label_dir, exist_ok=True)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, Ids = getImagesAndLabels(train_path)
    if not faces:
        messagebox.showerror("Error", "No training images found. Add students first.")
        return
    recognizer.train(faces, np.array(Ids))
    recognizer.save(os.path.join(label_dir, "Trainner.yml"))
    messagebox.showinfo("Success", "Training completed and model saved to models/Trainner.yml")
