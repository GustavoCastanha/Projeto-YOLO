from ultralytics import YOLO

def main():
    model = YOLO("yolo11s.pt")

    model.train(
        data="../dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        device="cpu"
    )

if __name__ == "__main__":
    main()