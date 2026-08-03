import tkinter as tk
from tkinter import messagebox
import threading

from clinical.runner import run_clinical
from dme.runner import run_dme
from anesthesia.runner import run_anesthesia


def start_clinical():
    threading.Thread(target=run_clinical).start()


def start_dme():
    threading.Thread(target=run_dme).start()


def start_anesthesia():
    threading.Thread(target=run_anesthesia).start()


def create_ui():

    root = tk.Tk()
    root.title("Healthcare Automation System")
    root.geometry("550x400")
    root.resizable(False, False)

    title = tk.Label(
        root,
        text="Healthcare Automation System",
        font=("Arial", 18, "bold")
    )
    title.pack(pady=20)

    clinical_btn = tk.Button(
        root,
        text="Clinical + Physician Automation",
        width=35,
        height=2,
        command=start_clinical
    )
    clinical_btn.pack(pady=10)

    dme_btn = tk.Button(
        root,
        text="DME Automation",
        width=35,
        height=2,
        command=start_dme
    )
    dme_btn.pack(pady=10)

    anesthesia_btn = tk.Button(
        root,
        text="Anesthesia Automation",
        width=35,
        height=2,
        command=start_anesthesia
    )
    anesthesia_btn.pack(pady=10)

    exit_btn = tk.Button(
        root,
        text="Exit",
        width=20,
        command=root.destroy
    )
    exit_btn.pack(pady=30)

    root.mainloop()