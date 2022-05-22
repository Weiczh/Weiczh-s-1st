import io
import pandas as pd
import glob
import os
from shutil import move
from os.path import join
from os import listdir, rmdir
target_folder = 'C:\\Users\\86187\\Documents\\GitHub\\Weiczh-s-1st\\hw2tinyimage\\tiny-imagenet-200\\val\\'
val_dict = {}
with open(target_folder + 'val_annotations.txt', 'r') as f:
    for line in f.readlines():
        split_line = line.split('\t')
        val_dict[split_line[0]] = split_line[1]
paths = glob.glob(target_folder + 'images/*')
paths[0].split('\\')[-1]
for path in paths:
    file = path.split('\\')[-1]
    folder = val_dict[file]
    if not os.path.exists(target_folder + str(folder)):
        os.mkdir(target_folder + str(folder))
for path in paths:
    file = path.split('\\')[-1]
    folder = val_dict[file]
    dest = target_folder + str(folder) + '\\' + str(file)
    move(path, dest)
os.remove(os.path.join(target_folder, 'val_annotations.txt'))
rmdir(os.path.join(target_folder, 'images'))
# 修订样本标签，将val文件夹改写为train相同的格式
