import csv, os, time
import numpy as np
import cv2
from pylab import *

class_csv = 'E:/AICUP_plant_33_public_test_dataset/submission_example_public.csv'
crop_csv = 'E:/AICUP_plant_33_public_test_dataset/tag_loccoor_public.csv'


path = 'E:/AICUP_plant_33_public_test_dataset/test_file/'
crop_path = 'E:/AICUP_plant_33_public_test_dataset/test_list/'

path_list = os.listdir(path)
# print(path_list)

w = int(500)
h = int(500)
# 開啟 CSV 檔案
start = time.time()


with open(crop_csv, newline='') as crop_csv_file:
    crop_csv_rows = csv.reader(crop_csv_file)
    for row in crop_csv_rows:
        if row[1] == 'Img':
            continue
        for _ in path_list:
            path_class = path + _
            path_class_list = os.listdir(path_class)
            for n in path_class_list:
                if os.path.isfile(path + _ + '/' + row[1]):
                    print(path + _ + '/' + row[1])
                    img = cv2.imread(path + _ + '/' + row[1])
                    if img.shape[1] > img.shape[0] and (row[2] != str(0) or row[3] != str(0)):
                        img = np.rot90(img)
                    x = int(img.shape[1] / 2)
                    y = int(img.shape[0] / 2)
                    x = x + int(row[2])
                    y = y + int(row[3])
                    x1 = x - w
                    x2 = x + w
                    y1 = y - h
                    y2 = y + h
                    if x1 <= 0:
                        x1 = 0
                    if y1 <= 0:
                        y1 = 0
                    if x2 >= img.shape[1]:
                        x2 = img.shape[1]
                    if y2 >= img.shape[0]:
                        y2 = img.shape[0]
                    crop_img = img[y1:y2, x1:x2]
                    crop_img = cv2.resize(crop_img, (224, 224), interpolation=cv2.INTER_AREA)
                    # crop_img = img

                    class_file = None
                    with open(class_csv, newline='') as class_csv_file:
                        class_csv_rows = csv.reader(class_csv_file)
                        for __ in class_csv_rows:
                            if __[0] == row[1]:
                                if not os.path.isdir(crop_path + __[1]):
                                    os.mkdir(crop_path + __[1])
                                cv2.imwrite(crop_path + __[1] + '/' + __[0], crop_img)
                                print('yes')
                                break
                        break





end = time.time()
print("執行時間：%f 秒" % (end - start))

