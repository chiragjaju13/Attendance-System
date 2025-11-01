import tkinter as tk
from tkinter import messagebox
import os

def launch_admin_panel(ROOT):
    import student_capture, face_train, attendance_viewer, manage_students, config_editor
    win = tk.Tk()
    win.title("Admin Panel - Class Vision (v4.1)")
    win.geometry("800x520")
    win.configure(bg="#0f172a")

    tk.Label(win, text="Admin Dashboard", font=("Poppins", 26, "bold"), bg="#0f172a", fg="#a78bfa").pack(pady=20)

    frame = tk.Frame(win, bg="#0f172a")
    frame.pack(pady=10)

    tk.Button(frame, text="➕ Add Student", command=lambda: student_capture.open_capture_window(ROOT), width=20, height=2).grid(row=0, column=0, padx=12, pady=12)
    tk.Button(frame, text="🗃️ Manage Students", command=lambda: manage_students.manage_students(ROOT), width=20, height=2).grid(row=0, column=1, padx=12, pady=12)
    tk.Button(frame, text="🧠 Train Faces", command=lambda: face_train.train_faces(ROOT), width=20, height=2).grid(row=1, column=0, padx=12, pady=12)
    tk.Button(frame, text="📊 View Attendance", command=lambda: attendance_viewer.view_attendance(ROOT), width=20, height=2).grid(row=1, column=1, padx=12, pady=12)
    tk.Button(frame, text="⚙️ Config", command=lambda: config_editor.edit_config(ROOT), width=20, height=2).grid(row=2, column=0, padx=12, pady=12)

    tk.Button(win, text="🔙 Logout", command=lambda: [win.destroy(), __import__('main')], width=20, height=2, bg="#ef4444").pack(pady=18)

    win.mainloop()
