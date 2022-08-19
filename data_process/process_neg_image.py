import os
import os.path as osp
import shutil

txt_path = fr"/media/sm/data2/luojie/centernet_data/COCO/train_label_txt"
img_path = fr"/media/sm/data2/luojie/centernet_data/COCO/train2017"
neg_path = fr"/media/sm/data2/luojie/centernet_data/COCO/neg_image"

os.makedirs(neg_path, exist_ok=True)
txt_list = []
for file in os.listdir(txt_path):
    txt_list.append(file.replace('txt', 'png'))

from tqdm import tqdm
for image in tqdm(os.listdir(img_path)):
    if image not in txt_list:
        shutil.move(osp.join(img_path, image), osp.join(neg_path, image))