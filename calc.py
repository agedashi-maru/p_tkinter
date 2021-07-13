from tkinter import *
from tkinter import ttk


# 画面に表示する値
label_value = ""
# 計算用のリスト
calc_list = []

def push_number_bnt(event):
    """
    数字ボタン用の処理
    """
    global label_value
    
    # 追記して再表示
    label_value += str(event.widget["text"])
    label_str.set(label_value)


def push_operator_btn(event):
    """
    「+ - x ÷」ボタン用の処理
    """
    global label_value
    global calc_list

    if len(calc_list) == 0:
        if label_value == "":
            return
        
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
    """
    「=」ボタン用の処理
    """
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
        # label_value = str(label_value)
        label_value = ""


def push_clear_bnt(event):
    """
    「c」ボタン用の処理
    """
    global label_value
    global calc_list

    label_value = ""
    calc_list = []
    label_str.set(label_value)


if __name__ == "__main__":
    root = Tk()
    root.title("電卓")

    frame = ttk.Frame(root, padding="20 20 20 20")
    frame.grid(column=0, row=0)

    label_str = StringVar()
    
    # 入力内容の表示領域を定義
    lb = ttk.Label(frame, textvariable=label_str)
    lb["width"] = 38
    lb.grid(column=1, row=1, columnspan=5)
    
    # 数字ボタンを定義
    text_num = 0
    for i in [4, 3, 2]:
        for j in [1, 2, 3]:
            btn = ttk.Button(frame, text=j+text_num)
            btn.bind("<Button-1>", push_number_bnt)
            btn.grid(column=j, row=i)
        
        text_num += 3
    
    # 演算子などの記号ボタンを定義
    b1 = ttk.Button(frame, text="+")
    b1.bind("<Button-1>", push_operator_btn)
    b1.grid(column=4, row=2)
    b2 = ttk.Button(frame, text="-")
    b2.bind("<Button-1>", push_operator_btn)
    b2.grid(column=5, row=2)
    b3 = ttk.Button(frame, text="x")
    b3.bind("<Button-1>", push_operator_btn)
    b3.grid(column=4, row=3)
    b4 = ttk.Button(frame, text="÷")
    b4.bind("<Button-1>", push_operator_btn)
    b4.grid(column=5, row=3)
    b5 = ttk.Button(frame, text="=")
    b5.bind("<Button-1>", push_equal_bnt)
    b5.grid(column=4, row=4)
    b6 = ttk.Button(frame, text="c")
    b6.bind("<Button-1>", push_clear_bnt)
    b6.grid(column=5, row=4)

    # ボタンの大きさを揃える
    for child in frame.winfo_children():
        if not child.__class__.__name__ == "Label":
            child["width"] = 6

    root.mainloop()