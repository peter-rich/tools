# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
dir = os.path.abspath("CelebA_nocrop")
dir_src = dir + '/images'
dir_res=dir + '/images_resize'
os.makedirs(dir_res)


filesize = 32
i=0
for filename in os.listdir(dir_src):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".jpg"):
	image=cv2.imread(dir_src+'/'+filename)
	res=cv2.resize(image,(filesize,filesize),interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(dir_res+'/'+filename,res)

