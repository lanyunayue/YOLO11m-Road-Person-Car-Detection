# YOLOv8 Small Object Detection Optimization

## 项目介绍

本项目针对自动驾驶中的小目标检测问题，基于 YOLO11m 模型进行优化，提高检测精度与召回率。

## 技术栈

* Python
* YOLOv8
* OpenCV

## 方法

* 提高输入分辨率（640 → 1024）
* 数据增强（Mosaic / MixUp）
* 参数调优

## 实验结果

| 方法       | mAP  | Recall |
| -------- | ---- | ------ |
| Baseline | 0.62 | 0.58   |
| 优化后      | 0.71 | 0.66   |

## 效果展示


## 运行方法

pip install -r requirements.txt
python main.py
