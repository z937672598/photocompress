from os import path,listdir,makedirs
from PIL import Image
rd_path = "./in"
wt_path = "./out"

def mkdir(path = wt_path):
        if not path.exists(path):
                makedirs(path)

def changeRes(ratio,img):
        (x0,y0) = img.size
        x1 = round(x0 * ratio)
        y1 = round(y0 * ratio)
        img = img.resize((x1,y1))
        return img

#def changeDPI(dpi,img):
