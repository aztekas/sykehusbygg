import pandas as pd
import json
import sys
from pathlib import Path


fo = Path(__file__).parent.parent.parent
data_fo = fo / "data"
katalog_fi = fo / "resource" / "Standardromkatalog v4.0-04.11.2025.xlsx"
STANDARDROMKATALOGEN_JSON = fo / "data" / "standardromkatalogen.json"


def excel_to_json(excel_path, output_path=None):
    excel_path = Path(excel_path)
    if not excel_path.exists():
        raise FileNotFoundError(f"Excel file not found: {excel_path}")

    # Read all sheets into a dict of DataFrames
    sheets = pd.read_excel(excel_path, sheet_name=None)

    result = {}
    for sheet_name, df in sheets.items():
        # Convert NaN -> None for clean JSON
        df = df.where(pd.notnull(df), None)

        # Convert DataFrame rows to list of dicts
        rows = df.to_dict(orient="records")
        result[sheet_name] = rows

    # Default output path
    if output_path is None:
        output_path = excel_path.with_suffix(".json")

    # Write to JSON file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON written to: {output_path}")


if __name__ == "__main__":

    if not STANDARDROMKATALOGEN_JSON.exists():
        excel_to_json(katalog_fi, STANDARDROMKATALOGEN_JSON)
    else:
        print("JSON already generated")

