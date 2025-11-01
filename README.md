# 🎯 Face Recognition Attendance System

A Python-based **Face Recognition Attendance System** that uses your **webcam** to automatically detect faces and mark attendance in an Excel/CSV file.  
It includes an **Admin Panel** for managing users and viewing attendance.

---

## 🧾 Overview

This system captures real-time images using a webcam, recognizes registered faces, and automatically logs attendance with timestamps.  
It’s ideal for schools, colleges, or offices to automate attendance without manual entry.

---

## 🚀 Features

✅ Real-time face detection and recognition using OpenCV & `face_recognition`  
✅ Attendance automatically marked in a CSV file  
✅ Prevents duplicate entries for the same session  
✅ Simple and user-friendly interface (Tkinter GUI)  
✅ Admin Panel for managing users and viewing logs  
✅ Clean modular code (easy to expand for CCTV later)

---

## 🧰 Tech Stack

- **Language:** Python 3.x  
- **Libraries Used:**
  - `opencv-python`
  - `face_recognition`
  - `numpy`
  - `pandas`
  - `datetime`
  - `tkinter`
- **Storage:** CSV (can be switched to Excel or database)
- **IDE Recommended:** VS Code / PyCharm

---

## 🏁 Quick Start (Go-to Guide)

Follow these simple steps to get started 👇

### 1️⃣ Clone this repository
```bash
git clone https://github.com/chiragjaju13/Attendance-System.git
cd Attendance-System
```

### 2️⃣ Install required dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add user images
Create a folder named `ImagesAttendance` (if not already there) and add clear images of each user:  
> Each image filename should match the person’s name.
```
ImagesAttendance/
├── Chirag.jpg
├── Jaju.png
```

### 4️⃣ Run the application
```bash
python main.py
```

### 5️⃣ Start Attendance
- The webcam will open automatically.  
- The system detects faces and logs attendance in `Attendance.csv`.  
- Each person is marked **only once per session**.

### 6️⃣ Admin Panel
Access the admin interface to:
- Add or remove users  
- View attendance records  
- Manage and export data

---

## 📂 Project Structure

```
Attendance-System/
│
├── main.py               # Main application (launch point)
├── admin_panel.py        # Admin module for management
├── face_recog.py         # Recognition logic
├── attendance.csv        # Attendance records (auto-created)
├── ImagesAttendance/     # Folder containing registered faces
├── requirements.txt      # Dependencies list
└── README.md             # Project documentation
```

---

## 📊 Attendance Output Format

| Name   | Time     | Date       | Status  |
|--------|----------|------------|----------|
| Chirag | 09:34:12 | XXXX-XX-XX | Present  |

---

## 🖼️ Screenshots (Optional)

> ![Main Interface](assets/main_ui.png)
> ![Admin Panel](assets/admin_panel.png)
> ![Attendance File](assets/attendance_csv.png)

*(Add actual screenshots later inside an `assets/` folder.)*

---

## 🧩 requirements.txt

If you haven’t created one, use this:
```
opencv-python
face_recognition
numpy
pandas
datetime
tkinter
```

*(Note: `tkinter` is included with Python by default on most systems.)*

---

## 🧠 Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|-----------|
| `ModuleNotFoundError` | Missing dependency | Run `pip install -r requirements.txt` |
| Camera not opening | Webcam in use / driver issue | Restart camera or close other apps |
| Faces not recognized | Poor lighting or unclear images | Use better lighting or clearer images |
| No `Attendance.csv` file | First-time run | It will auto-create after recognition |

---

## 🔮 Future Enhancements

- 📷 CCTV / NVR camera input  
- 🌐 Web-based dashboard for remote attendance viewing  
- 📧 Email reports for daily attendance  
- 🧑‍💼 Face re-registration and deletion from Admin Panel  
- 🧠 Deep-learning-based accuracy improvements

---

## 🤝 Contributing

Want to improve this project?  
1. Fork this repo  
2. Create a new branch (`feature-new`)  
3. Commit your changes  
4. Submit a Pull Request 🚀

---

## 📜 License

This project is licensed under the **MIT License** — free to use and modify.

---

## 👨‍💻 Author

**Chirag Jaju**  
📧 Email: chi18rag@gmail.com 

🔗 GitHub: [chiragjaju13](https://github.com/chiragjaju13)

⭐ *If you find this project helpful, please give it a star!*
