import os
import os.path as osp
import shutil

dst = fr"/media/sm/data2/luojie/centernet_data/COCO/train_label_xml"
src = fr"/media/sm/data2/luojie/centernet_data/COCO/val_label_xml"

for file in os.listdir(src):
    shutil.move(osp.join(src, file), osp.join(dst, file))