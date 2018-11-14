import tkinter as tk 
from tkinter import ttk
import os,tkinter.filedialog, tkinter.messagebox

class Application(tk.Frame):

    def __init__(self, master = None):
        #コンストラクタ
        super().__init__(master)
        self.place()
        self.button = [[],[],[],[]]
        self.button_name = [[],[],[],[]]
        self.file_path = [[],[],[],[]]
        self.create_widgets()
        self.read_files()

    def create_widgets(self):
        #ウィジェットの作成、配置
        count = 1
        for i in range(4):#再生ボタンの作成
            for j in range(4):
                self.button[i].append(ButtonProces(count = count))   
                self.button[i][j].grid(row = i + 1, column = j + 1, padx = 5, pady = 5)
                count += 1


    def read_files(self):
        #ファイルの読み込み
        count = 0
        with open('filepath.txt') as f:
            for i in range(4):
                for j in range(4):
                    self.file_path[i].append(f.readline(count))

class ButtonProces(tk.Button):
    def __init__(self, master = None, count = None):
        tk.Button.__init__(self,master = None,text = count, width = 10, height = 4)
        self.bind("<1>",self.play)
        self.bind("<3>", self.set_sound)
        
    def play(self,event):
        print(event.widget["text"])

    def set_sound(self,event):
        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        tk.messagebox.showinfo('sound button','処理ファイルを選択してください！')
        file = tk.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        #tkinter.messagebox.showinfo('sound button',file)
        
        filepath =""
        for i in file:
            filepath += i
        filename = os.path.basename(filepath)

        entry_label = tk.Label(text = "ボタン名を入力してください")
        entry = tk.Entry(width = 30)
        entry.insert(tk.END,filename)
        entry_button = tk.Button(text = "保存",command = lambda : self.set_name(event,entry.get()))
        entry_label.grid(row = 1, column = 1, columnspan = 4,sticky = tk.S)
        entry.grid(row = 2, column = 1, columnspan = 4, sticky = tk.S)
        entry_button.grid(row = 2,column = 4)

    def set_name(self,event,filename):
        event.widget["text"] = filename


root = tk.Tk()
app = Application(master = root)
app.mainloop()