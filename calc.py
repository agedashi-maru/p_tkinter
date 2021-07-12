from tkinter import *
from tkinter import ttk


label_value = ""

root = Tk()
root.title("電卓")
# root.geometry("200x150")

# frame = ttk.Frame(root, padding="20 20 20 20")
frame = ttk.Frame(root)
frame.grid(column=0, row=0)

def push_bnt(event):
    global label_value
    label_value += str(event.widget["text"])
    label_str.set(label_value)


label_str = StringVar()

lb = ttk.Label(frame, textvariable=label_str)
lb["background"] = "gray"
lb["width"] = 38
lb.grid(column=1, row=1, columnspan=5)

text_num = 0
for i in [4, 3, 2]:
    for j in [1, 2, 3]:
        btn = ttk.Button(frame, text=j+text_num)
        btn.bind("<Button-1>", push_bnt)
        btn["width"] = 6
        btn.grid(column=j, row=i)
    
    text_num += 3

b1 = ttk.Button(frame, text="+")
b1["width"] = 6
b1.bind("<Button-1>", push_bnt)
b1.grid(column=4, row=2)
b2 = ttk.Button(frame, text="-")
b2["width"] = 6
b2.bind("<Button-1>", push_bnt)
b2.grid(column=5, row=2)
b3 = ttk.Button(frame, text="x")
b3["width"] = 6
b3.bind("<Button-1>", push_bnt)
b3.grid(column=4, row=3)
b4 = ttk.Button(frame, text="÷")
b4["width"] = 6
b4.bind("<Button-1>", push_bnt)
b4.grid(column=5, row=3)
b5 = ttk.Button(frame, text="=")
b5["width"] = 14
b5.bind("<Button-1>", push_bnt)
b5.grid(column=4, row=4, columnspan=2)

# for child in frame.winfo_children():
#     child.grid_configure(padx=1, pady=1)

root.mainloop()