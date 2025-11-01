import tkinter as tk, os
from tkinter import messagebox
import config

def edit_config(ROOT):
    win = tk.Tk(); win.title("Config Editor"); win.geometry("480x260")
    tk.Label(win, text="Edit configuration values and Save", font=("Arial",12)).pack(pady=8)
    tk.Label(win, text="Admin Password:").pack(); pwd = tk.Entry(win); pwd.pack(); pwd.insert(0, config.ADMIN_PASSWORD)
    tk.Label(win, text="Camera Source (0 for webcam):").pack(); cam = tk.Entry(win); cam.pack(); cam.insert(0, str(config.CAMERA_SOURCE))
    tk.Label(win, text="Capture Duration (seconds):").pack(); dur = tk.Entry(win); dur.pack(); dur.insert(0, str(config.CAPTURE_DURATION_SECONDS))

    def save():
        new_pwd = pwd.get().strip(); new_cam = cam.get().strip(); new_dur = dur.get().strip()
        cfg = f"""CAMERA_SOURCE = {new_cam if new_cam.isdigit() else repr(new_cam)}\nCAPTURE_DURATION_SECONDS = {int(new_dur)}\nADMIN_PASSWORD = {repr(new_pwd)}\nDATA_DIR = 'data'\nTRAINING_DIR = 'data/TrainingImage'\nSTUDENT_CSV = 'data/StudentDetails/studentdetails.csv'\nMODEL_FILE = 'models/Trainner.yml'\n"""
        try:
            with open(os.path.join(ROOT, 'config.py'), 'w', encoding='utf-8') as f:
                f.write(cfg)
            messagebox.showinfo('Saved', 'Config saved. Restart app to apply changes.')
            win.destroy()
        except Exception as e:
            messagebox.showerror('Error', str(e))

    tk.Button(win, text='Save', command=save, width=20).pack(pady=10)
    tk.Button(win, text='Cancel', command=win.destroy, width=20).pack()
    win.mainloop()
