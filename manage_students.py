import os, pandas as pd, tkinter as tk
from tkinter import messagebox, simpledialog
import shutil, glob

def ensure_dirs(ROOT):
    os.makedirs(os.path.join(ROOT, "data", "StudentDetails"), exist_ok=True)

def manage_students(ROOT):
    ensure_dirs(ROOT)
    csv_path = os.path.join(ROOT, "data", "StudentDetails", "studentdetails.csv")
    if not os.path.exists(csv_path):
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write("Enrollment,Name\n")

    df = pd.read_csv(csv_path)
    win = tk.Tk(); win.title("Manage Students"); win.geometry("900x500")
    frame = tk.Frame(win); frame.pack(fill='both', expand=True)

    import tkinter.ttk as ttk
    tree = ttk.Treeview(frame, columns=("Enrollment","Name"), show='headings')
    tree.heading("Enrollment", text="Enrollment"); tree.heading("Name", text="Name")
    tree.pack(fill='both', expand=True)
    for _, row in df.iterrows():
        tree.insert('', 'end', values=(row['Enrollment'], row['Name']))

    def delete_student():
        sel = tree.selection()
        if not sel:
            messagebox.showerror("Select", "Select a student row to delete")
            return
        vals = tree.item(sel, 'values')
        enr = vals[0]
        matches = glob.glob(os.path.join(ROOT, "data", "TrainingImage", f"{enr}_*"))
        for m in matches:
            shutil.rmtree(m, ignore_errors=True)
        df2 = pd.read_csv(csv_path)
        try:
            df2 = df2[df2['Enrollment'] != int(enr)]
        except Exception:
            df2 = df2[df2['Enrollment'] != enr]
        df2.to_csv(csv_path, index=False)
        for i in sel:
            tree.delete(i)
        messagebox.showinfo("Deleted", f"Deleted student {enr}")

    def reregister():
        sel = tree.selection()
        if not sel:
            messagebox.showerror("Select", "Select a student to re-register")
            return
        vals = tree.item(sel, 'values')
        enr, name = vals
        matches = glob.glob(os.path.join(ROOT, "data", "TrainingImage", f"{enr}_*"))
        for m in matches:
            shutil.rmtree(m, ignore_errors=True)
        import student_capture
        student_capture.open_capture_window(ROOT)

    btn_frame = tk.Frame(win); btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="Delete Selected", command=delete_student).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Re-register Selected", command=reregister).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Close", command=win.destroy).grid(row=0, column=2, padx=5)
    win.mainloop()
