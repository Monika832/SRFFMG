import cv2
import os

def image_loader(path):
    get_path = os.path.abspath(path).replace("LR","LR35")
    img1,_ = cv2.imread(path), cv2.imread(get_path)
    return img1,_
    