# YOLO11m Road Person-Car Detection

## 项目介绍

真实道路感知的难点，不只是白天清晰画面下能否识别目标，而是模型在夜间低照度、强光逆光、雨天反光、运动模糊、人车遮挡和远距离小目标等复杂条件下，能否稳定识别行人与车辆。

在智能驾驶辅助、智慧交通监控、园区安防和车载记录仪升级等场景中，person 与 car 是最核心、最直接影响安全判断的两类目标。一旦出现行人漏检、车辆误检或目标框定位不稳定，就可能带来事故风险、责任纠纷、人工复核成本和管理效率下降。

本项目围绕复杂道路场景中的人车识别问题，基于 YOLO11m 构建 person / car 双类别目标检测模型，完成从数据重构、模型训练、指标评估、误检漏检分析到复杂场景验证的完整实验流程。

## 技术栈

- Python
- YOLO11m
- Ultralytics
- OpenCV
- PyTorch

## 数据集与任务定义

- 数据来源：BDD100K 行车视角数据
- 检测类别：person / car
- 输入尺寸：imgsz=800
- 类别处理：
  - pedestrian + rider 合并为 person
  - car 保留
  - bicycle / motorcycle 不纳入最终训练类别

## 方法流程

本项目主要围绕复杂道路场景下的 person / car 检测任务展开，核心流程如下：

1. 数据整理与类别重构  
   将 BDD100K 中的 pedestrian / rider 合并为 person，保留 car 类别，构建 person / car 双类别检测任务。

2. 模型训练与验证  
   基于 YOLO11m 进行目标检测训练，使用 imgsz=800 提升远距离目标与复杂场景下的检测表现。

3. 指标评估与结果分析  
   使用 Precision、Recall、mAP50、mAP50-95 等指标评估模型表现，并整理 PR 曲线、F1 曲线、混淆矩阵和训练收敛曲线。

4. 复杂视觉场景测试  
   针对夜间低照度、雨天反光、强光逆光、遮挡密集、远距离小目标等场景进行检测效果分析。

5. 误检漏检分析  
   对复杂场景中的漏检、误检和低置信度目标进行分析，为后续困难样本回流和鲁棒性优化提供依据。

## 实验结果

| 指标 | 结果 |
|---|---|
| Precision | 81.9% |
| Recall | 68.0% |
| mAP50 | 76.4% |
| mAP50-95 | 43.9% |
| car mAP50 | 81.3% |
| person mAP50 | 71.5% |

## 效果展示

仓库中包含以下可视化结果：

- PR_curve.png
- F1_curve.png
- confusion_matrix.png
- results.png
- 正常道路检测效果图
- 夜间低照度检测效果图
- 雨天道路检测效果图
- 强逆光检测效果图
- 远距离小目标检测效果图
- 遮挡密集场景检测效果图

## 项目结构

```text
YOLO11m-Road-Person-Car-Detection/
│
├── README.md
├── requirements.txt
├── predict_demo.py
├── train_command.md
│
├── results/
│   ├── PR_curve.png
│   ├── F1_curve.png
│   ├── confusion_matrix.png
│   └── results.png
│
├── demo_images/
│   ├── normal_road.jpg
│   ├── night.jpg
│   ├── rain.jpg
│   ├── backlight.jpg
│   └── small_object.jpg
│
└── docs/
    └── project_summary.pdf
```

## 推理示例

```python
from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(
    source="demo_images",
    imgsz=800,
    conf=0.4,
    save=True
)

print("Prediction finished.")
```

## 运行方法

安装依赖：

```bash
pip install -r requirements.txt
```

运行推理脚本：

```bash
python predict_demo.py
```

## 说明

由于 BDD100K 数据集版权和模型权重文件体积限制，本仓库不包含原始数据集、完整训练数据和模型权重文件，仅用于展示项目流程、实验结果、可视化图像和推理脚本。

