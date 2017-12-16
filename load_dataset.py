# -*- coding: utf-8 -*-

import cv2
import xml_read

# global parameteres
IMAGE_SIZE = 28
WHOLE_IMAGE_SIZE = 32
CATEGORY_SIZE = []
# use array of class may not be a good idea
# class Training:
#     pass
# training_data = []
train_images = []
train_labels = []
test_images = []
test_labels = []

# resize image to IMAGE_SIZE*IMAGE_SIZE
def resize_image(image,size):
    top=0
    bottom=0
    left=0
    right=0

    h,w,_ = image.shape
    if h<w:
        top = (w-h)//2
        bottom = w-h-top
    else:
        left=(h-w)//2
        right=h-w-left

    # input image should be a gray-scale image
    BLACK = [0,0,0]
    const = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)

    return cv2.resize(const,(size,size))

# recognize the label through traverse
def find_elt_in_array(label,objList):
    i=0
    for l in objList:
        i+=1
        if label == l:
            return i
    return 0

# recognize the label through traverse
def find_elts_in_array(names,objList):
    i=0
    labels = []
    for l in objList:
        i+=1
        if l in names:
            labels.append(i)
    return labels

def load_dataset():
    # for training images and labels
    # training ones are segmentation -- have better recognition accuracy
    objects = xml_read.load_training_from_xml()
    objList = xml_read.get_objList()
    CATEGORY_SIZE.append(len(objList)+1)

    for obj in objects:
        # training_sample = Training()
        newImg = resize_image(obj.Img,IMAGE_SIZE)
        train_images.append(newImg)
        labels = find_elts_in_array(obj.names,objList)
        train_labels.append(labels)

    # for test images and labels
    # test ones are whole images (labels are list instead of a single element)
    trainObjects = xml_read.load_test_from_xml()
    # for obj in trainObjects:
    #     # training_sample = Training()
    #     newImg = resize_image(obj.Img, IMAGE_SIZE)
    #     test_images.append(newImg)
    #     label = find_elt_in_array(obj.name, objList)
    #     test_labels.append(label)
    for obj in trainObjects:
        try:
            newImg = resize_image(obj.Img,IMAGE_SIZE)
            test_images.append(newImg)
            labels = find_elts_in_array(obj.names, objList)
            test_labels.append(labels)
        except:
            print("error observed")

    print("load_dataset load_dataset : length of train images and test labels",len(train_images),len(test_labels))
    return train_images, train_labels, test_images, test_labels

# def cc():
#     CATEGORY_SIZE.append(333)
#     return CATEGORY_SIZE