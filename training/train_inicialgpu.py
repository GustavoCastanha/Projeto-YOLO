#Treinamento usando GPU, mais rapido, recomendado para maiores qtds de fotos.

from ultralytics import YOLO

def main():
    #model = YOLO("runs/detect/train-x/weights/best.pt")
    model = YOLO("yolo11s.pt")

    model.train(
        data="dataset/data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        cache=True,
        device=0 
    )

if __name__ == "__main__":
    main()
     