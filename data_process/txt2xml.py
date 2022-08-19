from __future__ import annotations
from xml.dom import minidom, Node
import string
import os
import os.path as osp
from tqdm import tqdm

txt_path = fr"/media/sm/data2/luojie/centernet_data/COCO/train_val_txt"
save_path = fr"/media/sm/data2/luojie/centernet_data/COCO/train_val_xml"


txt_file_list = os.listdir(txt_path)
label_name_dict = {'10' : 'vehicle', '11' : 'pedestrain', '20' : 'background'}
count = 0

for file in tqdm(txt_file_list):
	name = file.replace('txt', 'png')
	w, h, d = 1280, 720, 3
	
	doc = minidom.Document()

	annotation = doc.createElement('annotation')
	doc.appendChild(annotation)

	folder = doc.createElement('folder')
	folder.appendChild(doc.createTextNode("JEPGImages"))
	annotation.appendChild(folder)

	filename = doc.createElement('filename')
	filename.appendChild(doc.createTextNode(name))
	annotation.appendChild(filename)

	size = doc.createElement('size')
	width = doc.createElement('width')
	width.appendChild(doc.createTextNode(str(w)))
	size.appendChild(width)
	height = doc.createElement('height')
	height.appendChild(doc.createTextNode(str(h))) 
	size.appendChild(height)
	depth = doc.createElement('depth')
	depth.appendChild(doc.createTextNode(str(d))) 
	size.appendChild(depth)
	annotation.appendChild(size)

	segmented = doc.createElement('segmented')
	segmented.appendChild(doc.createTextNode("0")) 
	annotation.appendChild(segmented)

	with open(osp.join(txt_path, file), 'r') as f:
		for info in f.readlines():
			box = info.strip().split(' ')
			object = doc.createElement('object')
			nm = doc.createElement('name')
			nm.appendChild(doc.createTextNode(label_name_dict[box[0]])) 
			object.appendChild(nm)
			pose = doc.createElement('pose')
			pose.appendChild(doc.createTextNode("undefined")) 
			object.appendChild(pose)
			truncated = doc.createElement('truncated')
			truncated.appendChild(doc.createTextNode("0")) 
			object.appendChild(truncated)
			difficult = doc.createElement('difficult')
			difficult.appendChild(doc.createTextNode("0")) 
			object.appendChild(difficult)
			bndbox = doc.createElement('bndbox')
			xmin = doc.createElement('xmin')
			xmin.appendChild(doc.createTextNode(box[1])) 
			bndbox.appendChild(xmin)
			ymin = doc.createElement('ymin')
			ymin.appendChild(doc.createTextNode(box[2])) 
			bndbox.appendChild(ymin)
			xmax = doc.createElement('xmax')
			xmax.appendChild(doc.createTextNode(box[3])) 
			bndbox.appendChild(xmax)
			ymax = doc.createElement('ymax')
			ymax.appendChild(doc.createTextNode(box[4])) 
			bndbox.appendChild(ymax)
			object.appendChild(bndbox)
			annotation.appendChild(object)

	with open(osp.join(save_path, file.replace('txt', 'xml')), 'w') as f:
		f.write(doc.toprettyxml())
	count += 1
	# exit(-1)
print(count)
print("done!")