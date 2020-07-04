import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, Text
import os

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

root = tk.Tk()

root.title("Sit Stand Timer")

root.resizable(0,0)

canvas = tk.Canvas(root, height=200, width=400, bg="#34bccf")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

resetTimer = tk.Button(root, text="Reset", padx=10, pady=5, fg="white", bg="#34bccf")
resetTimer.pack()

root.mainloop()