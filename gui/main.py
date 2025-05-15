import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import threading

def run_clips(symptoms):
    # تأكد من وجود المجلد
    os.makedirs("clips_engine", exist_ok=True)

    # حفظ الأعراض في ملف
    with open("clips_engine/input.clp", "w") as f:
        for s in symptoms:
            f.write(f"(symptom {s})\n")

    # تشغيل CLIPS داخل الكونتينر
    result = subprocess.run([
        "docker", "run", "--rm",
        "-v", f"{os.getcwd()}/clips_engine:/engine",
        "clips-engine",
        "/engine/clips",
        "-f", "/engine/diagnosis.clp"
    ], capture_output=True, text=True)

    return result.stdout

def diagnose():
    selected = [s for s, var in zip(symptom_list, vars) if var.get()]
    if not selected:
        messagebox.showwarning("No Input", "Please select at least one symptom.")
        return

    def run_in_thread():
        output = run_clips(selected)
        messagebox.showinfo("Diagnosis Result", output)

    threading.Thread(target=run_in_thread).start()

# واجهة المستخدم (GUI)
root = tk.Tk()
root.title("Disease Diagnosis Expert System")

symptom_list = ["fever", "cough", "fatigue"]
vars = [tk.BooleanVar() for _ in symptom_list]

for i, s in enumerate(symptom_list):
    tk.Checkbutton(root, text=s, variable=vars[i]).pack(anchor="w")

tk.Button(root, text="Diagnose", command=diagnose).pack(pady=10)

root.mainloop()
