##
## EPITECH PROJECT, 2026
## G-AIA-400-MPL-4-1-cvrie-2
## File description:
## computeDataset
##

from pathlib import Path
import sys
from typing import Iterable
import pandas as pd

def mergeDataset(csvPaths: Iterable[str | Path], outputPath: str | Path | None = None) -> pd.DataFrame:
    # Convert to list
	csvPaths = list(csvPaths)
	if not csvPaths:
		print("Error: No CSV files provided for merging.", file=sys.stderr)
		sys.exit(84)

	dataset = []
	expectedColumns = None

	# Read and validate each CSV file
	for csvPath in csvPaths:
		dataframe = pd.read_csv(csvPath)
		columns = list(dataframe.columns)

		if expectedColumns is None:
			expectedColumns = columns
		elif columns != expectedColumns:
			print(f"Error: Inconsistent columns in CSV file {csvPath}.", file=sys.stderr)
			sys.exit(84)

		dataset.append(dataframe)

	# Concatenate all dataframes into one
	mergedDataset = pd.concat(dataset, ignore_index=True)

	if outputPath is not None:
		mergedDataset.to_csv(outputPath, index=False)
	else:
		mergedDataset.to_csv("MergedDataset.csv", index=False)

	return mergedDataset
