from os import path,listdir
from PIL import Image
rd_path = "./in"
wt_path = "./out"

def mkdir(path = wt_path):
        if not os.path.exists(path):
                os.makedirs(path)

def changeSize(ratio,img):
        img = img

def changeDPI(dpi,img):


'''
for filelist in listdir(rd_path):
        print(rd_path,filelist)
        filename = path.join(rd_path,filelist)
        if path.isfile(filename):
                im = Image.open(filename)
                (x,y) = im.size
                print(x,y)
                x_s = round(x/2)
                y_s = round(y/2)
                resized = im.resize((x_s,y_s))
                resized.save(path.join(wt_path,filelist),dpi = (30,30))
'''