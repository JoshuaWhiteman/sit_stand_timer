import tkinter as tk
from win10toast import ToastNotifier

toaster = ToastNotifier()

def countdown(count):
    # change text in label
    mins, secs = divmod(count, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)        
    label['text'] = timeformat

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    else:
        label['text'] = 'SWITCH!'
        toaster.show_toast("SWITCH!", duration=10, threaded=True)

def reset():
    if label['text'] == 'SWITCH!':
        countdown(1800)
    

root = tk.Tk()

root.geometry("250x60") 

root.title("Sit/Stand Timer") 

label = tk.Label(root, font='Arial')
label.pack()

resetButton = tk.Button(root, text="RESET", font='Arial', bg='#2cd4f2', command=reset)
resetButton.pack()
  
countdown(1800)

root.mainloop()