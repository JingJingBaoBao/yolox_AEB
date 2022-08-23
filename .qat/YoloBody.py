# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class YoloBody(torch.nn.Module):
    def __init__(self):
        super(YoloBody, self).__init__()
        self.module_0 = py_nndct.nn.Input() #YoloBody::input_0
        self.module_1 = py_nndct.nn.quant_input() #YoloBody::YoloBody/QuantStub[quant_stub]/input.1
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=[5, 5], stride=[2, 2], padding=[2, 2], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/FirstConv[backbone]/CSPDarknet[backbone]/FirstConv[stem]/Conv2d[conv]/input.2
        self.module_3 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/FirstConv[backbone]/CSPDarknet[backbone]/FirstConv[stem]/ReLU[act]/input.4
        self.module_4 = py_nndct.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/BaseConv[0]/Conv2d[conv]/input.5
        self.module_5 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/BaseConv[0]/ReLU[act]/input.7
        self.module_6 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.8
        self.module_7 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv1]/ReLU[act]/input.12
        self.module_8 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.10
        self.module_9 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv2]/ReLU[act]/12347
        self.module_10 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.13
        self.module_11 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.15
        self.module_12 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.16
        self.module_13 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/12399
        self.module_14 = py_nndct.nn.Add() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/Add[add]/12401
        self.module_15 = py_nndct.nn.Cat() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Cat[cat]/input.18
        self.module_16 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.19
        self.module_17 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv3]/ReLU[act]/input.21
        self.module_18 = py_nndct.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/BaseConv[0]/Conv2d[conv]/input.22
        self.module_19 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/BaseConv[0]/ReLU[act]/input.24
        self.module_20 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.25
        self.module_21 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv1]/ReLU[act]/input.29
        self.module_22 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.27
        self.module_23 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv2]/ReLU[act]/12508
        self.module_24 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.30
        self.module_25 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.32
        self.module_26 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.33
        self.module_27 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/12560
        self.module_28 = py_nndct.nn.Add() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/Add[add]/input.35
        self.module_29 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.36
        self.module_30 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/ReLU[act]/input.38
        self.module_31 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.39
        self.module_32 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/ReLU[act]/12614
        self.module_33 = py_nndct.nn.Add() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/Add[add]/input.41
        self.module_34 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.42
        self.module_35 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/ReLU[act]/input.44
        self.module_36 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/Conv2d[conv]/input.45
        self.module_37 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/ReLU[act]/12668
        self.module_38 = py_nndct.nn.Add() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/Add[add]/12670
        self.module_39 = py_nndct.nn.Cat() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Cat[cat]/input.47
        self.module_40 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.48
        self.module_41 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv3]/ReLU[act]/input.50
        self.module_42 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/BaseConv[0]/Conv2d[conv]/input.51
        self.module_43 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/BaseConv[0]/ReLU[act]/input.53
        self.module_44 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.54
        self.module_45 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv1]/ReLU[act]/input.58
        self.module_46 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.56
        self.module_47 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv2]/ReLU[act]/12777
        self.module_48 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.59
        self.module_49 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.61
        self.module_50 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.62
        self.module_51 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/12829
        self.module_52 = py_nndct.nn.Add() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/Add[add]/input.64
        self.module_53 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.65
        self.module_54 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/ReLU[act]/input.67
        self.module_55 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.68
        self.module_56 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/ReLU[act]/12883
        self.module_57 = py_nndct.nn.Add() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/Add[add]/input.70
        self.module_58 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.71
        self.module_59 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/ReLU[act]/input.73
        self.module_60 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/Conv2d[conv]/input.74
        self.module_61 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/ReLU[act]/12937
        self.module_62 = py_nndct.nn.Add() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/Add[add]/12939
        self.module_63 = py_nndct.nn.Cat() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Cat[cat]/input.76
        self.module_64 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.77
        self.module_65 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv3]/ReLU[act]/input.79
        self.module_66 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/BaseConv[0]/Conv2d[conv]/input.80
        self.module_67 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/BaseConv[0]/ReLU[act]/input.82
        self.module_68 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.83
        self.module_69 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv1]/ReLU[act]/13020
        self.module_70 = py_nndct.nn.MaxPool2d(kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], ceil_mode=False) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/MaxPool2d[m]/ModuleList[0]/13034
        self.module_71 = py_nndct.nn.MaxPool2d(kernel_size=[5, 5], stride=[1, 1], padding=[2, 2], dilation=[1, 1], ceil_mode=False) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/MaxPool2d[m]/ModuleList[1]/13048
        self.module_72 = py_nndct.nn.MaxPool2d(kernel_size=[7, 7], stride=[1, 1], padding=[3, 3], dilation=[1, 1], ceil_mode=False) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/MaxPool2d[m]/ModuleList[2]/13062
        self.module_73 = py_nndct.nn.Cat() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/Cat[cat]/input.85
        self.module_74 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.86
        self.module_75 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv2]/ReLU[act]/input.88
        self.module_76 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv1]/Conv2d[conv]/input.89
        self.module_77 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv1]/ReLU[act]/input.93
        self.module_78 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv2]/Conv2d[conv]/input.91
        self.module_79 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv2]/ReLU[act]/13143
        self.module_80 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.94
        self.module_81 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.96
        self.module_82 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.97
        self.module_83 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/13195
        self.module_84 = py_nndct.nn.Cat() #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Cat[cat]/input.99
        self.module_85 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv3]/Conv2d[conv]/input.100
        self.module_86 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv3]/ReLU[act]/input.102
        self.module_87 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[lateral_conv0]/Conv2d[conv]/input.103
        self.module_88 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[lateral_conv0]/ReLU[act]/13250
        self.module_89 = py_nndct.nn.ConvTranspose2d(in_channels=128, out_channels=128, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #YoloBody::YoloBody/Deconv[backbone]/Deconv[upsample1]/ConvTranspose2d[deconv]/input.105
        self.module_90 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Deconv[backbone]/Deconv[upsample1]/ReLU[act]/13276
        self.module_91 = py_nndct.nn.Cat() #YoloBody::YoloBody/Cat[backbone]/Cat[cat1]/input.107
        self.module_92 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/BaseConv[conv1]/Conv2d[conv]/input.108
        self.module_93 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/BaseConv[conv1]/ReLU[act]/input.112
        self.module_94 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/BaseConv[conv2]/Conv2d[conv]/input.110
        self.module_95 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/BaseConv[conv2]/ReLU[act]/13331
        self.module_96 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.113
        self.module_97 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.115
        self.module_98 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.116
        self.module_99 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/13383
        self.module_100 = py_nndct.nn.Cat() #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/Cat[cat]/input.118
        self.module_101 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/BaseConv[conv3]/Conv2d[conv]/input.119
        self.module_102 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p4]/BaseConv[conv3]/ReLU[act]/input.121
        self.module_103 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[reduce_conv1]/Conv2d[conv]/input.122
        self.module_104 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[reduce_conv1]/ReLU[act]/13438
        self.module_105 = py_nndct.nn.ConvTranspose2d(in_channels=64, out_channels=64, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0], output_padding=[0, 0], groups=1, bias=True, dilation=[1, 1]) #YoloBody::YoloBody/Deconv[backbone]/Deconv[upsample2]/ConvTranspose2d[deconv]/input.124
        self.module_106 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Deconv[backbone]/Deconv[upsample2]/ReLU[act]/13464
        self.module_107 = py_nndct.nn.Cat() #YoloBody::YoloBody/Cat[backbone]/Cat[cat2]/input.126
        self.module_108 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/BaseConv[conv1]/Conv2d[conv]/input.127
        self.module_109 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/BaseConv[conv1]/ReLU[act]/input.131
        self.module_110 = py_nndct.nn.Conv2d(in_channels=128, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/BaseConv[conv2]/Conv2d[conv]/input.129
        self.module_111 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/BaseConv[conv2]/ReLU[act]/13519
        self.module_112 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.132
        self.module_113 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.134
        self.module_114 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.135
        self.module_115 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/13571
        self.module_116 = py_nndct.nn.Cat() #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/Cat[cat]/input.137
        self.module_117 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/BaseConv[conv3]/Conv2d[conv]/input.138
        self.module_118 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_p3]/BaseConv[conv3]/ReLU[act]/input.140
        self.module_119 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[bu_conv2]/Conv2d[conv]/input.141
        self.module_120 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[bu_conv2]/ReLU[act]/13626
        self.module_121 = py_nndct.nn.Cat() #YoloBody::YoloBody/Cat[backbone]/Cat[cat3]/input.143
        self.module_122 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/BaseConv[conv1]/Conv2d[conv]/input.144
        self.module_123 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/BaseConv[conv1]/ReLU[act]/input.148
        self.module_124 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/BaseConv[conv2]/Conv2d[conv]/input.146
        self.module_125 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/BaseConv[conv2]/ReLU[act]/13681
        self.module_126 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.149
        self.module_127 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.151
        self.module_128 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.152
        self.module_129 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/13733
        self.module_130 = py_nndct.nn.Cat() #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/Cat[cat]/input.154
        self.module_131 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/BaseConv[conv3]/Conv2d[conv]/input.155
        self.module_132 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n3]/BaseConv[conv3]/ReLU[act]/input.157
        self.module_133 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[bu_conv1]/Conv2d[conv]/input.158
        self.module_134 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/BaseConv[backbone]/BaseConv[bu_conv1]/ReLU[act]/13788
        self.module_135 = py_nndct.nn.Cat() #YoloBody::YoloBody/Cat[backbone]/Cat[cat4]/input.160
        self.module_136 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/BaseConv[conv1]/Conv2d[conv]/input.161
        self.module_137 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/BaseConv[conv1]/ReLU[act]/input.165
        self.module_138 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/BaseConv[conv2]/Conv2d[conv]/input.163
        self.module_139 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/BaseConv[conv2]/ReLU[act]/13843
        self.module_140 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.166
        self.module_141 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.168
        self.module_142 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.169
        self.module_143 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/13895
        self.module_144 = py_nndct.nn.Cat() #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/Cat[cat]/input.171
        self.module_145 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/BaseConv[conv3]/Conv2d[conv]/input.172
        self.module_146 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/CSPLayer[backbone]/CSPLayer[C3_n4]/BaseConv[conv3]/ReLU[act]/input.204
        self.module_147 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/BaseConv[head]/ModuleList[stems]/ModuleList[0]/Conv2d[conv]/input.174
        self.module_148 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/BaseConv[head]/ModuleList[stems]/ModuleList[0]/ReLU[act]/input.176
        self.module_149 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[0]/BaseConv[0]/Conv2d[conv]/input.177
        self.module_150 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[0]/BaseConv[0]/ReLU[act]/input.179
        self.module_151 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[0]/BaseConv[1]/Conv2d[conv]/input.180
        self.module_152 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[0]/BaseConv[1]/ReLU[act]/input.182
        self.module_153 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[cls_preds]/ModuleList[0]/14022
        self.module_154 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[0]/BaseConv[0]/Conv2d[conv]/input.183
        self.module_155 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[0]/BaseConv[0]/ReLU[act]/input.185
        self.module_156 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[0]/BaseConv[1]/Conv2d[conv]/input.186
        self.module_157 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[0]/BaseConv[1]/ReLU[act]/input.188
        self.module_158 = py_nndct.nn.Conv2d(in_channels=64, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[reg_preds]/ModuleList[0]/14094
        self.module_159 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[obj_preds]/ModuleList[0]/14114
        self.module_160 = py_nndct.nn.Cat() #YoloBody::YoloBody/Cat[head]/ModuleList[cats]/ModuleList[0]/ip.1
        self.module_161 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/BaseConv[head]/ModuleList[stems]/ModuleList[1]/Conv2d[conv]/input.189
        self.module_162 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/BaseConv[head]/ModuleList[stems]/ModuleList[1]/ReLU[act]/input.191
        self.module_163 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[1]/BaseConv[0]/Conv2d[conv]/input.192
        self.module_164 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[1]/BaseConv[0]/ReLU[act]/input.194
        self.module_165 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[1]/BaseConv[1]/Conv2d[conv]/input.195
        self.module_166 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[1]/BaseConv[1]/ReLU[act]/input.197
        self.module_167 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[cls_preds]/ModuleList[1]/14215
        self.module_168 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[1]/BaseConv[0]/Conv2d[conv]/input.198
        self.module_169 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[1]/BaseConv[0]/ReLU[act]/input.200
        self.module_170 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[1]/BaseConv[1]/Conv2d[conv]/input.201
        self.module_171 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[1]/BaseConv[1]/ReLU[act]/input.203
        self.module_172 = py_nndct.nn.Conv2d(in_channels=64, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[reg_preds]/ModuleList[1]/14287
        self.module_173 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[obj_preds]/ModuleList[1]/14307
        self.module_174 = py_nndct.nn.Cat() #YoloBody::YoloBody/Cat[head]/ModuleList[cats]/ModuleList[1]/ip.2
        self.module_175 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/BaseConv[head]/ModuleList[stems]/ModuleList[2]/Conv2d[conv]/input.205
        self.module_176 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/BaseConv[head]/ModuleList[stems]/ModuleList[2]/ReLU[act]/input.207
        self.module_177 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[2]/BaseConv[0]/Conv2d[conv]/input.208
        self.module_178 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[2]/BaseConv[0]/ReLU[act]/input.210
        self.module_179 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[2]/BaseConv[1]/Conv2d[conv]/input.211
        self.module_180 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[cls_convs]/ModuleList[2]/BaseConv[1]/ReLU[act]/input.213
        self.module_181 = py_nndct.nn.Conv2d(in_channels=64, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[cls_preds]/ModuleList[2]/14408
        self.module_182 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[2]/BaseConv[0]/Conv2d[conv]/input.214
        self.module_183 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[2]/BaseConv[0]/ReLU[act]/input.216
        self.module_184 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[2]/BaseConv[1]/Conv2d[conv]/input.217
        self.module_185 = py_nndct.nn.ReLU(inplace=True) #YoloBody::YoloBody/Sequential[head]/ModuleList[reg_convs]/ModuleList[2]/BaseConv[1]/ReLU[act]/input
        self.module_186 = py_nndct.nn.Conv2d(in_channels=64, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[reg_preds]/ModuleList[2]/14480
        self.module_187 = py_nndct.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=False) #YoloBody::YoloBody/Conv2d[head]/ModuleList[obj_preds]/ModuleList[2]/14500
        self.module_188 = py_nndct.nn.Cat() #YoloBody::YoloBody/Cat[head]/ModuleList[cats]/ModuleList[2]/ip
        self.module_189 = py_nndct.nn.dequant_output() #YoloBody::YoloBody/DeQuantStub[dequant_stub]/14504
        self.module_190 = py_nndct.nn.dequant_output() #YoloBody::YoloBody/DeQuantStub[dequant_stub]/14507
        self.module_191 = py_nndct.nn.dequant_output() #YoloBody::YoloBody/DeQuantStub[dequant_stub]/14510

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(input=output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_3(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_6 = self.module_6(output_module_0)
        output_module_6 = self.module_7(output_module_6)
        output_module_8 = self.module_8(output_module_0)
        output_module_8 = self.module_9(output_module_8)
        output_module_10 = self.module_10(output_module_6)
        output_module_10 = self.module_11(output_module_10)
        output_module_10 = self.module_12(output_module_10)
        output_module_10 = self.module_13(output_module_10)
        output_module_10 = self.module_14(input=output_module_10, other=output_module_6, alpha=1)
        output_module_10 = self.module_15(dim=1, tensors=[output_module_10,output_module_8])
        output_module_10 = self.module_16(output_module_10)
        output_module_10 = self.module_17(output_module_10)
        output_module_10 = self.module_18(output_module_10)
        output_module_10 = self.module_19(output_module_10)
        output_module_20 = self.module_20(output_module_10)
        output_module_20 = self.module_21(output_module_20)
        output_module_22 = self.module_22(output_module_10)
        output_module_22 = self.module_23(output_module_22)
        output_module_24 = self.module_24(output_module_20)
        output_module_24 = self.module_25(output_module_24)
        output_module_24 = self.module_26(output_module_24)
        output_module_24 = self.module_27(output_module_24)
        output_module_24 = self.module_28(input=output_module_24, other=output_module_20, alpha=1)
        output_module_29 = self.module_29(output_module_24)
        output_module_29 = self.module_30(output_module_29)
        output_module_29 = self.module_31(output_module_29)
        output_module_29 = self.module_32(output_module_29)
        output_module_29 = self.module_33(input=output_module_29, other=output_module_24, alpha=1)
        output_module_34 = self.module_34(output_module_29)
        output_module_34 = self.module_35(output_module_34)
        output_module_34 = self.module_36(output_module_34)
        output_module_34 = self.module_37(output_module_34)
        output_module_34 = self.module_38(input=output_module_34, other=output_module_29, alpha=1)
        output_module_34 = self.module_39(dim=1, tensors=[output_module_34,output_module_22])
        output_module_34 = self.module_40(output_module_34)
        output_module_34 = self.module_41(output_module_34)
        output_module_42 = self.module_42(output_module_34)
        output_module_42 = self.module_43(output_module_42)
        output_module_44 = self.module_44(output_module_42)
        output_module_44 = self.module_45(output_module_44)
        output_module_46 = self.module_46(output_module_42)
        output_module_46 = self.module_47(output_module_46)
        output_module_48 = self.module_48(output_module_44)
        output_module_48 = self.module_49(output_module_48)
        output_module_48 = self.module_50(output_module_48)
        output_module_48 = self.module_51(output_module_48)
        output_module_48 = self.module_52(input=output_module_48, other=output_module_44, alpha=1)
        output_module_53 = self.module_53(output_module_48)
        output_module_53 = self.module_54(output_module_53)
        output_module_53 = self.module_55(output_module_53)
        output_module_53 = self.module_56(output_module_53)
        output_module_53 = self.module_57(input=output_module_53, other=output_module_48, alpha=1)
        output_module_58 = self.module_58(output_module_53)
        output_module_58 = self.module_59(output_module_58)
        output_module_58 = self.module_60(output_module_58)
        output_module_58 = self.module_61(output_module_58)
        output_module_58 = self.module_62(input=output_module_58, other=output_module_53, alpha=1)
        output_module_58 = self.module_63(dim=1, tensors=[output_module_58,output_module_46])
        output_module_58 = self.module_64(output_module_58)
        output_module_58 = self.module_65(output_module_58)
        output_module_66 = self.module_66(output_module_58)
        output_module_66 = self.module_67(output_module_66)
        output_module_66 = self.module_68(output_module_66)
        output_module_66 = self.module_69(output_module_66)
        output_module_70 = self.module_70(output_module_66)
        output_module_71 = self.module_71(output_module_66)
        output_module_72 = self.module_72(output_module_66)
        output_module_73 = self.module_73(dim=1, tensors=[output_module_66,output_module_70,output_module_71,output_module_72])
        output_module_73 = self.module_74(output_module_73)
        output_module_73 = self.module_75(output_module_73)
        output_module_76 = self.module_76(output_module_73)
        output_module_76 = self.module_77(output_module_76)
        output_module_78 = self.module_78(output_module_73)
        output_module_78 = self.module_79(output_module_78)
        output_module_76 = self.module_80(output_module_76)
        output_module_76 = self.module_81(output_module_76)
        output_module_76 = self.module_82(output_module_76)
        output_module_76 = self.module_83(output_module_76)
        output_module_76 = self.module_84(dim=1, tensors=[output_module_76,output_module_78])
        output_module_76 = self.module_85(output_module_76)
        output_module_76 = self.module_86(output_module_76)
        output_module_76 = self.module_87(output_module_76)
        output_module_76 = self.module_88(output_module_76)
        output_module_89 = self.module_89(output_module_76)
        output_module_89 = self.module_90(output_module_89)
        output_module_89 = self.module_91(dim=1, tensors=[output_module_89,output_module_58])
        output_module_92 = self.module_92(output_module_89)
        output_module_92 = self.module_93(output_module_92)
        output_module_94 = self.module_94(output_module_89)
        output_module_94 = self.module_95(output_module_94)
        output_module_92 = self.module_96(output_module_92)
        output_module_92 = self.module_97(output_module_92)
        output_module_92 = self.module_98(output_module_92)
        output_module_92 = self.module_99(output_module_92)
        output_module_92 = self.module_100(dim=1, tensors=[output_module_92,output_module_94])
        output_module_92 = self.module_101(output_module_92)
        output_module_92 = self.module_102(output_module_92)
        output_module_92 = self.module_103(output_module_92)
        output_module_92 = self.module_104(output_module_92)
        output_module_105 = self.module_105(output_module_92)
        output_module_105 = self.module_106(output_module_105)
        output_module_105 = self.module_107(dim=1, tensors=[output_module_105,output_module_34])
        output_module_108 = self.module_108(output_module_105)
        output_module_108 = self.module_109(output_module_108)
        output_module_110 = self.module_110(output_module_105)
        output_module_110 = self.module_111(output_module_110)
        output_module_108 = self.module_112(output_module_108)
        output_module_108 = self.module_113(output_module_108)
        output_module_108 = self.module_114(output_module_108)
        output_module_108 = self.module_115(output_module_108)
        output_module_108 = self.module_116(dim=1, tensors=[output_module_108,output_module_110])
        output_module_108 = self.module_117(output_module_108)
        output_module_108 = self.module_118(output_module_108)
        output_module_119 = self.module_119(output_module_108)
        output_module_119 = self.module_120(output_module_119)
        output_module_119 = self.module_121(dim=1, tensors=[output_module_119,output_module_92])
        output_module_122 = self.module_122(output_module_119)
        output_module_122 = self.module_123(output_module_122)
        output_module_124 = self.module_124(output_module_119)
        output_module_124 = self.module_125(output_module_124)
        output_module_122 = self.module_126(output_module_122)
        output_module_122 = self.module_127(output_module_122)
        output_module_122 = self.module_128(output_module_122)
        output_module_122 = self.module_129(output_module_122)
        output_module_122 = self.module_130(dim=1, tensors=[output_module_122,output_module_124])
        output_module_122 = self.module_131(output_module_122)
        output_module_122 = self.module_132(output_module_122)
        output_module_133 = self.module_133(output_module_122)
        output_module_133 = self.module_134(output_module_133)
        output_module_133 = self.module_135(dim=1, tensors=[output_module_133,output_module_76])
        output_module_136 = self.module_136(output_module_133)
        output_module_136 = self.module_137(output_module_136)
        output_module_138 = self.module_138(output_module_133)
        output_module_138 = self.module_139(output_module_138)
        output_module_136 = self.module_140(output_module_136)
        output_module_136 = self.module_141(output_module_136)
        output_module_136 = self.module_142(output_module_136)
        output_module_136 = self.module_143(output_module_136)
        output_module_136 = self.module_144(dim=1, tensors=[output_module_136,output_module_138])
        output_module_136 = self.module_145(output_module_136)
        output_module_136 = self.module_146(output_module_136)
        output_module_147 = self.module_147(output_module_108)
        output_module_147 = self.module_148(output_module_147)
        output_module_149 = self.module_149(output_module_147)
        output_module_149 = self.module_150(output_module_149)
        output_module_149 = self.module_151(output_module_149)
        output_module_149 = self.module_152(output_module_149)
        output_module_149 = self.module_153(output_module_149)
        output_module_154 = self.module_154(output_module_147)
        output_module_154 = self.module_155(output_module_154)
        output_module_154 = self.module_156(output_module_154)
        output_module_154 = self.module_157(output_module_154)
        output_module_158 = self.module_158(output_module_154)
        output_module_159 = self.module_159(output_module_154)
        output_module_158 = self.module_160(dim=1, tensors=[output_module_158,output_module_159,output_module_149])
        output_module_161 = self.module_161(output_module_122)
        output_module_161 = self.module_162(output_module_161)
        output_module_163 = self.module_163(output_module_161)
        output_module_163 = self.module_164(output_module_163)
        output_module_163 = self.module_165(output_module_163)
        output_module_163 = self.module_166(output_module_163)
        output_module_163 = self.module_167(output_module_163)
        output_module_168 = self.module_168(output_module_161)
        output_module_168 = self.module_169(output_module_168)
        output_module_168 = self.module_170(output_module_168)
        output_module_168 = self.module_171(output_module_168)
        output_module_172 = self.module_172(output_module_168)
        output_module_173 = self.module_173(output_module_168)
        output_module_172 = self.module_174(dim=1, tensors=[output_module_172,output_module_173,output_module_163])
        output_module_136 = self.module_175(output_module_136)
        output_module_136 = self.module_176(output_module_136)
        output_module_177 = self.module_177(output_module_136)
        output_module_177 = self.module_178(output_module_177)
        output_module_177 = self.module_179(output_module_177)
        output_module_177 = self.module_180(output_module_177)
        output_module_177 = self.module_181(output_module_177)
        output_module_182 = self.module_182(output_module_136)
        output_module_182 = self.module_183(output_module_182)
        output_module_182 = self.module_184(output_module_182)
        output_module_182 = self.module_185(output_module_182)
        output_module_186 = self.module_186(output_module_182)
        output_module_187 = self.module_187(output_module_182)
        output_module_186 = self.module_188(dim=1, tensors=[output_module_186,output_module_187,output_module_177])
        output_module_158 = self.module_189(input=output_module_158)
        output_module_172 = self.module_190(input=output_module_172)
        output_module_186 = self.module_191(input=output_module_186)
        return output_module_158,output_module_172,output_module_186
