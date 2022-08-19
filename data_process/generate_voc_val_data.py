from asyncore import write
import os
import os.path as osp
import numpy as np
from tqdm import tqdm
import glob

save_path = "/home/sunxusheng/projects/yolox/yolox-pytorch-main"
os.makedirs(save_path,exist_ok=True)

data_dir_list = glob.glob("/media/edata/sunxusheng/ground_truth/*_process_txt")

write_list = []

for dir in data_dir_list:
    for file in os.listdir(dir):
        with open(osp.join(dir, file), 'r') as f:
            string = osp.join(dir, file).replace(".txt", ".png")
            for line in f.readlines():
                label, xmin, ymin, xmax, ymax = line.split()
                if label == "10":
                    label = 0
                elif label == "20":
                    label = 1
                elif label == "11":
                    continue
                new_str = f'{xmin},{ymin},{xmax},{ymax},{label}'
                string = string + " " + new_str
            write_list.append(string)


with open(osp.join(save_path, "voc_val_list.txt"), 'w') as f:
    for info in write_list:
        f.write(info + '\n')




            


