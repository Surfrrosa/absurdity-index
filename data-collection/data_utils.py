"""Shared utilities for data collection scripts."""

import csv
import glob
import os


def count_data_rows(filepath):
    """Count non-header rows in a CSV file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            return sum(1 for _ in reader)
    except Exception:
        return 0


def get_latest_file(pattern, min_rows=5, verbose=False):
    """Get the most recent file matching the pattern that has real data.

    Skips files with fewer than min_rows data rows (likely failed collections).
    """
    files = glob.glob(pattern)
    if not files:
        return None
    # Sort by filename descending (timestamps in filenames ensure chronological order)
    files.sort(reverse=True)
    for filepath in files:
        rows = count_data_rows(filepath)
        if rows >= min_rows:
            return filepath
        elif verbose:
            print(f"  Skipping {os.path.basename(filepath)} ({rows} rows, need >={min_rows})")
    return None
