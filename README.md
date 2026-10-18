<div align="center">
  <h1>🧠 Cvrie</h1>
  <p><strong>A Machine Learning Laboratory for Supervised and Unsupervised Algorithms</strong></p>
</div>

## Overview

Cvrie is a Machine Learning project split into two parts, built in Python with scikit-learn:

- **Supervised:** classify X-ray images by body part (chest, head, hand, foot).
- **Unsupervised:** cluster free-text descriptions of patient symptoms into groups of similar cases.

Each part has a Jupyter notebook that documents the experiments, and a few Python helper scripts.

## The Two Paradigms

### 1. Supervised Learning

In the `Supervised` directory, models learn to recognise which body part an X-ray shows (Chest, Head, Hand, Foot). Images are converted to grayscale, cropped and resized to 64×64, then flattened into 4096 pixel features.

- **Models:** Random Forest, PCA + SVM (scaling, PCA keeping 95% of the variance, RBF SVM) and a Multi-Layer Perceptron, each tuned with `GridSearchCV`.
- **Workflow:** Normalize images → Build the dataset CSV → Train-Test Split → Train Model → Evaluate (accuracy, confusion matrix) → Save Model (`ModelSave/`).
- The repository only ships 5 sample images per class; the full dataset used for training is not included.

### 2. Unsupervised Learning

In the `Unsupervised` directory, about 1,000 unlabeled patient symptom descriptions (`Dataset/Student_Dataset.csv`) are grouped into clusters of similar cases.

- **Techniques:** text cleaning with NLTK, text embeddings with TF-IDF and SentenceTransformers, clustering with K-Means and HDBSCAN, evaluation with the silhouette score, and UMAP for dimensionality reduction and visualization.
- **Workflow:** Load raw text → Clean → Embed → Cluster → Evaluate → Visualize groupings.

## Installation

Ensure you have Python 3 installed. It is recommended to use a virtual environment.

```bash
# Clone the repository
git clone git@github.com:Nexlein/Cvrie.git
cd Cvrie

# Install dependencies for either module
cd Supervised # or cd Unsupervised
pip install -r requirements.txt
```

### Dependencies

- `pandas` & `numpy` (Data manipulation)
- `scikit-learn` (Machine Learning algorithms)
- `matplotlib` (Data visualization)
- `pillow` (Image loading, Supervised)
- `nltk`, `sentence-transformers`, `umap-learn` (Text processing and embeddings, Unsupervised)

## How to Use

The experiments live in the notebooks: open `Supervised/Notebooks/supervised.ipynb` or `Unsupervised/Notebooks/unsupervised.ipynb` with Jupyter and run the cells in order. `Source/` holds the helper modules they import.

The supervised notebook saves its trained models to `Supervised/ModelSave/`. To classify your own X-rays with the saved models, put the images (`.jpg`, `.jpeg` or `.png`) in `Supervised/Dataset/Tests/Images/`, then run from the `Supervised` directory:

```bash
python Source/testModel.py -m mlp     # or svm, rf
python Source/testModel.py --every-models
```

Each image is normalized to `Dataset/Tests/Normalized/` and the predicted body part is printed. `python Source/cleanupProject.py` removes the generated files.
