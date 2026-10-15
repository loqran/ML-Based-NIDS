"""
Step 1: label, drop IPs, clean, and take a stratified random sample of each dataset.
run from repo root:  python tools/sample.py
find <name>.csv anywhere under data/ and writes data/processed/<name>_sample.parquet
"""

from pathlib import Path

import numpy as np
import pandas as pd

DATASETS = {
    "NF-UNSW-NB15-v2": 2_390_275,
    "NF-CSE-CIC-IDS2018-v2": 18_893_708,
}  # rows, from the UQ page
SAMPLE_SIZE = 100_000  # rows per dataset
SEED = 42


def sample_dataset(name, total_rows):
    # Find the CSV anywhere under data/, e.g. data/<id>_MOHANAD_A4706/data/<name>.csv
    path = next(Path("data").rglob(f"{name}.csv"), None)
    if path is None:
        raise SystemExit(
            f"Could not find {name}.csv under data/ - extract the zip there first."
        )
    frac = SAMPLE_SIZE / total_rows
    parts, rows_read = [], 0

    # Read in chunks: the CIC file is too big to load into memory at once.
    for chunk in pd.read_csv(path, chunksize=1_000_000):
        rows_read += len(chunk)
        chunk["Label"] = (chunk["Attack"] != "Benign").astype(
            int
        )  # benign = 0, attack = 1
        chunk = chunk.drop(columns=["IPV4_SRC_ADDR", "IPV4_DST_ADDR", "Attack"])
        chunk = chunk.replace([np.inf, -np.inf], np.nan).dropna()
        # Same fraction from each class in every chunk = stratified sample.
        parts.append(chunk.groupby("Label").sample(frac=frac, random_state=SEED))

    df = pd.concat(parts, ignore_index=True)
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()  # so no flow ends up in both the train and test split

    print(
        f"{name}: read {rows_read:,} rows (UQ page: {total_rows:,}), "
        f"removed {duplicates:,} duplicates, kept {len(df):,} rows, "
        f"{df['Label'].mean():.1%} attacks, {df.shape[1] - 1} features"
    )
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    df.to_parquet(f"data/processed/{name}_sample.parquet", index=False)


for name, total_rows in DATASETS.items():
    sample_dataset(name, total_rows)
