##
## EPITECH PROJECT, 2026
## G-AIA-400-MPL-4-1-cvrie-2
## File description:
## imageLoader
##

import sys

import numpy as np
from PIL import Image
from Source.config import PROJECT_ROOT, VALID_EXTENSIONS

def loadImage(imageId, bodyPart):
    imgDir = PROJECT_ROOT / "Dataset" / bodyPart / "Normalized"

    imgPath = next((imgDir / f"{imageId}{ext}" for ext in VALID_EXTENSIONS if (imgDir / f"{imageId}{ext}").exists()), None)
    if imgPath is None:
        print(f"Error: Image {imageId} not found in {imgDir}", file=sys.stderr)
        sys.exit(84)

    img = Image.open(str(imgPath))
    img_array = np.array(img, dtype='float32') / 255.0
    return img_array.flatten()

if __name__ == "__main__":
    imageId = "Head_1"
    bodyPart = "Head"
    imgData = loadImage(imageId, bodyPart)
    print(f"Loaded image data for {imageId} with shape: {imgData.shape}")
