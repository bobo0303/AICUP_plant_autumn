import csv, os, time, shutil
import numpy as np
import cv2
from pylab import *

test_public_csv = r'C:\Users\wiwiw\OneDrive\桌面/vote_ensemble_acc_over_87_models_10_conf_0.5_ensemble.csv'


test_public_path = r'E:\plant_33_train_val_test_fixed_croped_up\test_public/'
train_public_path = r'E:\plant_33_train_val_test_fixed_croped_up\train_33_pseudo_label/'
test_public_path_list = os.listdir(test_public_path)


with open(test_public_csv, newline='') as crop_csv_file:
    crop_csv_rows = csv.reader(crop_csv_file)
    for row in crop_csv_rows:
        if row[1] == 'label':
            continue
        for _ in test_public_path_list:
            path_class = test_public_path + _
            path_class_list = os.listdir(path_class)
            for n in path_class_list:
                if n == row[0]:
                    shutil.copy(test_public_path+_+'/'+n, train_public_path+row[1]+'/'+n) #複製
                    # os.remove(train_public_path+_+'/'+n)
                    break

