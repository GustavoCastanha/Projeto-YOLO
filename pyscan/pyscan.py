import cv2
import time 
import logging
import os
import json
from ultralytics import YOLO 
 
MODEL_PATH = r"C:\Users\rosan\Desktop\ProjetoIA\models\best\best.pt"
MATERIALS_PATH = os.path.join(os.path.dirname(__file__), "MATERIALS.json")
CAMERA_SOURCE = 0
CONFIDENCE_THRESHOLD = 0.65
RECONNECT_DELAY = 5

 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
 
def load_materials():
    with open(MATERIALS_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    items = data.get("MATERIALS", [])

    return {
        item["nome"].replace(" ", "_").upper(): item["codigo"]
        for item in items
    }


def draw_ui(frame, label, confidence, codigo=None):
    width = frame.shape[1]
 
    cv2.rectangle(frame, (0, 0), (width, 100), (40, 40, 40), -1)
 
    if label:
        cv2.putText(
            frame,
            f"MATERIAL: {label}",
            (20, 40),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (0, 255, 0),
            2
        )
        cv2.putText(
            frame,
            f"CODIGO: {codigo}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )
        cv2.putText(
            frame,
            f"CONF: {confidence:.0%}",
            (width - 180, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )
    else:
        cv2.putText(
            frame,
            "AGUARDANDO MATERIAL...",
            (20, 50),
            cv2.FONT_HERSHEY_DUPLEX,
            1,
            (200, 200, 200),
            2
        )
 
 
def main():
 
    if not os.path.exists(MODEL_PATH):
        logging.error("Modelo nao encontrado.")
        return

    materials = load_materials()
 
    logging.info("Carregando modelo...")
    model = YOLO(MODEL_PATH)
 
    logging.info("Inicializando camera...")
    
    cap = cv2.VideoCapture(CAMERA_SOURCE)
    #cap = cv2.VideoCapture(2)
    if not cap.isOpened():
        logging.error("Falha ao abrir camera.")
        return
 
    while True:
 
        ret, frame = cap.read()
 
        if not ret:
            logging.warning("Falha na camera. Tentando reconectar...")
            cap.release()
            time.sleep(RECONNECT_DELAY)
            #cap = cv2.VideoCapture(2)
            cap = cv2.VideoCapture(CAMERA_SOURCE)
            continue
 
        best_label = None
        best_conf = 0
        codigo = None
 
        try:
            results = model(frame, stream=True, verbose=False)
 
            for r in results:
                for box in r.boxes:
                    conf = float(box.conf[0])
 
                    if conf > CONFIDENCE_THRESHOLD and conf > best_conf:
                        best_conf = conf
 
                        cls_id = int(box.cls[0])
                        best_label = model.names[cls_id].replace(" ", "_").upper()
                        codigo = materials.get(best_label, "9999")
 
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
 
            draw_ui(frame, best_label, best_conf, codigo)
 
        except Exception as e:
            logging.error(f"Erro no processamento: {e}")
 
        cv2.imshow("Classificador de Materiais", frame)
 
        if cv2.waitKey(1) & 0xFF == 27:
            break
 
    cap.release()
 
    cv2.destroyAllWindows()
 
 
if __name__ == "__main__":
    main()
 
#teste
