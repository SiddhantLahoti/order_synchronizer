"""
Data cleaning and coordinate conversion utilities.
"""

import openpyxl.utils


def clean_order_id(value) -> str:
    """
    Standardizes Order IDs into clean, comparable strings to prevent mismatches
    caused by float representations (.0), leading/trailing whitespace, or None values.
    """
    if value is None:
        return ""
    val_str = str(value).strip()
    if val_str.endswith(".0"):
        val_str = val_str[:-2]
    return val_str


def col_to_index(col_letter: str) -> int:
    """Converts an Excel column letter (e.g., 'A', 'KV') to a 1-based index."""
    return openpyxl.utils.column_index_from_string(col_letter)