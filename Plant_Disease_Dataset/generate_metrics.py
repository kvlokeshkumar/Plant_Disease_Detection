import os
import json
import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix

print("Loading model...")
model = tf.keras.models.load_model("trained_plant_disease_model.keras")

# Load validation data
print("Loading validation dataset...")
validation_set = tf.keras.utils.image_dataset_from_directory(
    'valid',
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(128, 128),
    shuffle=False
)

class_names = validation_set.class_names
print(f"Found {len(class_names)} classes.")

# Get true labels and predictions
print("Generating predictions...")
y_true = []
y_pred_probs = []

for images, labels in validation_set:
    y_true.extend(np.argmax(labels.numpy(), axis=-1))
    y_pred_probs.extend(model.predict(images, verbose=0))

y_pred = np.argmax(y_pred_probs, axis=-1)

print("Calculating metrics...")
# Classification report (Precision, Recall, F1)
report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)

print("Saving results...")
results = {
    "class_names": class_names,
    "classification_report": report,
    "confusion_matrix": cm.tolist()
}

with open('model_metrics.json', 'w') as f:
    json.dump(results, f)

print("model_metrics.json successfully created!")
