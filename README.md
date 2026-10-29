# 🌿 Plant Disease Detection: Leaf Image Classifier with Severity Analysis

**Team Members:** K V Lokesh Kumar · Sinduja U V

## 💡 What is it?

Plant Disease Detection is a deep learning system that identifies crop diseases from a single photo of a leaf. Farmers, gardeners and agriculture students often can't reach an expert quickly, and a missed or late diagnosis lets a disease spread through a whole field.

Upload a leaf image and the system:

* 🔍 **Classifies** it into one of **38 crop/disease classes** across 14 crops (apple, corn, grape, potato, tomato and more) with a custom CNN.
* 📊 **Shows the top 5 predictions** with confidence scores.
* 🩺 **Estimates severity** (Mild, Moderate, Severe or Critical) from the share of the leaf that looks diseased.
* 💊 **Gives guidance**: description, symptoms, prevention and treatment steps matched to the severity level.
* 🌬️ **Previews pathogen spread** from field conditions (humidity, wind, rainfall, nearby infected plants).

Validation accuracy is **96.96%** on 17,572 images.

## 🏗️ System Architecture

```
 Leaf image (JPG/PNG)
        │
        ▼
 Streamlit app (main.py)
        │  resize to 128×128 RGB
        ▼
 CNN model (trained_plant_disease_model.keras)
        │  38 softmax probabilities
        ▼
 Top-5 classes ──► disease_info.py
                    ├─ disease database (description, symptoms, prevention)
                    └─ analyze_severity(): HSV colour analysis → affected leaf %
        │
        ▼
 Results: prediction · severity · treatments · pathogen spread preview
```

**Training pipeline** (`training_model.ipynb`): `train/` and `valid/` image folders → `image_dataset_from_directory` → CNN → 10 epochs → saved model, plus `training_hist.json` and `model_metrics.json`.

## ✨ Key Features

### 1. 🧠 Custom CNN Classifier
* 5 convolution blocks (32 → 64 → 128 → 256 → 512 filters), each with two 3×3 convolutions and max pooling.
* Dropout (0.25 and 0.4), a 1500-unit dense layer and a 38-class softmax output.
* 7.84 million parameters, trained with Adam (learning rate 0.0001) for 10 epochs.

### 2. 🩺 Severity Analysis
* Converts the leaf to HSV and separates healthy green tissue from discoloured areas.
* Maps the affected area to a level: **Mild** (<15%), **Moderate** (15–35%), **Severe** (35–60%) or **Critical** (>60%).
* Each level comes with an urgency rating and step-by-step treatment advice.

### 3. 📚 Disease Knowledge Base
* All 38 classes include the plant, the disease, its cause, symptoms, treatment and prevention.

### 4. 🌬️ Pathogen Spread Preview
* Rule-based scoring of spread pressure (Low, Medium or High) from severity, humidity, temperature, wind speed and direction, rainfall and nearby infected plants.
* Draws a factor radar chart and a 5×5 hotspot grid around the infected plant.

### 5. 📈 Model Dashboard and History
* **About** page: training vs validation accuracy and loss curves.
* **Prediction History** page: a log of the predictions made in the session and a chart of how they are distributed.

## 📊 Results

| Metric | Value |
|---|---|
| Validation accuracy | 96.96% |
| Macro precision / recall / F1 | 96.99% / 96.95% / 96.95% |
| Final training accuracy | 98.2% |
| Validation images | 17,572 |

## 🚀 Quick Start Guide

### Prerequisites
* Python 3.10 (required by TensorFlow 2.10)
* Git and [Git LFS](https://git-lfs.com), since the trained model is stored with LFS

### 1. Clone the repository
```bash
git lfs install
git clone https://github.com/kvlokeshkumar/Plant_Disease_Detection.git
cd Plant_Disease_Detection
git lfs pull
```

### 2. Set up the environment
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r Plant_Disease_Dataset/requirement.txt
```

### 3. Run the app
```bash
cd Plant_Disease_Dataset
streamlit run main.py
```
The app runs at `http://localhost:8501`. Open **Disease Recognition** in the sidebar, upload a leaf image and click **Predict Disease**.

### 4. Retrain the model (optional)
Download the dataset as described in [DATA_README.md](DATA_README.md), then:
```bash
cd Plant_Disease_Dataset
jupyter notebook training_model.ipynb    # run all cells
python generate_metrics.py               # rebuild model_metrics.json
```

## 🧪 Sample Images to Test

Try these images from `Plant_Disease_Dataset/test/test/`:

1. 🍎 **Apple Cedar Rust**: `AppleCedarRust1.JPG`
2. 🌽 **Corn Common Rust**: `CornCommonRust1.JPG`
3. 🥔 **Potato Early Blight**: `PotatoEarlyBlight1.JPG`
4. 🍅 **Tomato Yellow Leaf Curl Virus**: `TomatoYellowCurlVirus1.JPG`
5. 🌱 **Healthy Tomato**: `TomatoHealthy1.JPG`

## 🗂️ Dataset

[New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) on Kaggle: 70,295 training and 17,572 validation images of 38 classes. The images are not stored in this repository. See [DATA_README.md](DATA_README.md) for download steps.

## 📖 Documentation

* **[PROJECT_KNOWLEDGE.txt](PROJECT_KNOWLEDGE.txt)**: full documentation covering architecture, dataset, model, training, setup, known issues and open questions.
* **[DATA_README.md](DATA_README.md)**: where the dataset is stored and how to download it.
