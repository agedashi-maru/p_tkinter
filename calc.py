from tkinter import *
from tkinter import ttk


label_value = ""
calc_list = []

def push_number_bnt(event):
    global label_value
    label_value += str(event.widget["text"])
    label_str.set(label_value)


def push_operator_btn(event):
    global label_value
    global calc_list

    if label_value == "":
        pass

    elif len(calc_list) == 0:
        calc_list.append(int(label_value))
        calc_list.append(event.widget["text"])
        label_value = ""
        label_str.set(event.widget["text"])

    elif len(calc_list) == 1:
        calc_list.append(event.widget["text"])
        label_str.set(event.widget["text"])
        label_value = ""

    elif len(calc_list) == 2:
        if calc_list[1] == "+":
            label_value = calc_list[0] + int(label_value)
        elif calc_list[1] == "-":
            label_value = calc_list[0] - int(label_value)
        elif calc_list[1] == "x":
            label_value = calc_list[0] * int(label_value)
        elif calc_list[1] == "÷":
            label_value = calc_list[0] / int(label_value)

        label_str.set(label_value)
        calc_list = []
        calc_list.append(label_value)
        calc_list.append(event.widget["text"])
        label_value=""


def push_equal_bnt(event):
    global label_value
    global calc_list

    if len(calc_list) <= 1:
        label_str.set(label_value)
    else:
        if calc_list[1] == "+":
            label_value = calc_list[0] + int(label_value)
        elif calc_list[1] == "-":
            label_value = calc_list[0] - int(label_value)
        elif calc_list[1] == "x":
            label_value = calc_list[0] * int(label_value)
        elif calc_list[1] == "÷":
            label_value = calc_list[0] / int(label_value)

        label_str.set(label_value)
        calc_list = []
        calc_list.append(label_value)
        label_value = str(label_value)


def push_clear_bnt(event):
    global label_value
    global calc_list

    label_value = ""
    calc_list = []
    label_str.set(label_value)

root = Tk()
root.title("電卓")
# root.geometry("200x150")

frame = ttk.Frame(root, padding="20 20 20 20")
frame.grid(column=0, row=0)

label_str = StringVar()

lb = ttk.Label(frame, textvariable=label_str)
# lb["background"] = "gray"
lb["width"] = 38
lb.grid(column=1, row=1, columnspan=5)

text_num = 0
for i in [4, 3, 2]:
    for j in [1, 2, 3]:
        btn = ttk.Button(frame, text=j+text_num)
        btn.bind("<Button-1>", push_number_bnt)
        btn["width"] = 6
        btn.grid(column=j, row=i)
    
    text_num += 3

b1 = ttk.Button(frame, text="+")
b1["width"] = 6
b1.bind("<Button-1>", push_operator_btn)
b1.grid(column=4, row=2)
b2 = ttk.Button(frame, text="-")
b2["width"] = 6
b2.bind("<Button-1>", push_operator_btn)
b2.grid(column=5, row=2)
b3 = ttk.Button(frame, text="x")
b3["width"] = 6
b3.bind("<Button-1>", push_operator_btn)
b3.grid(column=4, row=3)
b4 = ttk.Button(frame, text="÷")
b4["width"] = 6
b4.bind("<Button-1>", push_operator_btn)
b4.grid(column=5, row=3)
b5 = ttk.Button(frame, text="=")
b5["width"] = 6
b5.bind("<Button-1>", push_equal_bnt)
b5.grid(column=4, row=4)
b6 = ttk.Button(frame, text="c")
b6["width"] = 6
b6.bind("<Button-1>", push_clear_bnt)
b6.grid(column=5, row=4)

# for child in frame.winfo_children():
#     child.grid_configure(padx=1, pady=1)

root.mainloop()