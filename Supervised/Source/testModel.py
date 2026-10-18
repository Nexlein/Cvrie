import sys
import argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from Source.config import PROJECT_ROOT
from Source.imageNormalizer import imageNormalizer
from Source.imageLoader import loadImage
import joblib

MODELS = {
    "mlp": {
        "model": Path(PROJECT_ROOT, "ModelSave", "modelMLP.pkl"),
        "scaler": Path(PROJECT_ROOT, "ModelSave", "scaler.pkl"),
        "label_encoder": Path(PROJECT_ROOT, "ModelSave", "labelEncoder.pkl"),
    },
    "svm": {
        "model": Path(PROJECT_ROOT, "ModelSave", "pipelineSVC.pkl"),
    },
    "rf": {
        "model": Path(PROJECT_ROOT, "ModelSave", "randomForest.pkl")
    },
}

def load_model(model_name):
    config = MODELS[model_name]
    try:
        model = joblib.load(config["model"])
        scaler = joblib.load(config["scaler"]) if "scaler" in config else None
        le = joblib.load(config["label_encoder"]) if "label_encoder" in config else None
        return model, scaler, le
    except FileNotFoundError as e:
        print(f"Error: Missing model file. Have you trained the models first? Details: {e}", file=sys.stderr)
        sys.exit(84)
    return model, scaler, le

def testModel(model_name):
    model, scaler, le = load_model(model_name)

    xList = []
    fileNames = []
    normalizedImg = Path(PROJECT_ROOT / "Dataset" / "Tests" / "Normalized")

    imageNormalizer()

    for file in normalizedImg.iterdir():
        normalizedImg = loadImage(file.stem, "Tests")
        xList.append(normalizedImg)
        fileNames.append(file.name)

    if scaler:
        xList = scaler.transform(xList)

    yList = model.predict(xList)

    if le:
        yList = le.inverse_transform(yList)

    for fileName, prediction in zip(fileNames, yList):
        print(f"{fileName} → {prediction}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a trained model on custom images.")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-m", "--model",
        choices=MODELS.keys(),
        help="Model to use for prediction (e.g. mlp, svm)"
    )
    group.add_argument(
        "--every-models",
        action="store_true",
        help="Run prediction with all available models"
    )
    
    args = parser.parse_args()

    if args.every_models:
        for model_name in MODELS.keys():
            print(f"\n=== {model_name.upper()} ===")
            testModel(model_name)
    else:
        testModel(args.model)