import tkinter as tk
import sys
sys.dont_write_bytecode = True

def gui():
    window = tk.Tk()
    entery = tk.Entry(window, font=("Arial", 8), width=38, justify= "right").grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)
    
    window.geometry("250x350")
    window.title("CALCULATOR")
    window.config(background="black")

    tk.Button(window, text="AC",font=("Arial", 20), width=3, height=1).grid(row=1, column=0, padx=1, pady=1)
    tk.Button(window, text="c",font=("Arial", 20), width=3, height=1).grid(row=1, column=1, padx=1, pady=1)
    tk.Button(window, text="%",font=("Arial", 20), width=3, height=1).grid(row=1, column=2, padx=1, pady=1)
    tk.Button(window, text="/",font=("Arial", 20), width=3, height=1).grid(row=1, column=3, padx=1, pady=1)

    tk.Button(window, text="1",font=("Arial", 20), width=3, height=1).grid(row=2, column=0, padx=1, pady=1)
    tk.Button(window, text="2",font=("Arial", 20), width=3, height=1).grid(row=2, column=1, padx=1, pady=1)
    tk.Button(window, text="3",font=("Arial", 20), width=3, height=1).grid(row=2, column=2, padx=1, pady=1)
    tk.Button(window, text="*",font=("Arial", 20), width=3, height=1).grid(row=2, column=3, padx=1, pady=1)

    tk.Button(window, text="4",font=("Arial", 20), width=3, height=1).grid(row=3, column=0, padx=1, pady=1)
    tk.Button(window, text="5",font=("Arial", 20), width=3, height=1).grid(row=3, column=1, padx=1, pady=1)
    tk.Button(window, text="6",font=("Arial", 20), width=3, height=1).grid(row=3, column=2, padx=1, pady=1)
    tk.Button(window, text="-",font=("Arial", 20), width=3, height=1).grid(row=3, column=3, padx=1, pady=1)

    tk.Button(window, text="7",font=("Arial", 20), width=3, height=1).grid(row=4, column=0, padx=1, pady=1)
    tk.Button(window, text="8",font=("Arial", 20), width=3, height=1).grid(row=4, column=1, padx=1, pady=1)
    tk.Button(window, text="9",font=("Arial", 20), width=3, height=1).grid(row=4, column=2, padx=1, pady=1)
    tk.Button(window, text="+",font=("Arial", 20), width=3, height=1).grid(row=4, column=3, padx=1, pady=1)

    tk.Button(window, text="0",font=("Arial", 20), width=3, height=1).grid(row=5, column=0, padx=1, pady=1)
    tk.Button(window, text="00",font=("Arial", 20), width=3, height=1).grid(row=5, column=1, padx=1, pady=1)
    tk.Button(window, text=".",font=("Arial", 20), width=3, height=1).grid(row=5, column=2, padx=1, pady=1)
    tk.Button(window, text="=",font=("Arial", 20), width=3, height=1).grid(row=5, column=3, padx=1, pady=1)


    
    window.mainloop()

if __name__=='__main__':
    gui()