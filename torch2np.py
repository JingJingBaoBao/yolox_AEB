import torch
import torch.nn as nn
import numpy as np

from nets import yolo
from yolo import YoloBody

model_file = "/home/sunxusheng/projects/yolox/yolox-pytorch-main/logs/2022_08_24/ep041-loss2.208-val_loss2.144.pth"
net    = YoloBody(3, 'nano')
net.eval()
ckpt = torch.load(model_file)
net.load_state_dict(torch.load(model_file, map_location='cpu'))
net.eval()
weights = dict()
# print(net.state_dict())
print("------------------------")
for k,v in net.state_dict().items():
    print(k)
    weights[k] = v

np.save("./yolox_numpy_0826.npy", weights)

