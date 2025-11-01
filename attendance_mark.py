import os, cv2, pandas as pd, datetime, time
from tkinter import messagebox
from config import CAMERA_SOURCE, CAPTURE_DURATION_SECONDS, STUDENT_CSV, MODEL_FILE

def start_attendance(ROOT, subject):
    cam_source = CAMERA_SOURCE
    try:
        cam = cv2.VideoCapture(int(cam_source)) if isinstance(cam_source, int) or str(cam_source).isdigit() else cv2.VideoCapture(cam_source)
    except:
        cam = cv2.VideoCapture(0)

    model_path = os.path.join(ROOT, MODEL_FILE)
    if not os.path.exists(model_path):
        messagebox.showerror("Model missing", "Trained model not found. Please train first (Admin → Train Faces).")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(model_path)
    face_cascade = cv2.CascadeClassifier(os.path.join(ROOT, "haarcascade_frontalface_default.xml"))
    if face_cascade.empty():
        messagebox.showerror("Cascade", "Cascade file not loaded correctly.")
        return

    try:
        df = pd.read_csv(os.path.join(ROOT, STUDENT_CSV))
    except Exception:
        messagebox.showerror("Students missing", "No student details found. Register students first.")
        return

    attendance = pd.DataFrame(columns=["Enrollment","Name"])
    duration = CAPTURE_DURATION_SECONDS
    end = time.time() + duration
    while True:
        ret, img = cam.read()
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        for (x,y,w,h) in faces:
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf < 70:
                name = df.loc[df['Enrollment']==Id]['Name'].values
                if len(name)>0:
                    name = name[0]
                else:
                    name = str(Id)
                attendance.loc[len(attendance)] = [Id, name]
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(img, str(name), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            else:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
                cv2.putText(img, "Unknown", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
        cv2.imshow(f"Marking {subject} - Press q to cancel", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if time.time() > end:
            break

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d_%H-%M-%S")
    attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
    if attendance.empty:
        messagebox.showinfo("Attendance", "No faces recognized.")
    else:
        save_dir = os.path.join(ROOT, "data", "Attendance", subject)
        os.makedirs(save_dir, exist_ok=True)
        filename = os.path.join(save_dir, f"{subject}_{date}.xlsx")
        attendance[date] = 1
        attendance.to_excel(filename, index=False)
        messagebox.showinfo("Saved", f"Attendance saved to {filename}")
    cam.release()
    cv2.destroyAllWindows()
