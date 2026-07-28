import cv2
import time
import logging
import os
import json
import unicodedata
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


def normalizar_nome(nome):
    nome = unicodedata.normalize("NFKD", nome)
    nome = nome.encode("ASCII", "ignore").decode("ASCII")
    return nome.replace(" ", "_").upper()


def load_materials():
    with open(MATERIALS_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    items = data.get("MATERIALS", [])

    return {
        normalizar_nome(item["nome"]): {
            "codigo": item["codigo"],
            "localizacao": item.get("localizacao", "N/A")
        }
        for item in items
    }


def draw_ui(frame, label, confidence, codigo, localizacao=None):
    width = frame.shape[1]

    cv2.rectangle(frame, (0, 0), (width, 100), (166, 86, 0), -1)

    if label:
        cv2.putText(
            frame,
            f"MATERIAL: {label}",
            (20, 40),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"COD: {codigo}",
            (20, 80),
            cv2.FONT_HERSHEY_DUPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        ''' cv2.putText(   APENAS PARA MOSTAR A CONFIANÇA.
            frame,
            f"CONF: {confidence:.0%}",
            (width - 180, 40),
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            (255, 255, 255),
            2
        )''' 
        cv2.putText(
            frame,
            f"POS:{localizacao}",
            (width - 180, 80),
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            (255, 255, 255),
            2
        )

    else:
        cv2.putText(
            frame,
            "AGUARDANDO MATERIAL...",
            (20, 50),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255, 255, 255),
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

    if not cap.isOpened():
        logging.error("Falha ao abrir camera.")
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            logging.warning("Falha na camera. Tentando reconectar...")
            cap.release()
            time.sleep(RECONNECT_DELAY)
            cap = cv2.VideoCapture(CAMERA_SOURCE)
            continue

        best_label = None
        best_conf = 0
        codigo = None
        localizacao = None

        try:
            results = model(frame, stream=True, verbose=False)

            for r in results:
                for box in r.boxes:

                    conf = float(box.conf[0])

                    if conf > CONFIDENCE_THRESHOLD and conf > best_conf:

                        best_conf = conf

                        cls_id = int(box.cls[0])
                        best_label = normalizar_nome(model.names[cls_id])

                        material_info = materials.get(best_label, {"codigo": "9999", "localizacao": "N/A"})
                        codigo = material_info["codigo"]
                        localizacao = material_info["localizacao"]

                        x1, y1, x2, y2 = map(int, box.xyxy[0])

                        cv2.rectangle(
                            frame,
                            (x1, y1),
                            (x2, y2),
                            (0, 255, 0),
                            3
                               
                        )

            draw_ui(frame, best_label, best_conf, codigo, localizacao)

        except Exception as e:
            logging.error(f"Erro no processamento: {e}")

        cv2.namedWindow("Classificador de Materiais", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(
            "Classificador de Materiais",
            cv2.WND_PROP_FULLSCREEN,
             cv2.WINDOW_FULLSCREEN
)

        cv2.imshow("Classificador de Materiais", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()