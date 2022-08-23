import os
import os.path as osp
import glob

file_list = glob.glob("/media/edata/sunxusheng/AEB/luojie/data/label_process_data_*")
save_list = []


for file_path in file_list:
    for root, dir, files in os.walk(file_path):
        for file in files:
            if not file.endswith('txt'):
                continue
            with open(osp.join(root, file), "r") as f:
                for line in f.readlines():
                    label, xmin, ymin, xmax, ymax = line.split()
                    w = int(xmax) - int(xmin)
                    h = int(ymax) - int(ymin)
                    if w * h > 250000:
                        save_list.append(osp.join(root, file))
                        break
for _ in save_list:
    print(_)
