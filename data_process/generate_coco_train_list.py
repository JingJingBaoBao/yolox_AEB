import glob
import numpy as np
txt_list = glob.glob('/media/sm/data2/luojie/centernet_data/luojie_3/*.txt')
# print(txt_list)
day = []
night = []
pd = []
cutin = []
diff = []
neg = []
for item in txt_list:
    if item.find('night_data') != -1:
        print(item)
        with open(item) as fr:
            tmp = fr.readlines()
            night = night + tmp
            np.random.shuffle(night)
            np.random.shuffle(night)
    elif item.find('data_pd_more8') != -1:
        with open(item) as fr:
            tmp = fr.readlines()
            pd = pd+tmp
            np.random.shuffle(pd)
            np.random.shuffle(pd)
        print(item)
    elif item.find('night_pd_more8') != -1:
        with open(item) as fr:
            tmp = fr.readlines()
            pd = pd+tmp
            np.random.shuffle(pd)
            np.random.shuffle(pd)
        print(item)
    elif item.find('data_day_cut_in')!= -1:
        with open(item) as fr:
            tmp = fr.readlines()
            cutin = cutin+tmp
            np.random.shuffle(cutin)
            np.random.shuffle(cutin)
        print(item)
    elif item.find('night_cut_in')!= -1:
        with open(item) as fr:
            tmp = fr.readlines()
            cutin = cutin+tmp
            np.random.shuffle(cutin)
            np.random.shuffle(cutin)
        print(item)
    # elif item.find('data_diff')!= -1:
    #     with open(item) as fr:
    #         diff = fr.readlines()
    #         # diff = diff+tmp
    #         np.random.shuffle(diff)
    #         np.random.shuffle(diff)
    #     print(item)
    # elif item.find('list_neg')!= -1:
    #     with open(item) as fr:
    #         neg = fr.readlines()
    #         # diff = diff+tmp
    #         np.random.shuffle(neg)
    #         np.random.shuffle(neg)
    #     print(item)
    elif item.find('train_list')!= -1:
        continue
    elif item.find('special')!= -1:
        continue
    else:
        print(item)
        tmp = []
        with open(item) as fr:
            tmp = fr.readlines()
        day = day+tmp
np.random.shuffle(day)
np.random.shuffle(day)
num_pd = len(pd)
num_night = len(night)
num_day = len(day)
num_cut=len(cutin)
num_diff = len(diff)
num_neg = len(neg)

print("pd",num_pd)
print("night",num_night)
print("day",num_day)
print("cut",num_cut)
print("diff", num_diff)
print("neg", num_neg)

pd_idx = 0
night_idx = 0
cut_idx = 0
diff_idx = 0
neg_idx = 0

write_list_train = []
write_list_val = []
from tqdm import tqdm
for i in tqdm(range(num_day)):
    if i % 1000 == 0:
        write_list_val.append(day[i])
        nidx = night_idx%num_night
        night_idx+=1
        write_list_val.append(night[nidx])
        pidx = pd_idx%num_pd
        pd_idx+=1
        write_list_val.append(pd[pidx])
        cutidx = cut_idx%num_cut
        cut_idx+=1
        write_list_val.append(cutin[cutidx])
        diffidx = diff_idx%num_diff
        diff_idx+=1
        write_list_val.append(diff[diffidx])
        # np.random.shuffle(write_list_val)
        # np.random.shuffle(write_list_val)
        
    else:
        write_list_train.append(day[i])
        nidx = night_idx%num_night
        night_idx+=1
        write_list_train.append(night[nidx])
        if i %2 == 0:
            pidx = pd_idx%num_pd
            pd_idx+=1
            write_list_train.append(pd[pidx])
            cutidx = cut_idx%num_cut
            cut_idx+=1
            write_list_train.append(cutin[cutidx])
        if i % 4 == 0:
            diffidx = diff_idx%num_diff
            diff_idx+=1
            write_list_train.append(diff[diffidx])
            # negidx = neg_idx % num_neg
            # neg_idx += 1
            # write_list_train.append(neg[negidx])
        
        # np.random.shuffle(write_list_train)
        # np.random.shuffle(write_list_train)


with open(fr'/media/sm/data2/luojie/centernet_data/voc/ImageSets/Main/coco_train_list.txt','w') as fw:
    for sub in write_list_train:
        fw.write('%s'%sub)

# with open(fr'/media/sm/data2/luojie/centernet_data/voc/ImageSets/Main/coco_val_list.txt','w') as fw:
#     for sub in write_list_val:
#         fw.write('%s'%sub)
