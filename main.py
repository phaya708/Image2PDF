import os
import img2pdf
from PIL import Image # img2pdfと一緒にインストールされたPillowを使います
import tkinter as tk
from tkinter import filedialog
import glob



class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(u"Image2PDF")
        self.root.geometry("700x500")
        self.files = glob.glob('input/png/*')
        self.MainMenu()

    def MainMenu(self):
      print(self.files)
      lbl_savename = tk.Label(text='保存ファイル名')
      lbl_savename.grid(row=0, column=0)
      self.txt_savename= tk.Entry(width=30)
      self.txt_savename.grid(row=0, column=1, pady=10)
      #self.txt_port.insert(0, self.data['subject'])
      self.dir_list = tk.StringVar(self.root, value=self.files)
      self.list_box = tk.Listbox(self.root, listvariable=self.dir_list, width=50)
      self.list_box.grid(row=1, column=1, pady=10)

      button_path = tk.Button(text=u'参照', command=self.FolderSelect)
      button_path.grid(row=7, column=2, pady=20)


      button_up = tk.Button(text=u'上へ', command=self.Exchange_up)
      button_up.grid(row=6, column=3, padx=10, pady=10)

      button_down = tk.Button(text=u'下へ', command=self.Exchange_down)
      button_down.grid(row=7, column=3, padx=10, pady=10)

      button_create = tk.Button(text=u'PDF作成', command=self.Run)
      button_create.grid(row=7, column=1, padx=10, pady=10)
      self.root.mainloop()

    def Get_Image(self):
      n = self.list_box.curselection()[0]
      return self.files[n]

    def Exchange_up(self):
      n = self.list_box.curselection()[0]
      if(n != 0):
        tmp_dir = self.files[n]
        self.files[n] = self.files[n-1]
        self.files[n-1] = tmp_dir
        self.dir_list.set(self.files)
        self.list_box.select_clear(n)
        self.list_box.select_set(n-1)

    def Exchange_down(self):
      n = self.list_box.curselection()[0]
      if(n != len(self.files)-1):
        tmp_dir = self.files[n]
        self.files[n] = self.files[n+1]
        self.files[n+1] = tmp_dir
        self.dir_list.set(self.files)
        self.list_box.select_clear(n)
        self.list_box.select_set(n+1)

    def FolderSelect(self):
        self.dir_name = (tk.filedialog.askdirectory() + "/*").replace('/', os.sep)
        self.files = glob.glob(self.dir_name)
        print(self.files)
        self.dir_list.set(self.files)

    def Run(self):
      pdf_dir_path = "pdf/".replace('/', os.sep) # 出力するPDFのディレクトリ名
      os.makedirs(pdf_dir_path, exist_ok=True)
      png_Folder = self.files
      self.filename = self.txt_savename.get()
      extension  = ".png" # 拡張子がPNGのものを対象
      
      pdf_path = pdf_dir_path + self.filename

      with open(pdf_path,"w+b") as f:
          # 画像フォルダの中にあるPNGファイルを取得し配列に追加、バイナリ形式でファイルに書き込む
          f.write(img2pdf.convert([Image.open(fname).filename for fname in png_Folder]))
      
      print("Success for PDF create")
      return

if __name__ == '__main__':
    app = Application()