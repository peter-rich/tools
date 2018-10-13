# -*- coding: utf-8 -*-
import os, os.path,shutil
import sys
import shutil


dir = os.path.abspath("CelebA_nocrop")
dir_src = dir + '/images_resize/'
dir_1=dir + '/' + sys.argv[1] + "/1"
dir_neg1=dir + '/' + sys.argv[1] + "/neg1"
os.makedirs(dir_1)
os.makedirs(dir_neg1)

class_id=0
with open("list_attr_celeba.txt") as fp:
	for i, line in enumerate(fp):
		if i==1:
			j=0
			label = ""
			for k  in range(0,466):
        			if line[k] != " ":
					label = label + line[k]
				else:
					if label == sys.argv[1]:
						class_id = j	
					j=j+1
					label = "" 		
		elif i >= 2 and i <= int(sys.argv[2])+1:
			print i
                        j=0
                        label = ""
			p = ""
                        for k  in range(0,len(line)):	
                                if line[k] != " " and line[k] != '\r':
                                        label = label + line[k]
                                else:   
                                        if label == "1" or label == "-1":
						if j == class_id:
                                        		if label == "1":
								shutil.copy( dir_src+p, dir_1) 
							else:
								shutil.copy( dir_src+p, dir_neg1)
						j = j + 1 
  
					elif j == 0:
						p = label
                                        label = ""
print ("Class is -> " +str(class_id))
#
#shutil.copyfile(src, dst)

