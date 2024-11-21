import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('Calculator')
window.geometry('300x400')
window.configure(bg='white')
window.resizable(False, False)

frame = tk.Frame(master=window, bg="white")
frame.pack(pady=20)

entry = tk.Entry(master=frame, font=('Arial', 20), borderwidth=2, relief='solid', width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10)

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        tkinter.messagebox.showinfo("Error", "Invalid Input")

def clear():
    entry.delete(0, tk.END)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(master=frame, text=text, padx=25, pady=20, command=clear, font=('Arial', 18), relief='flat', bg='#f0f0f0')
    elif text == '=':
        button = tk.Button(master=frame, text=text, padx=25, pady=20, command=equal, font=('Arial', 18), relief='flat', bg='#4CAF50', fg='white')
    else:
        button = tk.Button(master=frame, text=text, padx=25, pady=20, command=lambda num=text: myclick(num), font=('Arial', 18), relief='flat', bg='#f0f0f0')
    button.grid(row=row, column=col, sticky='nsew', pady=5)

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

window.mainloop()
