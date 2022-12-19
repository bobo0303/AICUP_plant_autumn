import numpy as np
import cv2
import os, random, shutil

path = 'D:/plant/sugarcane/'
path2 = 'D:/plant/BUFFER/'
files = os.listdir(path)
n=0

for i in files: #因為資料夾裡面的檔案都要重新更換名稱
    image = cv2.imread(path + i)
    #cv2.imshow("before", image)
    z = str(n + 1).zfill(8)

    #image2 = cv2.flip(image, 1) # 左右水平翻轉
    #image2 = cv2.flip(image, -1) # 上下左右翻轉
    image2 = np.rot90(image)  # 90度
    #cv2.imshow("after", image2)
    #cv2.waitKey(0)
    n+=1
    cv2.imwrite(path2+'enhancement_sugarcane_90_'+z+'.jpg', image2)
print("1GGGGGGGGGGGGGGGGGGGGGGGGGG")


