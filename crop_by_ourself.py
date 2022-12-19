import cv2,os
from pylab import *

origonal_path = 'E:/AIcup_plant_33_autumn/'     # 原始圖片資料夾 (這三個都不需包含類別)
croped_path = 'E:/AIcup_plant_33_autumn_croped/'    # 剪裁後圖片資料夾
checked_iamgefile = 'E:/checked_imagefile/'     # 檢查後重新剪裁圖片暫存資料夾

now_class = 'others/'    #你要檢查的類別 EX. 'betel/' 記得尾巴加斜線 /

if not os.path.isdir(checked_iamgefile + now_class):
    os.mkdir(checked_iamgefile + now_class)

path_list = os.listdir(origonal_path+now_class)
# print(path_list)
_ = 0
resume_number = 796   # 如果你中斷了那就從你結束第幾個開始繼續

def show_xy(event,x,y,flags,param):
    global dot1, dot2, origonal_img, img2, n
    if flags == 1:      #起始點 (滑鼠左點按下)
        if event == 1:
            dot1 = [x, y]
            # print(dot1)
        if event == 0:  #滑動位置框範圍 (左建按著移動)
            img2 = origonal_img.copy()
            dot2 = [x, y]
            cv2.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            cv2.imshow(n, img2)
            # print(dot2)
    if flags == 2:
        if event == 2 and dot1 != [] and dot2 != []:  # 查看剪裁樣式 (右鍵按下)
            crop_img = origonal_img[dot1[1]:dot2[1], dot1[0]:dot2[0]]
            crop_img = cv2.resize(crop_img, (224, 224), interpolation=cv2.INTER_AREA)
            cv2.imshow(n+'_new_crop', crop_img)
            cv2.moveWindow(n + '_new_crop', 0, 270)  # 調整 croped_img 顯示位置 可以自己調
        if event == 8:  # 直接刪除不要的剪裁圖片/把要刪除的圖片寫在txt中 (看你在哪用自己調整) (右鍵連點兩下)
            os.remove(croped_path+now_class+n)
            print('removed: ' + croped_path + now_class + n)      # 直接刪除 croped的圖片
            # f.write(n+'\n')
            # print('listed: ' + checked_iamgefile + now_class + n)
            # f.close()
    if flags == 4:
        if event == 9:  # 存檔剪裁好的圖片在 checked_iamgefile 中暫存 (中鍵連點兩下)
            crop_img = origonal_img[dot1[1]:dot2[1], dot1[0]:dot2[0]]
            crop_img = cv2.resize(crop_img, (224, 224), interpolation=cv2.INTER_AREA)
            cv2.imwrite(checked_iamgefile + now_class + n, crop_img)
            print('save to: ' + checked_iamgefile + now_class + n)

for n in path_list:
    _+=1
    if _ <= resume_number:  # 如果段在 100 那就寫99 那會從100開始
        continue
    origonal_img = None
    croped_img = None
    origonal_img = cv2.imread(origonal_path+now_class+n)

    dot1 = []                          # 記錄第一個座標
    dot2 = []                          # 記錄第二個座標

    if os.path.isfile(croped_path+now_class+n):
        croped_img = cv2.imread(croped_path + now_class + n)
    else:    # 跳過 croped 被刪掉的圖
        continue

    if origonal_img.shape[1]<2560 and origonal_img.shape[0]<1440:     #判斷圖片大小會不會超過螢幕可顯示範圍 (正常尺寸 1920*1082 自己改)
        print(str(_)+' '+str(origonal_img.shape))
    elif origonal_img.shape[1]>2560 or origonal_img.shape[0]>1440:    #超過螢幕解析度就強只縮小圖片不然會看不到完整圖 (正常解析度是1920*1080 自己改)
        origonal_img2 = cv2.resize(origonal_img, (round(origonal_img.shape[1]/2), round(origonal_img.shape[0]/2)), interpolation=cv2.INTER_AREA)
        if origonal_img2.shape[1] > 2560 or origonal_img2.shape[0] > 1440:  # 二次檢查
            origonal_img2 = cv2.resize(origonal_img2,(round(origonal_img2.shape[1] / 2), round(origonal_img2.shape[0] / 2)),interpolation=cv2.INTER_AREA)
            print(str(_)+' '+str(origonal_img.shape) + '>>' + str(origonal_img2.shape))
            origonal_img=origonal_img2
        else:
            print(str(_)+' '+str(origonal_img.shape) + '>>' + str(origonal_img2.shape))
            origonal_img = origonal_img2

    cv2.imshow(n, origonal_img)
    cv2.moveWindow(n,380,0)     # 調整 origonal_img 顯示位置 可以自己調
    cv2.imshow(n+'_croped_img', croped_img)
    cv2.moveWindow(n+'_croped_img',0,0)  # 調整 croped_img 顯示位置 可以自己調
    cv2.setMouseCallback(n, show_xy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''

左上往右下框

'''