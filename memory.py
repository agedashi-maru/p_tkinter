import tkinter as tk
import random
import time


selected_card = {}

def push_button(event):
    global selected_card
    try:
        text_num = int(event.widget["text"])
    except ValueError as e:
        pass
    else:
        sv_list[text_num-1].set(pattern_list[text_num-1])
        time.sleep(0.5)
        if len(selected_card) == 0:
            selected_card[text_num] = pattern_list[text_num-1]
        else:
            for key, value in selected_card.items():
                pass
            
            if value == pattern_list[text_num-1]:
                pass
            else:
                sv_list[text_num-1].set(text_num)
                sv_list[int(key)-1].set(str(key))
                
            selected_card = {}


if __name__ == "__main__":
    root = tk.Tk()
    root.title("神経衰弱")
    
    pattern_list = ["◎", "◎", "△", "△", "☆", "☆"]
    random.shuffle(pattern_list)
    
    sv_list = []
    
    mainFrame = tk.Frame(root, padx=10, pady=10)
    mainFrame.grid(row=0, column=0)
    
    count = 1
    for i in range(2):
        for j in range(3):
            sv = tk.StringVar()
            sv.set(str(count))
            sv_list.append(sv)
            card = tk.Button(mainFrame, textvariable=sv)
            card.bind("<Button-1>", push_button)
            card["width"] = 5
            card["height"] = 4
            card.grid(row=i+1, column=j+1)
            count += 1
    
    root.mainloop()