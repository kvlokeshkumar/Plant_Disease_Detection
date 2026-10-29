# Plant Disease Detection

A convolutional neural network (TensorFlow/Keras) that classifies leaf images into 38 crop disease classes, with a Streamlit web app for predictions, severity estimation and treatment guidance. Validation accuracy is about 97%.

## Quick start

```bash
git lfs install
git clone https://github.com/kvlokeshkumar/Plant_Disease_Detection.git
cd Plant_Disease_Detection
pip install -r Plant_Disease_Dataset/requirement.txt   # Python 3.10
cd Plant_Disease_Dataset
streamlit run main.py
```

## Documentation

- **[PROJECT_KNOWLEDGE.txt](PROJECT_KNOWLEDGE.txt)**: full project documentation, covering architecture, dataset, model, training, setup, known issues and open questions.
- **[DATA_README.md](DATA_README.md)**: where the training dataset is stored and how to download it.
