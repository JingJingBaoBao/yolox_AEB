import numpy as np
import cv2
import os
import os.path as osp
from tqdm import tqdm
from PIL import Image

yuv_root = fr"/home/sunxusheng/projects/yolox/yolox-pytorch-main/image008_yuv422"

files = os.listdir(yuv_root)
for i in tqdm(range(len(files))):
    file = files[i]
    filepath = osp.join(yuv_root, file)
    dst = filepath.replace('yuv422', 'yuv444').replace('L', 'LC')
    if osp.exists(osp.join(dst)):
        continue
    img = np.array(Image.open(filepath))
    Y = img[:720, ]
    uv = np.repeat(img[720:, ], 2).reshape(720 * 2, -1)
    U = uv[:720]
    V = uv[720:]
    YUV = np.array([Y,U,V]).transpose([1,2,0])
    img = Image.fromarray(YUV)
    os.makedirs(os.path.split(dst)[0], exist_ok=True)
    img.save(dst)