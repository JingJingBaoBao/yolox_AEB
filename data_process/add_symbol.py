from curses import savetty
import os
import os.path as osp
import shutil
from tqdm import tqdm
import glob
from PIL import Image
import numpy as np
import cv2

sym_path = "/home/sunxusheng/projects/yolox/yolox-pytorch-main/symbol.png"
path = fr"/media/edata/sunxusheng/AEB/luojie/data/data_0517"
save_path = fr"/media/edata/sunxusheng/AEB/luojie/data/symbol_0517"
os.makedirs(save_path, exist_ok=True)

symbol = cv2.imread(sym_path)
symbol = cv2.resize(symbol,(1280, 720))
sym_data = np.array(symbol, np.float32)
mask_data = np.zeros((720, 1280,3))
mask_data[sym_data[:] < 255] = sym_data[sym_data[:] < 255]
mask_data.reshape((720, 1280,3))

for root, dirs, files in os.walk(path):
    for file in tqdm(files):
        if not file.endswith('png'):
            continue
        img = cv2.imread(osp.join(root, file))
        img_data = np.array(img, np.float32)
        new_img_data = mask_data * 0.5 + img_data * 0.5

        cv2.imwrite( "111.png", new_img_data)

