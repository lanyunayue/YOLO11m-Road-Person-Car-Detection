# 训练与验证命令记录

## 训练命令示例

```bash
yolo detect train model=yolo11m.pt data=data.yaml imgsz=800 epochs=50 batch=8 device=0
```

## 验证命令示例

```bash
yolo detect val model=best.pt data=data.yaml imgsz=800 batch=8 device=0
```

## 推理命令示例

```bash
yolo detect predict model=best.pt source=demo_images imgsz=800 conf=0.4 save=True
```
