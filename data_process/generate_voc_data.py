from asyncore import write
import os
import os.path as osp
import numpy as np
from tqdm import tqdm
import glob

save_path = "/media/edata/sunxusheng/AEB/luojie/data/voc_train_0517"
os.makedirs(save_path,exist_ok=True)

data_dir_list = glob.glob("/media/edata/sunxusheng/AEB/luojie/data/label_process_data_0517")
write_list = []
day = []
night = []
cutin = []
pd = []

for dir in data_dir_list:
    for root, dir, files in os.walk(dir):
        for file in files:
            item = root.split('/')[-1]
            if item == "day":
                day.append(osp.join(root, file))
            elif item == "night":
                night.append(osp.join(root, file))
            elif item == "day_cutin" or item == "night_cutin":
                cutin.append(osp.join(root, file))
            elif item == "day_pd" or item == "night_pd":
                pd.append(osp.join(root, file))
print(len(day), len(night), len(cutin), len(pd))
np.random.shuffle(day)
np.random.shuffle(night)
np.random.shuffle(cutin)
np.random.shuffle(pd)

all_list = [day, night, cutin, pd]
for l in all_list:
    for i in range(len(l)):
        try:
            with open(l[i], 'r') as f:
                string = l[i]
                for line in f.readlines():
                    label, xmin, ymin, xmax, ymax = line.split()
                    if label == "10":
                        label = 0
                    elif label == "20":
                        label = 1
                    elif label == "11":
                        label = 2
                    new_str = f'{xmin},{ymin},{xmax},{ymax},{label}'
                    string = string + " " + new_str
            l[i] = string
        except:
            print(l[i])

night_idx, cutin_idx, pd_idx = 0, 0, 0
with open(osp.join(save_path, "voc_train_list.txt"), 'w') as f:
    for i in range(len(day)):
        f.write(day[i]+'\n')
        night_idx %= len(night)
        f.write(night[night_idx]+'\n')
        night_idx += 1

        if i % 2 == 0:
            cutin_idx %= len(cutin)
            f.write(cutin[cutin_idx]+'\n')
            cutin_idx += 1
        
        if i % 4 == 0:
            pd_idx %= len(pd)
            f.write(pd[pd_idx]+'\n')
            pd_idx += 1





            


