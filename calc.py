from tkinter import *
from tkinter import ttk


calc_str = ""

def push_number_bnt(event):
    """
    数字ボタン用の処理
    """
    global calc_str
    
    calc_str += event.widget["text"]
    label_str.set(event.widget["text"])
    


def push_operator_btn(event):
    """
    「+ - x ÷」ボタン用の処理
    """
    global calc_str
    
    text = event.widget["text"]

    if text == "+":
        calc_str += "+"
    elif text == "-":
        calc_str += "-"
    elif text == "x":
        calc_str += "*"
    elif text == "÷":
        calc_str += "/"

    label_str.set(event.widget["text"])


def push_equal_bnt(event):
    """
    「=」ボタン用の処理
    """
    global calc_str

    equal_str = eval(calc_str)
    label_str.set(equal_str)


def push_clear_bnt(event):
    """
    「c」ボタン用の処理
    """
    global calc_str
    
    calc_str = ""
    label_str.set("0")


if __name__ == "__main__":
    root = Tk()
    root.title("電卓")

    frame = ttk.Frame(root, padding="20 20 20 20")
    frame.grid(column=0, row=0)

    label_str = StringVar()
    label_str.set("0")
    
    # 入力内容の表示領域を定義
    lb = ttk.Label(frame, textvariable=label_str)
    lb["width"] = 38
    lb.grid(column=1, row=1, columnspan=5)
    
    # 数字ボタンを定義
    text_num = 0
    for i in [4, 3, 2]:
        for j in [1, 2, 3]:
            btn = ttk.Button(frame, text=str(j+text_num))
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