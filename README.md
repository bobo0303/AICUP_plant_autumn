# AICUP-plant-Autumn (TEAM_2042)
組員: wiwi6166, julian135707, louis52099, 97a4a07, GoofyAhh
Only for AI CUP group and private notes

---
## 農地作物現況調查影像辨識競賽 - 春季賽：AI作物影像判釋
![image](https://imgur.com/lsnkVY5.jpeg)
---

## 文件結構說明

- `python_image_enhancement-main`: 包括水平翻轉與90度旋轉的部分；
- `pytorch-image-models-main`: 主訓練與測試程式參考 timm；
- `crop_by_ourself.py`: 經過自動剪裁後手動重新剪裁與刪除；
- `fake_label_read_csv_class_file.py`: 使用 public dataset 製造 pseudo label；
- `mix_two_dataset.py`: 合併 public 和 private csv檔；
- `vote.py`: 最後投票；
- `requirements.txt`: 完整環境；

## 預訓練與模型載點

- `checkpoints` : 訓練模型"[這裡](https://drive.google.com/drive/u/4/folders/1_YqlrD4gkr5OvOByk1wyxKUIuB6mG8Qg)"有載點雲端；

---


## 使用說明

### 資料處理

### 訓練方法
```
python3 -u train.py \
/home/twsahaj458/efb5/plant_33_new_aug/ \
--model efficientnet_b5 \
--num-classes 33 \
--batch-size 8 \
--epochs 100 \
--vflip 0.5 \
--reprob 0.5 \
--aug-splits 3 \
--aa rand-m9-mstd0.5-inc1 \
--model-ema \
--model-ema-decay 0.9998 \
--pretrained \
--amp \
--mean 0.4033 0.4388 0.3304 \
--std 0.2322 0.2267 0.2441
- ...
```
- `/home/twsahaj458/efb5/plant_33_new_aug/`: 訓練資料夾內需包含`train`與`val`；
- `num-classes`: 設定類別數量；
- `batch-size`: 設定一次迭代batch；
- `epochs`: 訓練次數；
- `pretrained `: 是否使用預訓練；
- `mean/std `: 為資料集平衡設定的mean與std(默認為我們強化過資料集計算值)；


### 測試方法

### 投票方法

---

## Reference

[ilaydaDuratnir/python_image_enhancement](https://github.com/ilaydaDuratnir/python_image_enhancement)

[zheng-yuwei/PyTorch-Image-Classification](https://github.com/zheng-yuwei/PyTorch-Image-Classification)

[d-li14/mobilenetv3.pytorch](https://github.com/d-li14/mobilenetv3.pytorch)

[lukemelas/EfficientNet-PyTorch](https://github.com/lukemelas/EfficientNet-PyTorch)

[zhanghang1989/ResNeSt](https://github.com/zhanghang1989/ResNeSt)

[yizt/Grad-CAM.pytorch](https://github.com/yizt/Grad-CAM.pytorch)

---
## Contact
If you have any question, feel free to contact wiwi61666166@gmail.com

