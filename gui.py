import tkinter as tk
import sys
sys.dont_write_bytecode = True

def gui():
    window = tk.Tk()
    tk.Entry(window, width=50).grid(row=0, column=0)
    button = tk.Button(window, text="1").grid(row=0, column=1)
    
    window.mainloop()

if __name__=='__main__':
    gui()