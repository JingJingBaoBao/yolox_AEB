import os
import os.path as osp
import shutil
from tqdm import tqdm

txt_path = fr"/media/sm/data2/luojie/centernet_data/luojie_3/coco_train_list.txt"
dst_path_train = fr"/media/sm/data2/luojie/centernet_data/COCO/train_label_txt"
dst_path_val = fr"/media/sm/data2/luojie/centernet_data/COCO/val_label_txt"

os.makedirs(dst_path_train, exist_ok=True)
os.makedirs(dst_path_val, exist_ok=True)

with open(txt_path, 'r') as f:
    for file in tqdm(f.readlines()):
        if len(file.split()) == 2:
            image, label = file.split()
            post_fix = image.split('/')[-2].split('data')[-1]
            # image_file = image.split('/')[-1]
            label_file = label.split('/')[-1]

            # save_file =  image_file.split('_W1280')[0] + post_fix + "_W1280" +  image_file.split('_W1280')[-1]
            save_file =  label_file.split('_W1280')[0] + post_fix + "_W1280" +  label_file.split('_W1280')[-1]

            # print(save_file)
            shutil.copy(label, osp.join(dst_path_train, save_file))
        # else:
        #     image = file.strip()
        #     # post_fix = image.split('/')[-2].split('data')[-1]
        #     image_file = image.split('/')[-1]
        #     # save_file =  image_file.split('_W1280')[0] + post_fix + "_W1280" +  image_file.split('_W1280')[-1]
        #     # print(image_file)
        #     # exit(-1)
        #     shutil.copy(image, osp.join(dst_path_val, image_file))


print("Done!")