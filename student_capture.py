import os, cv2, time
import tkinter as tk
from tkinter import messagebox
import threading
from config import CAMERA_SOURCE

def ensure_dirs(ROOT):
    os.makedirs(os.path.join(ROOT, "data", "TrainingImage"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "data", "StudentDetails"), exist_ok=True)

def open_capture_window(ROOT):
    ensure_dirs(ROOT)
    win = tk.Tk()
    win.title("Add Student - Multi-angle Capture")
    win.geometry("640x420")
    win.configure(bg="#1b1b2f")

    tk.Label(win, text="Enrollment:", bg="#1b1b2f", fg="white").place(x=20, y=20)
    enr_entry = tk.Entry(win); enr_entry.place(x=120, y=20)

    tk.Label(win, text="Name:", bg="#1b1b2f", fg="white").place(x=20, y=60)
    name_entry = tk.Entry(win); name_entry.place(x=120, y=60)

    tk.Label(win, text=f"Camera: {CAMERA_SOURCE}", bg="#1b1b2f", fg="white").place(x=20, y=100)

    tk.Button(win, text="Start Capture", command=lambda: threading.Thread(target=capture_student, args=(ROOT, win, enr_entry.get(), name_entry.get()), daemon=True).start(), width=20, bg="#2b2b45", fg="white").place(x=120, y=150)
    tk.Button(win, text="Close", command=win.destroy, width=20, bg="#a11", fg="white").place(x=350, y=150)

    win.mainloop()

def capture_student(ROOT, parent_win, enrollment, name):
    if not enrollment or not name:
        messagebox.showerror("Missing", "Enrollment and Name are required")
        return
    directory = f"{enrollment}_{name}"
    path = os.path.join(ROOT, "data", "TrainingImage", directory)
    if os.path.exists(path):
        messagebox.showerror("Exists", "Student folder already exists. Use Manage Students to update or delete.")
        return
    os.makedirs(path, exist_ok=True)

    cam_src = CAMERA_SOURCE
    try:
        cam = cv2.VideoCapture(int(cam_src)) if isinstance(cam_src, int) or str(cam_src).isdigit() else cv2.VideoCapture(cam_src)
    except:
        cam = cv2.VideoCapture(0)

    cascade_path = os.path.join(ROOT, "haarcascade_frontalface_default.xml")
    if not os.path.exists(cascade_path):
        messagebox.showerror("Missing Cascade", f"Place haarcascade_frontalface_default.xml in project root: {cascade_path}")
        return
    detector = cv2.CascadeClassifier(cascade_path)
    if detector.empty():
        messagebox.showerror("Invalid Cascade", "Cascade file couldn't be loaded. Re-download correct file.")
        return

    counts_per_angle = 8
    angles = ["center", "left", "right", "up", "down"]
    sample_count = 0

    try:
        for angle in angles:
            t_end = time.time() + 2
            while time.time() < t_end:
                ret, frame = cam.read()
                if not ret:
                    break
                cv2.imshow("Adjust pose - press q to cancel", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cam.release(); cv2.destroyAllWindows(); return
            captured = 0
            while captured < counts_per_angle:
                ret, frame = cam.read()
                if not ret:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    captured += 1
                    sample_count += 1
                    fname = f"{name}_{enrollment}_{angle}_{captured}.jpg"
                    cv2.imwrite(os.path.join(path, fname), gray[y:y+h, x:x+w])
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
                    cv2.putText(frame, f"{angle} {captured}/{counts_per_angle}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                cv2.imshow("Capturing - press q to cancel", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cam.release(); cv2.destroyAllWindows(); return
        cam.release()
        cv2.destroyAllWindows()
        # append to student details CSV
        csv_path = os.path.join(ROOT, "data", "StudentDetails", "studentdetails.csv")
        header = not os.path.exists(csv_path)
        with open(csv_path, "a", newline='', encoding='utf-8') as f:
            import csv as _csv
            writer = _csv.writer(f)
            if header:
                writer.writerow(["Enrollment", "Name"])
            writer.writerow([enrollment, name])
        messagebox.showinfo("Done", f"Captured images for {name}. Total images: {sample_count}")
    except Exception as e:
        try:
            cam.release()
            cv2.destroyAllWindows()
        except:
            pass
        messagebox.showerror("Error", str(e))
