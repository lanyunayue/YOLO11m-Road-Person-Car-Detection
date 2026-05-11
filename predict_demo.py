from ultralytics import YOLO

# 本仓库不上传 best.pt 权重文件
# 如需本地运行，请将训练好的 best.pt 放到项目根目录下

model = YOLO("best.pt")

results = model.predict(
    source="demo_images",
    imgsz=800,
    conf=0.4,
    save=True
)

print("Prediction finished.")
