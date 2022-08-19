import os
import os.path as osp
import shutil
from tqdm import tqdm

root_path = fr"/media/edata/sunxusheng/ground_truth"

for root, dir, files in os.walk(root_path):
    for txt_file in tqdm(files):
        if not txt_file.endswith('txt'):
            continue
        boxes = []
        with open(osp.join(root, txt_file), 'r') as f:
            for line in f.readlines():
                boxes.append(line)

        save_path = root.replace("day_txt", "day_process_txt").replace("night_txt", "night_process_txt")
        os.makedirs(save_path, exist_ok=True)
        with open(osp.join(save_path, txt_file), 'w') as f:
            for m in range(len(boxes)):
                    label, xmin, ymin, xmax, ymax = boxes[m].split()
                    if label == '100':
                        new_label = 11
                    elif label == '11' or label == '21':
                        new_label = 10
                    elif label == '32' or label == '43' or label == '53':
                        new_label = 20
                    # elif label == '43' or label == '53':
                    #     new_label = 20
                    # elif label == '32':
                    #     new_label = 30
                    f.write('%d %d %d %d %d\n' % (new_label, int(xmin), int(ymin), int(xmax), int(ymax)))
