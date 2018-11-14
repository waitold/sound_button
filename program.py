import tkinter as tk 
from tkinter import ttk
import os,tkinter.filedialog, tkinter.messagebox
import pygame
import time

class Application(tk.Frame):

    def __init__(self, master = None):
        #コンストラクタ
        super().__init__(master)
        self.place()
        self.button = [[],[],[],[]]
        self.button_name = [[],[],[],[]]
        self.file_path = [[],[],[],[]]
        self.read_files()
        self.create_widgets()

    def create_widgets(self):
        #ウィジェットの作成、配置
        count = 1
        for i in range(4):#再生ボタンの作成
            for j in range(4):
                self.button[i].append(ButtonProces(name = self.button_name[i][j],column = j, row = i))   
                self.button[i][j].grid(row = i + 1, column = j + 1, padx = 5, pady = 5)
                count += 1


    def read_files(self):
        #ファイルの読み込み
        count = 0
        line =''
        with open('filepath.txt', mode = 'r') as f:
            for i in range(4):
                for j in range(4):
                    line = f.readline()
                    line = line[0:-1]
                    line.rstrip()
                    self.file_path[i].append(line)
                    count += 1
        count = 0
        with open('button_name.txt', mode = 'r') as f:
            for i in range(4):
                for j in range(4):
                    line = f.readline()
                    line.strip()
                    self.button_name[i].append(line)
                    count += 1

    def write_files(self):#ファイルの書き込み
        with open('filepath.txt', mode = 'w') as f:
            for i in range(4):
                for j in range(4):
                    f.write(self.file_path[i][j] + "\n")
        with open('button_name.txt', mode = 'w') as f:
            for i in range(4):
                for j in range(4):
                    f.write(self.button_name[i][j])
        

class ButtonProces(tk.Button):
    def __init__(self, master = None, name = None, column = None, row = None):
        tk.Button.__init__(self,master = None,text = name, width = 10, height = 4)
        self.bind("<1>",self.play)
        self.bind("<3>", self.set_sound)
        self.column =  column
        self.row = row
        self.entry_frame = tk.Frame()
        
    def play(self,event):#サウンドの再生
        filepath = app.file_path[event.widget.row][event.widget.column]
        filepath.strip()
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(1)
        time.sleep(0.05)
        pygame.mixer.music.stop()

    def set_sound(self,event):#サウンドのファイルパス取得
        fTyp = [("","*.mp3")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        tk.messagebox.showinfo('sound button','処理ファイルを選択してください！')
        file = tk.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        #tkinter.messagebox.showinfo('sound button',file)
        
        filepath =""
        for i in file:
            filepath += i
        app.file_path[event.widget.row][event.widget.column] = filepath  #ファイルパスを書き込み

        filename = os.path.basename(filepath)

        entry_label = tk.Label(self.entry_frame,text = "ボタン名を入力してください")
        entry = tk.Entry(self.entry_frame,width = 30)
        entry.insert(tk.END,filename)
        entry_button = tk.Button(self.entry_frame,text = "保存",command = lambda : self.set_name(event,entry.get()))
        entry_label.pack(anchor = tk.S)
        entry.pack(anchor = tk.S)
        entry_button.pack(anchor = tk.S)
        self.entry_frame.grid(column = 2,columnspan = 4,sticky = tk.W)

    def set_name(self,event,filename):#ボタン名の変更
        event.widget["text"] = filename
        app.button_name[event.widget.row][event.widget.column] = filename + '\n'
        app.write_files()
        self.entry_frame.destroy()


root = tk.Tk()
app = Application(master = root)
app.mainloop()
root.mainloop()