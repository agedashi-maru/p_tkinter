import tkinter as tk
import random
import time
import datetime
import sys


class MemoryGame(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master=master)
        
        # 選択されたカードを保持するdict
        self.selected_card = []
        # カードの絵柄パターン
        self.pattern_list = ["◎", "△", "☆", "◇", "□", "@", "#", "$", "&", "〇", "▽", "●", "▼", "▲", "★", "■"]
        # 表示カードの絵柄リスト
        self.card_pattern_list = []
        # 各カードに割り当てるStringVarを管理するリスト
        self.sv_list = []
        # タイマー用変数
        self.t = datetime.datetime.strptime("00:00", "%M:%S")
        # カードが配置される行数
        self.ROW=2
        # カードが配置される列数
        self.COLUMN=3
        
        self.create_widgets(master)
    
    
    def create_widgets(self, master):
        mainFrame = tk.Frame(master, padx=10)
        mainFrame.grid(row=0, column=0)
        
        # リトライ用のボタンを定義する
        self.retry_label = tk.StringVar()
        self.retry_label.set("リトライ")
        tk.Button(mainFrame, textvariable=self.retry_label, font=('FixedSys',14,'bold'), padx=15, command=self.retry_button).grid(row=1, column=1, columnspan=self.COLUMN+1)
        
        # カード用のボタンを定義する
        count = 1
        for i in range(self.ROW):
            for j in range(self.COLUMN):
                sv = tk.StringVar()
                sv.set(str(count))
                self.sv_list.append(sv)
                card = tk.Button(mainFrame, textvariable=sv)
                card.bind("<Button-1>", self.push_card_button)
                card["width"] = 5
                card["height"] = 4
                card.grid(row=i+2, column=j+2)
                count += 1
        
        # タイマー用のラベルを定義する
        self.buff = tk.StringVar()
        self.buff.set("")
        tk.Label(mainFrame, textvariable=self.buff, font=('FixedSys',14,'bold'), pady=8).grid(row=self.ROW+2, column=1, columnspan=self.COLUMN+1)
        
        
    def push_card_button(self, event):
        """
        カードのボタンを押したときの処理
        """
        
        try:
            text_num = int(event.widget["text"])
        except ValueError as e:
            # 絵柄が押されたときは何もしない
            pass
        else:
            # 数字から絵柄に変更する
            self.sv_list[text_num-1].set(self.card_pattern_list[text_num-1])
            time.sleep(0.3)
            
            if len(self.selected_card) % 2 == 0 :
                self.selected_card.append((text_num, self.card_pattern_list[text_num-1]))
                
            else:
                # 前回のカードと比較する
                if self.selected_card[-1][1] == self.card_pattern_list[text_num-1]:
                    self.selected_card.append((text_num, self.card_pattern_list[text_num-1]))
                else:
                    self.sv_list[text_num-1].set(text_num)
                    self.sv_list[self.selected_card[-1][0]-1].set(str(self.selected_card[-1][0]))
                    del self.selected_card[-1]

    def create_pattern_list(self):
        """
        カードの絵柄を、指定された行列分作成する
        """
        
        self.card_pattern_list = []
        self.selected_card = []
        num = int(self.COLUMN * self.ROW / 2)
        random.shuffle(self.pattern_list)
        for i in range(num):
            pattern = self.pattern_list[i]
            self.card_pattern_list.append(pattern+str(i+1))
            self.card_pattern_list.append(pattern+str(i+1))
        
        random.shuffle(self.card_pattern_list)
        
        
    def count_time(self):
        """
        タイマーの処理
        """
        
        self.buff.set(self.t.strftime("%M:%S"))
        self.t = self.t + datetime.timedelta(seconds=1)
        if self.ROW*self.COLUMN != len(self.selected_card):
            root.after(1000, self.count_time)


    def retry_button(self):
        """
        リトライボタンを押したときの処理
        """
        
        # 各パラメータを初期化する
        for i, sv in enumerate(self.sv_list):
            sv.set(i+1)
        
        self.t = datetime.datetime.strptime("00:00", "%M:%S")
        self.create_pattern_list()
        self.count_time()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("神経衰弱")
    
    memory_game = MemoryGame(root)
    
    # カードのパターンを作成
    memory_game.create_pattern_list()
    # タイマー開始
    memory_game.count_time()
    
    memory_game.mainloop()