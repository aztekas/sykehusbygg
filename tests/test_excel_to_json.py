import json
import sys
import pathlib

import pytest


def test_excel_to_json_roundtrip(tmp_path):
    # Skip the test if pandas isn't available in the environment
    pd = pytest.importorskip("pandas")

    # Ensure the package src directory is on sys.path so we can import the module
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"
    sys.path.insert(0, str(src_dir))

    from sykehusbygg.excel_to_json import excel_to_json

    # Create three small dataframes and write them to an Excel file
    df1 = pd.DataFrame({"id": [1, 2], "name": ["alice", "bob"]})
    df2 = pd.DataFrame({"value": [None, 3], "flag": [True, False]})
    df3 = pd.DataFrame({"x": [0.1, 0.2], "y": ["a", "b"]})

    excel_path = tmp_path / "sample.xlsx"
    # use openpyxl engine (installed via pyproject dependencies)
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df1.to_excel(writer, sheet_name="Sheet1", index=False)
        df2.to_excel(writer, sheet_name="Second", index=False)
        df3.to_excel(writer, sheet_name="Third", index=False)

    out_json = tmp_path / "out.json"
    # Run the function under test
    excel_to_json(excel_path, out_json)

    # Load and assert the json structure
    data = json.loads(out_json.read_text(encoding="utf-8"))

    # Basic structure and sheet names
    assert set(data.keys()) == {"Sheet1", "Second", "Third"}

    # Check Sheet1 rows
    assert data["Sheet1"] == [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}]

    # Check Second - missing values should become null -> None in Python
    assert data["Second"][0]["value"] is None
    assert data["Second"][1]["value"] == 3

    # Check Third values
    assert data["Third"][0]["x"] == pytest.approx(0.1)
    assert data["Third"][1]["y"] == "b"
