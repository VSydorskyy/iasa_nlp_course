# IASA NLP Course

# Setup Working Environment  

## Pre-requirements 

- conda 4.12.0 (later versions may also work) - [Installation](https://docs.anaconda.com/anaconda/install/index.html)
- VS Code - [Ubuntu Installation](https://code.visualstudio.com/docs/setup/linux)
- (Optional) CUDA Version: 11.4; Driver Version: 470.129.06 - [Installation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

## Setup environment 

### Poetry (Recommended)

1. Install Poetry using [Poetry full guide](https://python-poetry.org/docs/#installation).
    - Important: Check if it is working using `poetry --version`
2. Run command to keep your `.venv` folder right in your project: `poetry config virtualenvs.in-project true`
3. `poetry shell`
    - Important: If you have `conda` and 2 environments were activated: `conda deactivate`
4. `poetry install --no-root`

In order to activate environment on the next use. Important: you should be inside your project

`poetry shell`

### Conda

If you have CUDA
```bash
conda env create -f environment_gpu.yaml
```
Otherwise
```bash
conda env create -f environment.yaml
```

In order to activate environment 

```bash
conda activate iasa_nlp_env
```

# Start Jupyter

You may use any port 
```bash
jupyter lab --port 7766
```

# Content 

1. [x] Структура та структурні елементи постановки ML задачі. Формалізація бізнес задач. Основні задачі й методи в сфері Обробки природних мов - Volodymyr 
2. [x] Представлення природніх мов в машинному вигляді. Класичні та нейронні алгоритми векторизації. Класичні ML підходи в NLP. - Vladyslav 
3. [x] Основні метрики в NLP (обробка природніх мов). Побудова оцінки підходів і моделей в NLP - валідація. - Anton
4. [x] Підходи з використанням архітектур RNN/GRU/LSTM. - Volodymyr
5. [x] Підходи з використанням архітектури Transformer. - Anton  
6. [x] Генеративні задачі: машинний переклад, сумаризація тексту, умовна та безумовна текстова генерація, розгляд GPT архітектури - Vladyslav
7. [x] Задача кластеризації. Задача моделювання тем. - Volodymyr
8. [x] MLOps - розгортання моделей. - Anton 
# Use Kaggle or Colab for computations

## Kaggle 

1. Create [Kaggle](https://www.kaggle.com/) account 
2. Create [Notebook](https://www.kaggle.com/code)
3. Explore [docs](https://www.kaggle.com/docs/notebooks) and find out how 
    - Add Kaggle dataset to notebook 
    - Turn on GPU 

## Colab 

1. Create Notebook in [Colab](https://colab.research.google.com/)
2. Enable GPU 
3. Add Kaggle dataset to Colab - https://www.geeksforgeeks.org/how-to-import-kaggle-datasets-directly-into-google-colab/

# Data

- For most of lectures you will need datasets from Kaggle. [Prepare in advance](#how-to-use-kaggle-datasets)
    - CommonLit - Evaluate Student Summaries dataset API command: `kaggle competitions download -c commonlit-evaluate-student-summaries`
    - Natural Language Processing with Disaster Tweets dataset API command: `kaggle competitions download -c nlp-getting-started`
    - Mantis Analytics Location Detection dataset: `kaggle datasets download -d vladimirsydor/mantis-analytics-location-detection`
    - Dataset for Topic Modelling: `https://drive.google.com/drive/folders/1jwh225T0DIEN4A1wMZ8-dVJX-2Tsovqf?usp=sharing`
- We recommend to create `data` folder in the course root directory and put all datasets there. So you might have next structure

```
data/
    nlp_getting_started/
        train.csv
        test.csv
        ...
    ...
Lecture_1/
...
```

## How to use Kaggle datasets

1. Create [Kaggle](https://www.kaggle.com/) account
2. Proceed [with Installation & Authentication](https://www.kaggle.com/docs/api#getting-started-installation-&-authentication)
3. Don't forget to join a competition and accept its rules on a Kaggle website.
4. Download dataset with API command 
