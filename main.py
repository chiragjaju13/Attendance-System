import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from config import ADMIN_PASSWORD

ROOT = os.path.dirname(os.path.abspath(__file__))

def open_admin():
    pwd = simpledialog.askstring("Admin Login", "Enter admin password:", show="*")
    if not pwd:
        return
    if pwd == ADMIN_PASSWORD:
        import admin_panel
        root.destroy()
        admin_panel.launch_admin_panel(ROOT)
    else:
        messagebox.showerror("Access Denied", "Incorrect password")

def open_attendance():
    subject = simpledialog.askstring("Subject", "Enter subject name for attendance:")
    if not subject:
        return
    import attendance_mark
    root.destroy()
    attendance_mark.start_attendance(ROOT, subject.strip())

if __name__ == '__main__':
    root = tk.Tk()
    root.title("CLASS VISION - Face Attendance System (v4.1)")
    root.geometry("820x520")
    root.configure(bg="#0f172a")

    tk.Label(root, text="CLASS VISION", font=("Poppins", 36, "bold"), bg="#0f172a", fg="#6366f1").pack(pady=30)
    tk.Label(root, text="Manual Face Recognition Attendance", font=("Poppins", 16), bg="#0f172a", fg="#94a3b8").pack(pady=5)

    tk.Button(root, text="👨‍🏫 Admin Panel", font=("Poppins", 18, "bold"),
               bg="#1e293b", fg="white", width=22, command=open_admin).pack(pady=30)

    tk.Button(root, text="📸 Take Attendance", font=("Poppins", 18, "bold"),
               bg="#1e293b", fg="white", width=22, command=open_attendance).pack(pady=10)

    root.mainloop()
