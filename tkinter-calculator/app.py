from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x400")

display = Entry(window, width=20, font=("Arial", 16), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(value):
    display.insert(END, value)

def clear():
    display.delete(0, END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, str(result))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

row = 1
col = 0

for b in buttons:
    if b == "C":
        Button(
            window,
            text=b,
            width=7,
            height=2,
            font=("Arial", 12),
            command=clear
        ).grid(row=row, column=col, padx=5, pady=5)

    elif b == "=":
        Button(
            window,
            text=b,
            width=7,
            height=2,
            font=("Arial", 12),
            command=calculate
        ).grid(row=row, column=col, padx=5, pady=5)

    else:
        Button(
            window,
            text=b,
            width=7,
            height=2,
            font=("Arial", 12),
            command=lambda x=b: click(x)
        ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()