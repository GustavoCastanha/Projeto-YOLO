# IA para Classificação de Materiais

Sistema de visão computacional desenvolvido em **Python 3.14** utilizando **YOLO11s (Ultralytics)** para detecção e classificação automática de materiais em tempo real.

O projeto foi desenvolvido para aplicações industriais, permitindo identificar materiais por meio de uma câmera USB e consultar automaticamente um banco de dados local (`MATERIALS.json`) para obter o código correspondente ao material detectado.

---

# Objetivo

O objetivo deste projeto é automatizar o processo de identificação de materiais utilizando Inteligência Artificial.

O sistema é capaz de:

- Detectar materiais em tempo real;
- Classificar automaticamente cada material;
- Exibir o nome, código e confiança da detecção;
- Consultar um banco de dados local (`MATERIALS.json`);
- Permitir expansão com novos materiais através de re-treinamento do modelo;
- Operar continuamente utilizando uma câmera fixa.

---

# Estrutura do Projeto

```text
ProjetoIA/
│
├── dataset/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   │
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│   │
│   ├── train.cache
│   ├── val.cache
│   └── data.yaml
│
├── models/
│   └── best/
│       └── best.pt
│
├── app/
│   ├── __pycache__/
│   ├── MATERIALS.json
│   └── pyscan.py
│
├── training/
│
├── README.md
└── ProjetoIA.sln
```

---

# Dataset

O treinamento utiliza a estrutura padrão do YOLO.

```
dataset/
├── images/
│   ├── train/
│   └── val/
│
├── labels/
│   ├── train/
│   └── val/
│
└── data.yaml
```

Cada imagem deve possuir seu respectivo arquivo de anotação (`.txt`).

Exemplo:

```
imagem001.jpg
imagem001.txt
```

Os arquivos `.cache` são gerados automaticamente pelo Ultralytics para acelerar o carregamento do dataset durante o treinamento.

---

# Classes

As classes são definidas no arquivo:

```
dataset/data.yaml
```

Exemplo:

```yaml
names:
  0: vedacao_2
  1: vedacao_3
  2: vedacao_35
```

Após iniciar o treinamento do projeto, recomenda-se manter a ordem das classes para preservar a compatibilidade do modelo treinado.

---

# Modelo Treinado

Após o treinamento é gerado o modelo:

```
models/best/best.pt
```

Este arquivo contém todos os pesos treinados da rede neural e é utilizado pela aplicação para realizar as detecções.

Sempre que um novo treinamento for concluído, basta substituir este arquivo.

---

# Aplicação Principal

A aplicação é executada através do arquivo:

```
app/pyscan.py
```

Durante sua execução o sistema realiza automaticamente:

- Carregamento do modelo YOLO11;
- Inicialização da câmera USB;
- Captura contínua de imagens;
- Detecção dos materiais;
- Classificação dos objetos encontrados;
- Consulta ao banco de dados local;
- Exibição das informações na tela;
- Reconexão automática da câmera em caso de falha.

---

# Banco de Dados Local

O arquivo

```
app/MATERIALS.json
```

funciona como um banco de dados local da aplicação.

Ele relaciona o nome da classe detectada pelo modelo ao código correspondente do material.

Exemplo:

```json
{
    "VEDACAO_2": "903853835",
    "VEDACAO_3": "90824572",
    "VEDACAO_35": "90824573"
}
```

Sempre que um novo material for adicionado ao sistema, este arquivo também deverá ser atualizado.

---

# Fluxo para Inclusão de Novos Materiais

Sempre que um novo material precisar ser reconhecido pelo sistema, siga o fluxo abaixo:

1. Fotografar o novo material;
2. Rotular todas as imagens;
3. Adicionar as imagens ao dataset;
4. Atualizar o arquivo `data.yaml`;
5. Executar um novo treinamento;
6. Substituir o arquivo `models/best/best.pt`;
7. Atualizar o arquivo `MATERIALS.json`.

Dessa forma a aplicação continuará funcionando sem necessidade de alterar o código-fonte.

---

# Tecnologias Utilizadas

- Python 3.13.13
- YOLO11 (Ultralytics)
- OpenCV
- NumPy
- JSON
- Visual Studio Code

---

# Hardware Utilizado

- Computador Windows
- Câmera USB

---

# Requisitos

Instale as dependências do projeto utilizando:

```bash
pip install ultralytics
pip install opencv-python
pip install numpy
```

---

# Boas Práticas

Para obter a melhor precisão do modelo recomenda-se:

- Utilizar iluminação constante;
- Manter a câmera sempre fixa;
- Fotografar todos os materiais na mesma distância;
- Utilizar um fundo padronizado;
- Capturar imagens de diferentes rotações do material;
- Validar o modelo antes de utilizá-lo em produção.

---

# Funcionalidades

Atualmente o sistema possui:

- ✅ Treinamento utilizando YOLO11;
- ✅ Detecção em tempo real;
- ✅ Classificação automática de materiais;
- ✅ Consulta automática ao `MATERIALS.json`;
- ✅ Exibição do nome do material;
- ✅ Exibição do código correspondente;
- ✅ Exibição da confiança da detecção;
- ✅ Reconexão automática da câmera;
- ✅ Estrutura preparada para expansão de novos materiais.

---

# Melhorias Futuras

Funcionalidades planejadas para versões futuras:

- Dashboard para estatísticas;
- Histórico de detecções;
- Banco de dados SQL;
- Exportação de relatórios;
- Interface gráfica dedicada.

---

# Autor

**Gustavo Castanha**

Projeto desenvolvido para classificação automática de materiais utilizando Inteligência Artificial aplicada à Visão Computacional.

---

# Licença

Este projeto é destinado para fins de estudo, pesquisa e aplicações industriais, podendo ser adaptado conforme a necessidade do ambiente de utilização.

---

# Status

🟢 **Em desenvolvimento ativo**

O projeto encontra-se funcional, realizando a classificação automática de materiais em tempo real e preparado para expansão através de novos treinamentos do modelo.
