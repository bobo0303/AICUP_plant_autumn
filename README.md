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
- `xxx`: 最後投票；

## 預訓練與模型載點

- `checkpoints` & `pretrained`: 目錄內 `Readme.md` 附有載點雲端；

---


## 使用說明

### 資料處理

### 訓練方法
```
- data
  - train
    - class_0
      - 0.jpg
      - 1.jpg
      - ...
    - class_1
      - ...
    - ..
  - test
    - ...
  - val
    - ...
- dataloader
- ...
```
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

