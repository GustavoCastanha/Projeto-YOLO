# Projeto-YOLOV11 Python 3.14

# IA para Classificação de Materiais 

Este projeto utiliza **Inteligência Artificial com YOLO (Ultralytics)** para **detectar e classificar matérias/produtos** a partir de imagens ou vídeo em tempo real, usando câmera USB ou IP (RTSP).

O foco é uso **industrial/profissional**, com estrutura organizada para facilitar manutenção, re-treinamento e entrega ao cliente.

---

## 🎯 Objetivo

* Detectar automaticamente matérias/produtos
* Classificar cada matéria corretamente
* Rodar em tempo real com câmera
* Permitir re-treinamento quando surgirem novas matérias

---

## 🗂️ Estrutura do Projeto

```
ProjetoIA/
├── dataset/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│   └── data.yaml
│
├── training/
│   └── train.py
│
├── inference/
│   └── detect.py
│
├── models/
│   └── best.pt
│
└── README.md
```

---

## 📁 Dataset

* `images/train` → imagens usadas para treinar a IA
* `images/val` → imagens usadas apenas para validação
* `labels/train` → labels das imagens de treino
* `labels/val` → labels das imagens de validação

As imagens e labels devem ter **o mesmo nome**:

```
img001.jpg → img001.txt
```

---

## 🏷️ Classes

As classes são definidas no arquivo `data.yaml`.

Exemplo:

```yaml
names:
  0: materia_A
  1: materia_B
```

⚠️ A ordem e os números das classes **não devem ser alterados após o início do projeto**.

---

## 🧠 Treinamento da IA

O treinamento é feito com o arquivo:

```
training/train.py
```

Este script:

* Lê o dataset
* Treina o modelo YOLO
* Gera um modelo final (`best.pt`)

Após o treino, o modelo deve ser copiado para:

```
models/best.pt
```

O treinamento só precisa ser executado quando:

* O projeto iniciar
* Novas matérias forem adicionadas

---

## 🎥 Execução (Produção)

A execução em tempo real é feita com:

```
inference/detect.py
```

Este script:

* Carrega o modelo treinado
* Abre a câmera (USB ou IP)
* Detecta e classifica as matérias em tempo real

⚠️ Este é o código usado em produção.

---

## 🔁 Atualização de Novas Matérias

Fluxo correto:

1. Tirar novas fotos
2. Rotular as imagens
3. Adicionar ao dataset existente
4. Rodar novamente `train.py`
5. Substituir o arquivo `models/best.pt`

O código de execução **não precisa ser alterado**.

---

## 🧩 Tecnologias Utilizadas

* Python 3.13
* YOLO (Ultralytics)
* OpenCV
* VS Code
* GPU NVIDIA (GTX 1650 ou superior recomendada)

---

## 📌 Observações Importantes

* Manter iluminação e câmera padronizadas melhora muito a precisão
* Não misturar datasets com iluminação muito diferente
* Sempre validar o modelo antes de usar em produção

---

## 👤 Autor

Projeto desenvolvido por **Gustavo Castanha**.

---

## ✅ Status do Projeto

🚧 Em desenvolvimento / treinamento inicial
