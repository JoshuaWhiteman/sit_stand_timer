import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, Text
import os

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

root = tk.Tk()

canvas = tk.Canvas(root, height=200, width=400, bg="#34bccf")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8)

root.mainloop()