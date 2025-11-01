import os, tkinter as tk, glob, pandas as pd
from tkinter import messagebox, simpledialog

def view_attendance(ROOT):
    root = tk.Tk(); root.withdraw()
    subject = simpledialog.askstring("Subject", "Enter subject name:")
    root.destroy()
    if not subject:
        return
    pattern_xlsx = os.path.join(ROOT, "data", "Attendance", subject, f"{subject}_*.xlsx")
    files = glob.glob(pattern_xlsx)
    if not files:
        messagebox.showinfo("No Data", "No attendance files found for this subject")
        return
    latest = sorted(files)[-1]
    try:
        df = pd.read_excel(latest)
    except Exception as e:
        messagebox.showerror("Error", str(e)); return
    win = tk.Tk(); win.title(f"Attendance - {subject}"); win.geometry("700x500")
    for r in range(min(200, df.shape[0])):
        for c in range(df.shape[1]):
            tk.Label(win, text=str(df.iat[r,c]), borderwidth=1, relief="solid", width=20).grid(row=r, column=c, padx=2, pady=2)
    win.mainloop()
