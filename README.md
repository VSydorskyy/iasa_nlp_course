# IASA NLP Course

# Setup Working Environment  

## Pre-requirements 

- conda 4.12.0 (later versions may also work) - [Installation](https://docs.anaconda.com/anaconda/install/index.html)
- VS Code - [Ubuntu Installation](https://code.visualstudio.com/docs/setup/linux)
- (Optional) CUDA Version: 11.4; Driver Version: 470.129.06 - [Installation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

## Setup environment 

If you have CUDA
```bash
conda env create -f environment_gpu.yaml
```
Otherwise
```bash
conda env create -f environment.yaml
```

# Start Jupyter

You may use any port 
```bash
jupyter lab --port 7766
```

# Content 

1. [ ] Структура та структурні елементи постановки ML задачі. Формалізація бізнес задач. Основні задачі й методи в сфері Обробки природних мов - Volodymyr 
2. [ ] Представлення природніх мов в машинному вигляді. Класичні та нейронні алгоритми векторизації. Класичні ML підходи в NLP(Take from 4th Lecture). - Vladyslav 
3. [ ] Основні метрики в NLP (обробка природніх мов). Побудова оцінки підходів і моделей в NLP - валідація. - Anton
4. [ ] Підходи з використанням архітектур RNN/GRU/LSTM. - Volodymyr
5. [ ] Підходи з використанням архітектури Transformer. - Anton  
6. [ ] Генеративні задачі: машинний переклад, умовна та безумовна текстова генерація, розгляд GPT архітектури - Vladyslav
    - Task Exploration 
    - Theoretic background (GPT)
    - Train small GPT
    - GPT2 to GPT3 change. Model is bigger that dataset. GPT 3.5 with RL  
    - Summarization and Translation: T5 or Bart
7. [ ] Задача кластеризації. Задача моделювання тем. - Volodymyr
8. [ ] MLOps - розгортання моделей. - Anton 
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

- For Week 2 and 3 we will use Kaggle datasets. [Prepare in advance](#how-to-use-kaggle-datasets)
    - Fake and real news dataset API command: `kaggle datasets download -d clmentbisaillon/fake-and-real-news-dataset`
    - Toxic Comment Classification Challenge API command: `kaggle competitions download -c jigsaw-toxic-comment-classification-challenge`
    - Our propaganda detection dataset - `kaggle datasets download -d vladimirsydor/propaganda-detection-our-data`
    - Unsupervised ru propaganda dataset 01-02-2022 till 30-01-2023 - `kaggle datasets download -d vladimirsydor/ru-propaganda-2022-year`

## How to use Kaggle datasets

1. Create Kaggle account 
1. Create [Kaggle](https://www.kaggle.com/) account
2. Proceed [with Installation & Authentication](https://www.kaggle.com/docs/api#getting-started-installation-&-authentication)
3. Download dataset with API command 
