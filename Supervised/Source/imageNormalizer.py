##
## EPITECH PROJECT, 2026
## Cvrie
## File description:
## imageNormalizer
##

from pathlib import Path
import sys
from PIL import Image
from Source.config import IMAGE_SIZE, PROJECT_ROOT

### TODO:
# - apporter une solution en plus pour les déséquilibre de données
# - revoir la partie loss F/ learning rate/ Doc
# - ajouter de nouvelles classifications
# - Clear section in each notebook for model comparisons (ex: loss function)
# - Clear section in each notebook for conclusions and insight

### Sujet:
# Each time, your model should try to adapt itself to reduce the value of its loss function.
# This concept should be part of your notebook. Selecting a good loss function is essential for your model's
# training to be efficient.

# Your model will likely not be perfect from the get go. You should document your process and trial and error.
# Try using different algorithms, explore possibilities, and write down everything you did and your results.
# For this task, your model's result will only be a small part of what is evaluated. Your defense, where you
# will present your notebook, will be more important.

def _isNormalized(bodyPartList):
    for bodyPart in bodyPartList:
        norPath = Path(PROJECT_ROOT, "Dataset", bodyPart, "Normalized")
        srcPath = Path(PROJECT_ROOT, "Dataset", bodyPart, "Images")

        if not norPath.exists() or not norPath.is_dir():
            return False

        norCount = len([f for f in norPath.iterdir() if f.is_file()])
        srcCount = len([f for f in srcPath.iterdir() if f.is_file()])
        if norCount != srcCount:
            return False
    return True

def _imageResizerFormater(filePath):
    path = Path(filePath)
    img = Image.open(path)
    img = img.convert("L")

    w, h = img.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top  = (h - min_dim) // 2
    img = img.crop((left, top, left + min_dim, top + min_dim))

    img_resized = img.resize((IMAGE_SIZE, IMAGE_SIZE), Image.Resampling.LANCZOS)

    output_dir = Path(path.parent.parent, "Normalized", path.name)
    if not output_dir.parent.exists() or not output_dir.parent.is_dir():
            output_dir.mkdir(parents=True)
    img_resized.save(output_dir)

def imageNormalizer(bodyPartList=None):
    if bodyPartList is None:
        bodyPartList = ["Tests"]
    if _isNormalized(bodyPartList):
        return
    for bodyPart in bodyPartList:
        datasetPath = Path(PROJECT_ROOT, "Dataset", bodyPart, "Images")

        if not datasetPath.exists() or not datasetPath.is_dir():
            print(f"Error: Source directory {datasetPath} not found.", file=sys.stderr)
            sys.exit(84)

        for file in datasetPath.iterdir():
            if file.is_file():
                filePath = Path(PROJECT_ROOT, "Dataset", bodyPart, "Images", file.name)
                _imageResizerFormater(filePath)

if __name__ == "__main__":
    bodyPartList = [
        "Head",
        "Chest",
        "Hand"
    ]
    imageNormalizer(bodyPartList)
