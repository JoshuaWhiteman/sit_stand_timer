import tkinter as tk


window = tk.Tk()
window.title("Testing")

frame_a = tk.Frame()
frame_a.pack()

label = tk.Label(master=frame_a, text="testing frame_a")
label.pack()

window.mainloop()