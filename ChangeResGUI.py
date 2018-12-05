import ChangeRes
import tkinter
import os
import time
from PIL import Image

class GUI(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Changing Image!")
        self.lable = tkinter.Label(self.root, text="enter the ratio:")
        self.button_go = tkinter.Button(self.root, command = self.go, text = "Lets go!")
        #self.button_disable = tkinter.Button(self.root, command = self.disableProxy, text = "I am cool now.")
        self.ratio_input = tkinter.Entry(self.root,width = 30)
        #self.original_proxy = "HTTP:AMD YES"

    def gui_arrange(self):
        self.lable.pack()
        self.ratio_input.pack()
        #self.button_disable.pack()
        self.button_go.pack()

    def go(self):
        ChangeRes.mkdir(path = ChangeRes.rd_path)
        ChangeRes.mkdir(path = ChangeRes.wt_path)
        for filelist in os.listdir(ChangeRes.rd_path):
            filename = os.path.join(ChangeRes.rd_path,filelist)
            if os.path.isfile(filename):
                    img = Image.open(filename)
                    ChangeRes.changeRes(self.ratio_input,img)
                    img.save(os.path.join(ChangeRes.wt_path,filelist))


if __name__ == "__main__":
    gui = GUI()
    gui.gui_arrange()
    tkinter.mainloop()
    pass
