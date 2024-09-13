import tkinter as tk
from tkinter import *
import time

def count():
    timer = int(entry1.get())
    
  
    
    while timer > 0:
        m, s = divmod(timer, 60)
        h, m = divmod(m, 60)
        timer_format = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
        label2.config(text=timer_format)
        root.update()
        time.sleep(1)
        timer -= 1
        
    label3.config(text='Time Out!')
    

root = tk.Tk()
root.title('Counting Seconds')


label1 = Label(root , text='Enter the number of seconds' , width=50)
label1.pack(pady=25)

entry1 = tk.Entry(root)
entry1.pack(pady=25)


label2 = tk.Label(root , text ='00:00:00')
label2.pack(pady=25)

label3 = tk.Label(root)
label3.pack(pady=25)

btn = tk.Button(root, text="Start" , command=count)
btn.pack(pady=25)

root.mainloop()