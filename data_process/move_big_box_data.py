import os
import os.path as osp
import shutil
save_path = "/home/sunxusheng/projects/yolox/yolox-pytorch-main/big_box"
if osp.exists(save_path):
    shutil.rmtree(save_path)
os.makedirs(save_path, exist_ok=True)

with open("11.txt", "r") as f:
    for line in f.readlines():
        png_path = line.replace('txt', 'png').replace('label_process_','').strip()
        
        # print(png_path)
        # print(osp.exists(png_path.strip()))
        print(osp.join(save_path, png_path.split('/')[-1]))
        shutil.copy(png_path, osp.join(save_path, png_path.split('/')[-1]))