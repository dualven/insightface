import face_model
import argparse
import cv2
import sys
import numpy as np
import datetime

parser = argparse.ArgumentParser(description='face model test')
# general
parser.add_argument('--image-size', default='112,112', help='')
#parser.add_argument('--model', default='/data/insightface/models/model-r100-ii/model,0', help='path to load model.')
parser.add_argument('--model', default='/data/insightface/recognition/models/r100-arcface-emore/model,1', help='path to load model.')
#parser.add_argument('--ga-model', default='/data/insightface/recognition/models/r100-arcface-emore/model,1', help='path to load model.')
parser.add_argument('--ga-model', default='/data/insightface/models/gamodel-r50/model,0', help='path to load model.')
parser.add_argument('--gpu', default=0, type=int, help='gpu id')
parser.add_argument('--det', default=0, type=int, help='mtcnn option, 1 means using R+O, 0 means detect from begining')
parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
args = parser.parse_args()
time_now = datetime.datetime.now()
model = face_model.FaceModel(args)
time_now2 = datetime.datetime.now()
diff= time_now2 - time_now
print("now the diff is :" )
print(diff.total_seconds())

img = cv2.imread('wx1.jpg')
img = model.get_input(img)
f1 = model.get_feature(img)
time_now3 = datetime.datetime.now()
diff= time_now3 - time_now2
print(diff.total_seconds())

print(f1[0:10])
#print(f1)
gender, age = model.get_ga(img)
print(gender)
print(age)
#sys.exit(0)
img2 = cv2.imread('wx2.jpg')
img2 = model.get_input(img2)
f2 = model.get_feature(img2)
time_now4 = datetime.datetime.now()
diff= time_now4 - time_now3
print(diff.total_seconds())
print(f2[0:10])
dist = np.sum(np.square(f1-f2))
time_now5 = datetime.datetime.now()
diff= time_now5 - time_now4
print(diff.total_seconds())
print(dist)
sim = np.dot(f1, f2.T)
print(sim)
#diff = np.subtract(source_feature, target_feature)
#dist = np.sum(np.square(diff),1)
