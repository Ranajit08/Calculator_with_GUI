from calculator import Calc
import tkinter as tk


def gui():
    window = tk.Tk()
    entry = tk.Entry(
        window, font=("Arial", 20), width=15, justify="right", bd=2, relief="solid"
    )
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=1)

    def click_1():
        entry.insert("end", "1")

    def click_2():
        entry.insert("end", "2")

    def click_3():
        entry.insert("end", "3")

    def click_4():
        entry.insert("end", "4")

    def click_5():
        entry.insert("end", "5")

    def click_6():
        entry.insert("end", "6")

    def click_7():
        entry.insert("end", "7")

    def click_8():
        entry.insert("end", "8")

    def click_9():
        entry.insert("end", "9")

    def click_0():
        entry.insert("end", "0")

    def click_00():
        entry.insert("end", "00")

    def click_plus():
        entry.insert("end", "+")

    def click_minus():
        entry.insert("end", "-")

    def click_multiplication():
        entry.insert("end", "*")

    def click_division():
        entry.insert("end", "/")

    def click_percentage():
        entry.insert("end", "%")

    def click_backspace():
        current = entry.get()
        entry.delete(0, "end")
        entry.insert(0, current[:-1])

    def click_all_clear():
        entry.delete(0, "end")

    def click_dot():
        entry.insert("end", ".")

    def click_result():
        string = entry.get()
        re = Calc(string)
        entry.delete(0, "end")
        total = re.result()
        entry.insert("end", total)

    window.geometry("250x350")
    window.title("CALCULATOR")
    window.config(background="black")

    tk.Button(
        window,
        text="AC",
        font=("Arial", 20),
        width=3,
        height=1,
        background="black",
        activebackground="black",
        fg="white",
        activeforeground="white",
        command=click_all_clear,
    ).grid(row=1, column=0, padx=1, pady=1)
    tk.Button(
        window,
        text="⌫",
        font=("Arial", 20),
        width=3,
        height=1,
        background="black",
        activebackground="black",
        fg="white",
        activeforeground="white",
        command=click_backspace,
    ).grid(row=1, column=1, padx=1, pady=1)
    tk.Button(
        window,
        text="%",
        font=("Arial", 20),
        width=3,
        height=1,
        background="black",
        activebackground="black",
        fg="white",
        activeforeground="white",
        command=click_percentage,
    ).grid(row=1, column=2, padx=1, pady=1)
    tk.Button(
        window,
        text="/",
        font=("Arial", 20),
        width=3,
        height=1,
        background="black",
        activebackground="black",
        fg="white",
        activeforeground="white",
        command=click_division,
    ).grid(row=1, column=3, padx=1, pady=1)

    tk.Button(
        window, text="1", font=("Arial", 20), width=3, height=1, command=click_1
    ).grid(row=2, column=0, padx=1, pady=1)
    tk.Button(
        window, text="2", font=("Arial", 20), width=3, height=1, command=click_2
    ).grid(row=2, column=1, padx=1, pady=1)
    tk.Button(
        window, text="3", font=("Arial", 20), width=3, height=1, command=click_3
    ).grid(row=2, column=2, padx=1, pady=1)
    tk.Button(
        window,
        text="*",
        font=("Arial", 20),
        width=3,
        height=1,
        background="black",
        activebackground="black",
        fg="white",
        activeforeground="white",
        command=click_multiplication,
    ).grid(row=2, column=3, padx=1, pady=1)

    tk.Button(
        window, text="4", font=("Arial", 20), width=3, height=1, command=click_4
    ).grid(row=3, column=0, padx=1, pady=1)
    tk.Button(
        window, text="5", font=("Arial", 20), width=3, height=1, command=click_5
    ).grid(row=3, column=1, padx=1, pady=1)
    tk.Button(
        window, text="6", font=("Arial", 20), width=3, height=1, command=click_6
    ).grid(row=3, column=2, padx=1, pady=1)
    tk.Button(
        window,
        text="-",
        font=("Arial", 20),
        width=3,
        height=1,
        background="black",
        activebackground="black",
        fg="white",
        activeforeground="white",
        command=click_minus,
    ).grid(row=3, column=3, padx=1, pady=1)

    tk.Button(
        window, text="7", font=("Arial", 20), width=3, height=1, command=click_7
    ).grid(row=4, column=0, padx=1, pady=1)
    tk.Button(
        window, text="8", font=("Arial", 20), width=3, height=1, command=click_8
    ).grid(row=4, column=1, padx=1, pady=1)
    tk.Button(
        window, text="9", font=("Arial", 20), width=3, height=1, command=click_9
    ).grid(row=4, column=2, padx=1, pady=1)
    tk.Button(
        window,
        text="+",
        font=("Arial", 20),
        width=3,
        height=1,
        background="black",
        activebackground="black",
        fg="white",
        activeforeground="white",
        command=click_plus,
    ).grid(row=4, column=3, padx=1, pady=1)

    tk.Button(
        window, text="0", font=("Arial", 20), width=3, height=1, command=click_0
    ).grid(row=5, column=0, padx=1, pady=1)
    tk.Button(
        window, text="00", font=("Arial", 20), width=3, height=1, command=click_00
    ).grid(row=5, column=1, padx=1, pady=1)
    tk.Button(
        window, text=".", font=("Arial", 20), width=3, height=1, command=click_dot
    ).grid(row=5, column=2, padx=1, pady=1)
    tk.Button(
        window,
        text="=",
        font=("Arial", 20),
        width=3,
        height=1,
        background="orange",
        activebackground="orange",
        fg="white",
        activeforeground="white",
        command=click_result,
    ).grid(row=5, column=3, padx=1, pady=1)

    window.mainloop()


if __name__ == "__main__":
    gui()
