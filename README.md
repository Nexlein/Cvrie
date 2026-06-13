<div align="center">
  <h1>🧠 Cvrie</h1>
  <p><strong>A Machine Learning Laboratory for Supervised and Unsupervised Algorithms</strong></p>
</div>

## Overview

Cvrie is a comprehensive Machine Learning exploration project split into two primary paradigms: **Supervised** and **Unsupervised** learning. Built entirely in Python using standard data science libraries, this project serves as a sandbox for implementing, training, evaluating, and visualizing various predictive and clustering models.

## The Two Paradigms

### 1. Supervised Learning

In the `Supervised` directory, models are trained using **labeled datasets**. The goal is to learn a mapping from inputs to outputs to make accurate predictions on unseen data.

- **Common Tasks:** Classification (predicting categories) and Regression (predicting continuous values).
- **Workflow:** Load dataset → Preprocess → Train-Test Split → Train Model → Evaluate Accuracy/Loss → Save Model (`ModelSave/`).

### 2. Unsupervised Learning

In the `Unsupervised` directory, algorithms are tasked with finding hidden structures in **unlabeled data**. The models must discover patterns, similarities, and groupings entirely on their own.

- **Common Tasks:** Clustering (e.g., K-Means, grouping similar data points) and Dimensionality Reduction (e.g., PCA, simplifying complex datasets).
- **Workflow:** Load raw data → Extract Features → Apply Clustering/Reduction → Visualize groupings.

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

## How to Use

Both the `Supervised` and `Unsupervised` directories contain their respective `Source/` folders with executable Python scripts, and `Notebooks/` for interactive Jupyter experiments.

- **To run a script:** `python Source/main.py`
- **To explore data interactively:** Open the `.ipynb` files in the `Notebooks/` folder using Jupyter.
- Trained models are automatically exported to the `ModelSave/` directory so they can be reused without retraining!
