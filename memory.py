import tkinter as tk
import random
import time
import datetime
import sys


# 選択されたカードを保持するdict
selected_card = []
# カードの絵柄パターン
pattern_list = ["◎", "△", "☆", "◇", "□", "@", "#", "$", "&", "〇", "▽", "●", "▼", "▲", "★", "■"]
card_pattern_list = []
# 各カードに割り当てるStringVarを管理するリスト
sv_list = []
# タイマー用変数
t = datetime.datetime.strptime("00:00", "%M:%S")
# カードが配置される行数
ROW=2
# カードが配置される列数
COLUMN=3


def push_card_button(event):
    """
    カードのボタンを押したときの処理
    """
    global selected_card
    global card_pattern_list
    global sv_list
    try:
        text_num = int(event.widget["text"])
    except ValueError as e:
        # 絵柄が押されたときは何もしない
        pass
    else:
        # 数字から絵柄に変更する
        sv_list[text_num-1].set(card_pattern_list[text_num-1])
        time.sleep(0.3)
        
        if len(selected_card) % 2 == 0 :
            selected_card.append((text_num, card_pattern_list[text_num-1]))
            
        else:
            # 前回のカードと比較する
            if selected_card[-1][1] == card_pattern_list[text_num-1]:
                selected_card.append((text_num, card_pattern_list[text_num-1]))
            else:
                sv_list[text_num-1].set(text_num)
                sv_list[selected_card[-1][0]-1].set(str(selected_card[-1][0]))
                del selected_card[-1]

def create_pattern_list():
    """
    カードの絵柄を、指定された行列分作成する
    """
    global ROW
    global COLUMN
    global pattern_list
    global card_pattern_list
    
    card_pattern_list = []
    num = int(COLUMN * ROW / 2)
    random.shuffle(pattern_list)
    for i in range(num):
        pattern = pattern_list[i]
        card_pattern_list.append(pattern+str(i+1))
        card_pattern_list.append(pattern+str(i+1))
    
    random.shuffle(card_pattern_list)
    
def count_time():
    """
    タイマーの処理
    """
    global t
    global ROW
    global COLUMN
    
    buff.set(t.strftime("%M:%S"))
    t = t + datetime.timedelta(seconds=1)
    if ROW*COLUMN != len(selected_card):
        root.after(1000, count_time)


def retry_button():
    """
    リトライボタンを押したときの処理
    """
    global selected_card
    global t
    
    # 各パラメータを初期化する
    for i, sv in enumerate(sv_list):
        sv.set(i+1)
    
    t = datetime.datetime.strptime("00:00", "%M:%S")
    count_time()
    create_pattern_list()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("神経衰弱")
    
    # パターンをランダムにする
    random.shuffle(pattern_list)

    mainFrame = tk.Frame(root, padx=10)
    mainFrame.grid(row=0, column=0)
    
    # リトライ用のボタンを定義する
    retry_label = tk.StringVar()
    retry_label.set("リトライ")
    tk.Button(mainFrame, textvariable=retry_label, font=('FixedSys',14,'bold'), padx=15, command=retry_button).grid(row=1, column=1, columnspan=COLUMN+1)
    
    # カード用のボタンを定義する
    count = 1
    for i in range(ROW):
        for j in range(COLUMN):
            sv = tk.StringVar()
            sv.set(str(count))
            sv_list.append(sv)
            card = tk.Button(mainFrame, textvariable=sv)
            card.bind("<Button-1>", push_card_button)
            card["width"] = 5
            card["height"] = 4
            card.grid(row=i+2, column=j+2)
            count += 1
    
    # タイマー用のラベルを定義する
    buff = tk.StringVar()
    buff.set("")
    tk.Label(mainFrame, textvariable=buff, font=('FixedSys',14,'bold'), pady=8).grid(row=ROW+2, column=1, columnspan=COLUMN+1)
    
    # カードのパターンを作成
    create_pattern_list()
    # タイマー開始
    count_time()
    
    root.mainloop()