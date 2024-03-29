from random import sample, shuffle
import os
import cv2
import numpy as np
import torch
from PIL import Image
from torch.utils.data.dataset import Dataset

from utils.utils import cvtColor, preprocess_input


class YoloDataset(Dataset):
    def __init__(self, annotation_lines, neg_images_lines, input_shape, num_classes, epoch_length, \
                 mosaic, mixup, mosaic_prob, mixup_prob, train, special_aug_ratio=0.7):
        super(YoloDataset, self).__init__()
        self.annotation_lines = annotation_lines
        self.neg_images_lines = neg_images_lines
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.epoch_length = epoch_length
        self.mosaic = mosaic
        self.mosaic_prob = mosaic_prob
        self.mixup = mixup
        self.mixup_prob = mixup_prob
        self.train = train
        self.special_aug_ratio = special_aug_ratio
        self.epoch_now = -1
        self.length = len(self.annotation_lines)
        self.neg_length = len(self.neg_images_lines)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        index_neg = index % self.neg_length
        index = index % self.length
        #   训练时进行数据的随机增强
        #   验证时不进行数据的随机增强
        if self.mosaic and self.rand() < self.mosaic_prob and self.epoch_now < self.epoch_length * self.special_aug_ratio:
            lines = sample(self.annotation_lines, 3)
            lines.append(self.annotation_lines[index])
            shuffle(lines)
            image, box = self.get_random_data_with_Mosaic(lines, self.input_shape)

            if self.mixup and self.rand() < self.mixup_prob:
                lines = sample(self.annotation_lines, 1)
                image_2, box_2 = self.get_random_data(lines[0], self.input_shape, random=self.train)
                image, box = self.get_random_data_with_MixUp(image, box, image_2, box_2)
        else:
            image, box = self.process_data(self.annotation_lines[index], self.neg_images_lines[index_neg], self.input_shape, random=self.train)

        # 生成image和box
        # lines = sample(self.annotation_lines, 3)
        # lines.append(self.annotation_lines[index])
        # lines = [self.annotation_lines[index], self.neg_images_lines[index_neg]]
        # image, box = self.process_data(lines, random = self.train)

        image = np.transpose(preprocess_input(np.array(image, dtype=np.int8)), (2, 0, 1))
        box = np.array(box, dtype=np.float32)
        if len(box) != 0:
            box[:, 2:4] = box[:, 2:4] - box[:, 0:2]
            box[:, 0:2] = box[:, 0:2] + box[:, 2:4] / 2
        return image, box

    def rand(self, a=0, b=1):
        return np.random.rand() * (b - a) + a

    def crop_two_roi(self, image):
        image_crop = image[80:, :, :]
        test_img = cv2.resize(image_crop, (640, 320), interpolation=cv2.INTER_LINEAR)
        #####################
        img_0 = cv2.resize(test_img, (256, 128), interpolation=cv2.INTER_LINEAR)
        img_1 = test_img[96:96+128,192:192+256, :]
        gene_image = np.concatenate([img_0, img_1], axis=1)

        return gene_image

    def process_data(self, annotation_line, neg_lines, input_shape, random=True):
        # image 要转成numpy格式
        
        line = annotation_line.split()
        neg_line = neg_lines.strip()

        pos_image = cv2.imread(line[0])
        neg_image = cv2.imread(neg_line)

        pos_image = self.crop_two_roi(pos_image)
        neg_image = self.crop_two_roi(neg_image)
        image_arr = np.concatenate([pos_image, neg_image],axis=1)
        image = Image.fromarray(image_arr)
        #cv2.imwrite(os.path.join("/home/sunxusheng/projects/yolox/yolox-pytorch-main/box_debug", line[0].split('/')[-1]), image_arr)
        # ------------------------------#
        iw, ih = image.size
        h, w = input_shape

        box = np.array([np.array(list(map(int, box.split(',')))) for box in line[1:]])

        box_2 = box.copy()
        if len(box) > 0:
            np.random.shuffle(box)
            box[:, [0, 2]] = box[:, [0, 2]] / 5
            box[:, [1, 3]] = (box[:, [1, 3]] - 80) / 5
            box[:, 0:2][box[:, 0:2] < 0] = 0
            box[:, 2][box[:, 2] > w/4] = w/4
            box[:, 3][box[:, 3] > h] = h
            box_w = box[:, 2] - box[:, 0]
            box_h = box[:, 3] - box[:, 1]
            box = box[np.logical_and(box_w > 1, box_h > 1)]

            np.random.shuffle(box_2)
            box_2[:, [0, 2]] = box_2[:, [0, 2]] / 2 - 192 + 256
            box_2[:, [1, 3]] = (box_2[:, [1, 3]] - 80) / 2 - 96 
            # box_2[:, 0:2][box_2[:, 0:2] < 0] = 0
            box_2[:, 0][box_2[:, 0] < w/4] = w/4
            box_2[:, 2][box_2[:, 2] > w/2] = w/2
            box_2[:, 1][box_2[:, 1] < 0] = 0
            box_2[:, 3][box_2[:, 3] > h] = h
            box_w = box_2[:, 2] - box_2[:, 0]
            box_h = box_2[:, 3] - box_2[:, 1]
            box_2 = box_2[np.logical_and(box_w > 1, box_h > 1)]

        final_box = []
        for b in box:
            final_box.append(np.array(list(b)))
        for b in box_2:
            final_box.append(np.array(list(b)))
        final_box = np.array(final_box)

        # for box in final_box:
        #     xmin, ymin, xmax, ymax, label = box
        #     print(xmin, ymin, xmax, ymax)
        #     xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)
        #     if int(label) == 0:
        #         cv2.rectangle(image_arr, (xmin, ymin), (xmax, ymax-1), (0, 0, 255), 1)
        #     elif int(label) == 1:
        #         cv2.rectangle(image_arr, (xmin, ymin), (xmax, ymax-1), (0, 255, 255), 1)
        #     elif int(label) == 2:
        #         cv2.rectangle(image_arr, (xmin, ymin), (xmax, ymax-1), (0, 255, 0), 1)

        # cv2.imwrite(os.path.join("/home/sunxusheng/projects/yolox/yolox-pytorch-main/box_debug", line[0].split('/')[-1]), image_arr)
            # for box in box_right:
            #     xmin, ymin, xmax, ymax, label = box
            #     print(xmin, ymin, xmax, ymax)
            #     xmin, ymin, xmax, ymax = int(xmin), int(ymin), int(xmax), int(ymax)
            #     if int(label) == 0:
            #         cv2.rectangle(gene_image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
            #     elif int(label) == 1:
            #         cv2.rectangle(gene_image, (xmin, ymin), (xmax, ymax), (0, 255, 255), 1)
            #     elif int(label) == 2:
            #         cv2.rectangle(gene_image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)

            # with open(fr"F:\AEB\data\yolox-pytorch-main\1.txt", "w") as f:
            #     for b in new_box:
            #         xmin, ymin, xmax, ymax, label = b
            #         f.write('%d %d %d %d %d\n'%(xmin, ymin, xmax, ymax, label))
        return image, final_box

    def get_random_data(self, annotation_line, neg_lines, input_shape, jitter=.3, hue=.1, sat=0.7, val=0.4, random=True):
        line = annotation_line.split()
        neg_line = neg_lines.strip()
        # print("line", line)
        # print("negline", neg_line)
        # # ------------------------------#
        # #   读取图像并转换成RGB图像
        # # ------------------------------#
        # print("line[0]", line[0])
        # print("negline[0]", neg_line[0])

        # pos_image = Image.open(line[0])
        # neg_image = Image.open(neg_line)
        pos_image = cv2.imread(line[0])
        neg_image = cv2.imread(neg_line)

        # print(pos_image.size, neg_image.size, neg_line)
        image_arr = np.concatenate([pos_image, neg_image],axis=1)
        image = Image.fromarray(image_arr)
        # image = cvtColor(image)
        # ------------------------------#
        #   获得图像的高宽与目标高宽
        # ------------------------------#
        iw, ih = image.size
        h, w = input_shape
        # ------------------------------#
        #   获得预测框
        # ------------------------------#
        box = np.array([np.array(list(map(int, box.split(',')))) for box in line[1:]])

        if not random:
            scale = min(w / iw, h / ih)
            nw = int(iw * scale)
            nh = int(ih * scale)
            dx = (w - nw) // 2
            dy = (h - nh) // 2

            image = image.resize((nw, nh), Image.BICUBIC)
            new_image = Image.new('RGB', (w, h), (128, 128, 128))
            new_image.paste(image, (dx, dy))
            image_data = np.array(new_image, np.float32)

            if len(box) > 0:
                np.random.shuffle(box)
                box[:, [0, 2]] = box[:, [0, 2]] * nw / iw + dx
                box[:, [1, 3]] = box[:, [1, 3]] * nh / ih + dy
                box[:, 0:2][box[:, 0:2] < 0] = 0
                box[:, 2][box[:, 2] > w] = w
                box[:, 3][box[:, 3] > h] = h
                box_w = box[:, 2] - box[:, 0]
                box_h = box[:, 3] - box[:, 1]
                box = box[np.logical_and(box_w > 1, box_h > 1)]  # discard invalid box

            return image_data, box

        new_ar = iw / ih * self.rand(1 - jitter, 1 + jitter) / self.rand(1 - jitter, 1 + jitter)
        scale = self.rand(.2, .5)
        if new_ar < 1:
            nh = int(scale * h)
            nw = int(nh * new_ar)
        else:
            nw = int(scale * w)
            nh = int(nw / new_ar)
        # print(nw, nh, "nwnh")
        image = image.resize((nw, nh), Image.BICUBIC)

        dx = int(self.rand(0, w - nw))
        dy = int(self.rand(0, h - nh))
        new_image = Image.new('RGB', (w, h), (128, 128, 128))
        new_image.paste(image, (dx, dy))
        image = new_image

        flip = self.rand() < .5
        if flip: image = image.transpose(Image.FLIP_LEFT_RIGHT)

        image_data = np.array(image, np.float32)

        if len(box) > 0:
            np.random.shuffle(box)
            box[:, [0, 2]] = box[:, [0, 2]] * nw / iw + dx
            box[:, [1, 3]] = box[:, [1, 3]] * nh / ih + dy
            if flip: box[:, [0, 2]] = w - box[:, [2, 0]]
            box[:, 0:2][box[:, 0:2] < 0] = 0
            box[:, 2][box[:, 2] > w] = w
            box[:, 3][box[:, 3] > h] = h
            box_w = box[:, 2] - box[:, 0]
            box_h = box[:, 3] - box[:, 1]
            box = box[np.logical_and(box_w > 1, box_h > 1)]

        # im = np.uint8(image_data)
        # for b in box:
        #     if b[-1] != 2:
        #         cv2.rectangle(im, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (255, 0, 0))
        # cv2.imwrite(os.path.join("/home/sunxusheng/projects/yolox/yolox-pytorch-main/box_debug", line[0].split('/')[-1]), im)

        return image_data, box

    def merge_bboxes(self, bboxes, cutx, cuty):
        merge_bbox = []
        for i in range(len(bboxes)):
            for box in bboxes[i]:
                tmp_box = []
                x1, y1, x2, y2 = box[0], box[1], box[2], box[3]

                if i == 0:
                    if y1 > cuty or x1 > cutx:
                        continue
                    if y2 >= cuty and y1 <= cuty:
                        y2 = cuty
                    if x2 >= cutx and x1 <= cutx:
                        x2 = cutx

                if i == 1:
                    if y2 < cuty or x1 > cutx:
                        continue
                    if y2 >= cuty and y1 <= cuty:
                        y1 = cuty
                    if x2 >= cutx and x1 <= cutx:
                        x2 = cutx

                if i == 2:
                    if y2 < cuty or x2 < cutx:
                        continue
                    if y2 >= cuty and y1 <= cuty:
                        y1 = cuty
                    if x2 >= cutx and x1 <= cutx:
                        x1 = cutx

                if i == 3:
                    if y1 > cuty or x2 < cutx:
                        continue
                    if y2 >= cuty and y1 <= cuty:
                        y2 = cuty
                    if x2 >= cutx and x1 <= cutx:
                        x1 = cutx
                tmp_box.append(x1)
                tmp_box.append(y1)
                tmp_box.append(x2)
                tmp_box.append(y2)
                tmp_box.append(box[-1])
                merge_bbox.append(tmp_box)
        return merge_bbox

    def get_random_data_with_Mosaic(self, annotation_line, input_shape, jitter=0.3, hue=.1, sat=0.7, val=0.4):
        h, w = input_shape
        min_offset_x = self.rand(0.3, 0.7)
        min_offset_y = self.rand(0.3, 0.7)

        image_datas = []
        box_datas = []
        index = 0
        for line in annotation_line:
            line_content = line.split()
            image = Image.open(line_content[0])
            iw, ih = image.size
            box = np.array([np.array(list(map(int, box.split(',')))) for box in line_content[1:]])
            flip = self.rand() < 0.5
            if flip and len(box) > 0:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
                box[:, [0, 2]] = iw - box[:, [2, 0]]
            new_ar = iw / ih * self.rand(1 - jitter, 1 + jitter) / self.rand(1 - jitter, 1 + jitter)
            scale = self.rand(.4, 1)
            if new_ar < 1:
                nh = int(scale * h)
                nw = int(nh * new_ar)
            else:
                nw = int(scale * w)
                nh = int(nw / new_ar)
            image = image.resize((nw, nh), Image.BICUBIC)
            if index == 0:
                dx = int(w * min_offset_x) - nw
                dy = int(h * min_offset_y) - nh
            elif index == 1:
                dx = int(w * min_offset_x) - nw
                dy = int(h * min_offset_y)
            elif index == 2:
                dx = int(w * min_offset_x)
                dy = int(h * min_offset_y)
            elif index == 3:
                dx = int(w * min_offset_x)
                dy = int(h * min_offset_y) - nh

            new_image = Image.new('RGB', (w, h), (128, 128, 128))
            new_image.paste(image, (dx, dy))
            image_data = np.array(new_image)

            index = index + 1
            box_data = []
            # ---------------------------------#
            #   对box进行重新处理
            # ---------------------------------#
            if len(box) > 0:
                np.random.shuffle(box)
                box[:, [0, 2]] = box[:, [0, 2]] * nw / iw + dx
                box[:, [1, 3]] = box[:, [1, 3]] * nh / ih + dy
                box[:, 0:2][box[:, 0:2] < 0] = 0
                box[:, 2][box[:, 2] > w] = w
                box[:, 3][box[:, 3] > h] = h
                box_w = box[:, 2] - box[:, 0]
                box_h = box[:, 3] - box[:, 1]
                box = box[np.logical_and(box_w > 1, box_h > 1)]
                box_data = np.zeros((len(box), 5))
                box_data[:len(box)] = box

            image_datas.append(image_data)
            box_datas.append(box_data)

        cutx = int(w * min_offset_x)
        cuty = int(h * min_offset_y)

        new_image = np.zeros([h, w, 3])
        new_image[:cuty, :cutx, :] = image_datas[0][:cuty, :cutx, :]
        new_image[cuty:, :cutx, :] = image_datas[1][cuty:, :cutx, :]
        new_image[cuty:, cutx:, :] = image_datas[2][cuty:, cutx:, :]
        new_image[:cuty, cutx:, :] = image_datas[3][:cuty, cutx:, :]

        new_image = np.array(new_image, np.uint8)
        new_boxes = self.merge_bboxes(box_datas, cutx, cuty)
        image_d = Image.fromarray(new_image)
        # image_d.save(fr"F:\AEB\data\yolox-pytorch-main\img\1.png")
        return new_image, new_boxes

    def get_random_data_with_MixUp(self, image_1, box_1, image_2, box_2):
        new_image = np.array(image_1, np.float32) * 0.5 + np.array(image_2, np.float32) * 0.5
        if len(box_1) == 0:
            new_boxes = box_2
        elif len(box_2) == 0:
            new_boxes = box_1
        else:
            new_boxes = np.concatenate([box_1, box_2], axis=0)
        return new_image, new_boxes


# DataLoader中collate_fn使用
def yolo_dataset_collate(batch):
    images = []
    bboxes = []
    for img, box in batch:
        images.append(img)
        bboxes.append(box)
    images = torch.from_numpy(np.array(images)).type(torch.FloatTensor)
    bboxes = [torch.from_numpy(ann).type(torch.FloatTensor) for ann in bboxes]
    return images, bboxes
