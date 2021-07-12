import tkinter as tk


root = tk.Tk()
root.title("Entry")
root.geometry("200x150")


def button_ok():
    value = edBox.get()
    label_str.set(value)
    
label_str = tk.StringVar()

lb = tk.Label(root, text="", textvariable=label_str)
lb.pack()

edBox = tk.Entry(width=25)
edBox.pack()

btn_ok = tk.Button(text="OK", command=button_ok)
btn_ok.pack()


root.mainloop()