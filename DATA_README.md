# Data

The training and validation images are too large for Git (about 1.6 GB, 87,867 files), so they are not in this repository.

## What is in Git and what is not

| Path | Size | In Git? | Where it lives |
|---|---|---|---|
| `Plant_Disease_Dataset/trained_plant_disease_model.keras` | 94 MB | Yes, via Git LFS | This repository (run `git lfs pull`) |
| `Plant_Disease_Dataset/test/test/` | 560 KB, 33 images | Yes | This repository |
| `Plant_Disease_Dataset/train/` | ~1.3 GB, 70,295 images | No | Kaggle (below) |
| `Plant_Disease_Dataset/valid/` | ~316 MB, 17,572 images | No | Kaggle (below) |
| `data set/Plant_Disease_Dataset.zip` | 1.4 GB | No | Local copy of the Kaggle download |

## Source

Kaggle: **New Plant Diseases Dataset** by vipoooool
https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset

## How to download

Option A, from the browser:
1. Sign in to Kaggle and open the link above.
2. Click **Download** and unzip the archive.

Option B, with the Kaggle CLI (needs a Kaggle API token in `~/.kaggle/kaggle.json`; never commit that file):

```bash
pip install kaggle
kaggle datasets download -d vipoooool/new-plant-diseases-dataset
```

## Expected layout after setup

Copy or move the `train` and `valid` folders (each containing 38 class folders) into `Plant_Disease_Dataset/`. The Kaggle archive may nest them a few levels deep, under a folder like `New Plant Diseases Dataset(Augmented)`.

```
Plant_Disease_Dataset/
├── train/
│   ├── Apple___Apple_scab/
│   ├── ...                  (38 class folders)
│   └── Tomato___healthy/
├── valid/
│   └── ...                  (same 38 class folders)
└── test/test/               (already in Git)
```

To check the counts, run this from `Plant_Disease_Dataset/` in Python:

```python
import tensorflow as tf
tf.keras.utils.image_dataset_from_directory('train')   # Found 70295 files belonging to 38 classes.
tf.keras.utils.image_dataset_from_directory('valid')   # Found 17572 files belonging to 38 classes.
```

The class folder names must match exactly, because the model's class order is the alphabetical order of these folders.

## Optional: keep your own copy

If you want the exact local copy (`data set/Plant_Disease_Dataset.zip`, 1,487,392,828 bytes) kept as well, upload it to Google Drive or a private Hugging Face dataset and add the link here.
