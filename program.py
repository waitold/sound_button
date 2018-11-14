import tkinter as tk 
import itertools
import os,tkinter.filedialog, tkinter.messagebox

def callback(event,i,j):#サウンド再生
    print(event.widget["text"])

def set_sound(event,i,j):#ボタンの名前設定
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tk.messagebox.showinfo('sound button','処理ファイルを選択してください！')
    file = tk.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

    tkinter.messagebox.showinfo('sound button',file)
    filepath =""
    for i in file:
        filepath += i
    filename = os.path.basename(filepath)
    print(filepath)
    print(filename)

    entry_frame = tk.Frame(root)
    entry_frame.place(x = 10, y =400)
    entry_text = tk.Label(entry_frame,text = "ファイル名")
    entry_text.pack()
    sound_name = tk.Entry(entry_frame,width = 60)
    sound_name.pack()
    sound_name.insert(tk.END,filename)
    entry_button = tk.Button(entry_frame,text = "完了",width = 3,height =1)
    entry_button.pack()


root = tk.Tk()
root.title("sound button")
root.geometry("400x600")
    

button = [[],[],[],[]]
count = 1

for i in range(4):#再生ボタンの作成
    for j in range(4):
        button[i].append(tk.Button(root, text = count, width = 10, height = 4))   
        button[i][j].bind("<1>",callback(self,i,j))
        button[i][j].bind("<3>",set_sound(self,i,j))
        count += 1
for i in range(1,5):#再生ボタンの配置
     for j in range(1,5):
         button[i-1][j-1].grid(row = i, column = j, padx = 10, pady = 5)

root.mainloop()