##
## EPITECH PROJECT, 2026
## G-AIA-400-MPL-4-1-cvrie-2
## File description:
## Tools
##

import sys
import pandas as pd
from pathlib import Path
import logging
from Source.config import PROJECT_ROOT, VALID_EXTENSIONS

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def _getImageFiles(imagePaths):
    # Check if the dataset directory exists
    if not imagePaths.exists():
        print(f"Error: No file found {imagePaths}", file=sys.stderr)
        sys.exit(84)

    # Collect all valid image paths
    imageFiles = sorted([
        file for file in imagePaths.rglob("*")
        if file.is_file() and file.suffix.lower() in VALID_EXTENSIONS
    ])

    if not imageFiles:
        print(f"Error: No valid image files found in {imagePaths}", file=sys.stderr)
        sys.exit(84)

    logger.info(f"Analysed file : {imagePaths.resolve()}")
    logger.info(f"Number of images found : {len(imageFiles)}")
    return imageFiles

def _createCSV(imagePaths, bodyPart, datasetDir=None):
    # Create dataframe for CSV
    df = pd.DataFrame({
        "ImageId": [imagePath.stem for imagePath in imagePaths],
        "Label(BodyPart)": bodyPart
    })
    logger.info(f"Created DataFrame with {len(df)} entries for body part: {bodyPart}")

    # Determine output directory for CSV
    if datasetDir is not None:
        outputDir = Path(datasetDir).resolve().parent
    else:
        outputDir = Path(imagePaths[0]).resolve().parent
    logger.info(f"Output directory for CSV: {outputDir}")

    # Ensure output directory exists
    csvName = f"{bodyPart}Dataset.csv"
    csvPath = outputDir / csvName
    df.to_csv(csvPath, index=False)
    logger.info(f"CSV created at: {csvPath}")

    return csvPath

def prepareDataset(bodyPart: str):
    datasetPath = PROJECT_ROOT / "Dataset" / bodyPart / "Normalized"

    logger.info(f"Preparing dataset for body part: {bodyPart}")

    imageFiles = _getImageFiles(datasetPath)
    csvPath = _createCSV(
        imagePaths=imageFiles,
        bodyPart=bodyPart,
        datasetDir=datasetPath
    )
    return csvPath

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s", stream=sys.stdout)
    prepareDataset(bodyPart="Chest")
