##
## EPITECH PROJECT, 2026
## G-AIA-400-MPL-4-1-cvrie-2
## File description:
## cleanCsv
##

"""
Removes:
- Dataset/<bodyPart>/Normalized/*
- Dataset/<bodyPart>/<bodyPart>Dataset.csv
- Dataset/mergedDataset.csv
"""

from pathlib import Path
import shutil
from config import PROJECT_ROOT

BODYPARTS = ["Chest", "Head", "Foot", "Hand", "Tests"]

def _removePath(path: Path) -> None:
    """Remove a file or directory path if it exists."""
    if not path.exists():
        return
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()

def cleanBodyPart(datasetPath: Path, bodyPart: str) -> None:
    """Delete normalized images and body-part CSV for one body part."""
    bodyPartDir = datasetPath / bodyPart
    normalizedDir = bodyPartDir / "Normalized"
    datasetCsv = bodyPartDir / f"{bodyPart}Dataset.csv"

    if normalizedDir.exists():
        for file in normalizedDir.iterdir():
            _removePath(file)

    _removePath(datasetCsv)

def cleanupProject() -> None:
    """Delete all generated dataset in the repository."""
    datasetPath = PROJECT_ROOT / "Dataset"
    for bodyPart in BODYPARTS:
        cleanBodyPart(datasetPath, bodyPart)
    _removePath(datasetPath / "mergedDataset.csv")

if __name__ == "__main__":
    cleanupProject()
