# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import xml.etree.ElementTree as ET
import os
from cv2 import *
import random

# the path of test folder and relevant images and annotations
testPath='./test/'
imagePath=testPath+'JPEGImages/'
annoPath=testPath+'Annotations/'

# Object class is used to save objects (object name, filename and image)
class Object:
    pass

# read all files
images = os.listdir(imagePath)
annotations = os.listdir(annoPath)
objects = []
TRAINING = int(0.85*len(annotations))
testObjects = []

random.shuffle(annotations)
# convert to root
# def load_training_from_xml():
# # return value: objects (array of class Object)
# # variable of Object:
# # ---- name : the object strategy
# # ---- filename : xml name of file
# # ---- Img : processed image (gray, only include the object w/ 'name')
#     for f in annotations[0:TRAINING]:
#         tree=ET.parse(annoPath+f)
#         root=tree.getroot()
#         for obj in root.findall('object'):
#             # save the object name
#             try:
#                 name = obj.findtext('name')
#
#                 # save the cut image
#                 bndbox = obj.find('bndbox')
#                 xmin = int(bndbox.findtext('xmin'))
#                 ymin = int(bndbox.findtext('ymin'))
#                 xmax = int(bndbox.findtext('xmax'))
#                 ymax = int(bndbox.findtext('ymax'))
#                 img = imread(imagePath + f[0:-4] + ".jpg")
#                 # grayImg = cvtColor(img,COLOR_BGR2GRAY)
#                 cutImg = img[ymin:ymax,xmin:xmax]
#
#                 # save to a class
#                 myObj = Object()
#                 myObj.name = name
#                 myObj.filename = f
#                 myObj.Img = cutImg
#                 objects.append(myObj)
#             except:
#                 print("Oops! Load training image error!")
#     return objects

def load_training_from_xml():
# return value: objects (array of class Object)
# variable of Object:
# ---- name : the object strategy
# ---- filename : xml name of file
# ---- Img : processed image (gray, only include the object w/ 'name')
    for f in annotations[0:TRAINING]:
        tree=ET.parse(annoPath+f)
        root=tree.getroot()

        myObj = Object()
        myObj.names = []
        myObj.filename = f
        myObj.Img = imread(imagePath + f[0:-4] + ".jpg")
        try:

            for obj in root.findall('object'):
                # save the object name

                name = obj.findtext('name')
                myObj.names.append(name)
            objects.append(myObj)
        except:
            print("Oops! Load training image error!")
    return objects

def load_test_from_xml():
    # return value: objects (array of class Object)
    # variable of Object:
    # ---- name : the object strategy
    # ---- filename : xml name of file
    # ---- Img : processed image (gray, only include the object w/ 'name')

    for f in annotations[TRAINING:]:
        tree = ET.parse(annoPath + f)
        root = tree.getroot()

        try:
            myObj = Object()
            myObj.names = []
            myObj.filename = f
            myObj.Img = imread(imagePath + f[0:-4] + ".jpg")
            # grayImg = cvtColor(img,COLOR_BGR2GRAY)

            for obj in root.findall('object'):
                # save the object name
                name = obj.findtext('name')
                myObj.names.append(name)

            testObjects.append(myObj)
        except:
            print("Oops! Load test image error!")
    # print("xml_read load_test : length of test objects is ",len(testObjects))
    return testObjects

# def load_test_from_xml():
#     # return value: objects (array of class Object)
#     # variable of Object:
#     # ---- name : the object strategy
#     # ---- filename : xml name of file
#     # ---- Img : processed image (gray, only include the object w/ 'name')
#
#     for f in annotations[TRAINING:]:
#         tree = ET.parse(annoPath + f)
#         root = tree.getroot()
#         for obj in root.findall('object'):
#             # save the object name
#             name = obj.findtext('name')
#
#             # save the cut image
#             bndbox = obj.find('bndbox')
#             xmin = int(bndbox.findtext('xmin'))
#             ymin = int(bndbox.findtext('ymin'))
#             xmax = int(bndbox.findtext('xmax'))
#             ymax = int(bndbox.findtext('ymax'))
#             img = imread(imagePath + f[0:-4] + ".jpg")
#             grayImg = cvtColor(img, COLOR_BGR2GRAY)
#             cutImg = grayImg[ymin:ymax, xmin:xmax]
#
#             # save to a class
#             myObj = Object()
#             myObj.name = name
#             myObj.filename = f
#             myObj.Img = cutImg
#             testObjects.append(myObj)
#
#     # print("xml_read load_test : length of test objects is ",len(testObjects))
#     return testObjects

# for test: print and show an image
# currObj = objects[0]
# imshow("Test image",currObj.Img)
# waitKey(0)
# for o in objects:
#     print(o.name)
# find all elements have object and save to a tuple
objList = ['person','aeroplane','car','train','boat','bottle','horse','cow','bus']
def get_objList():
    for o in objects:
        names = o.names
        for n in names:
            if n not in objList:
                objList.append(n)

    print(objList)
    return objList

def get_simple_objList():
    return objList
# find all objects whose name is specific like 'person'

# training to the category

if __name__ == '__main__':
    load_training_from_xml()
    print(get_objList())

