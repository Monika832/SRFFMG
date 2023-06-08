import numpy as np
import os
from pathlib import Path
import cv2
from multiprocessing import Pool
import tqdm

HIGH_DIR = "high"
LOW_DIR = "low"

if not os.path.exists(HIGH_DIR):
  os.mkdir(HIGH_DIR)
if not os.path.exists(LOW_DIR):
  os.mkdir(LOW_DIR)
IMAGE_DIR = "../../sample"


def add_noise_and_save(args):
  img,idx = args
  img = cv2.imread(str(img))
  org = img[0:297, 0:297]  
  reduced = cv2.resize(org,(74,74))
  uni_noise=np.zeros((74,74,3),dtype=np.uint8)
  cv2.randu(uni_noise,0,255)
  uni_noise=(uni_noise*0.5).astype(np.uint8)
  un_img=cv2.add(reduced,uni_noise)
  imp_noise=np.zeros((74,74,3),dtype=np.uint8)
  cv2.randu(imp_noise,0,255)
  imp_noise=cv2.threshold(imp_noise,245,255,cv2.THRESH_BINARY)[1]
  in_img=cv2.add(un_img,imp_noise)
  in_img= cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite(os.path.join(HIGH_DIR,f"{idx}.jpg"),org)
  cv2.imwrite(os.path.join(LOW_DIR,f"{idx}.jpg"),in_img)

images = list(Path(IMAGE_DIR).glob("*.jpg"))
images = images + list(Path(IMAGE_DIR).glob("*.Jpg"))

idx = np.arange(len(images))
args = list(zip(images,idx))
print(f"Total {len(args)} images")

with Pool() as p:
  list(tqdm.tqdm(p.imap_unordered(add_noise_and_save, args,chunksize=10), total=len(args)))
