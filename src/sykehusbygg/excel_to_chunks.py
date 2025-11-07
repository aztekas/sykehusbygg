import pandas as pd
from pathlib import Path

# set path
fo = Path("..").resolve()
katalog_fi = fo / "sykehusbygg" / "resource" / "Standardromkatalog v4.0-04.11.2025.xlsx"

# read all sheet
sheets = pd.read_excel(katalog_fi, sheet_name=None, engine="openpyxl")

# get sheet name and content
first_sheet_name = list(sheets.keys())[0]
first_sheet_df = sheets[first_sheet_name]

RFP = first_sheet_df

# replace true fales
ja_nei_columns = [col for col in RFP.columns if 'Ja/Nei' in col]
RFP[ja_nei_columns] = RFP[ja_nei_columns].replace({True: 'Ja', False: 'Nei'})

# fullfill NA
RFP = RFP.fillna("ikke relevant for dette rommet")


def format_row_chunks(df):
    for _, row in df.iterrows():
        def chunk_generator():
            # prefix
            prefixes = {}
            for col in row.index:
                if ' - ' in col:
                    prefix = col.split(' - ')[0]
                    prefixes.setdefault(prefix, []).append(col)

            yield "{"
            for prefix, cols in prefixes.items():
                yield "  {"
                yield '    "RFP (hva er det)",'
                yield '    "Dette er en beskrivelse av noen av funksjonene i et rom",'
                yield f'    "Kode": "{row.get("Kode", "")}",'
                yield f'    "Navn": "{row.get("Navn", "")}",'
                yield f'    "Standard areal": "{row.get("Standard areal", "")}",'
                yield ""
                yield f'    "Beskrivelse": "{row.get("Beskrivelse", "")}",'
                yield ""
                yield f'    "Under følger detaljer for {prefix}:"'
                yield ""
                for col in cols:
                    if pd.notna(row[col]):
                        short_col = col.replace(prefix + ' - ', '')
                        yield f'    "{short_col}: {row[col]}",'
                yield "  },"
            yield "}"

        yield "\n".join(chunk_generator())


# this is what we want
rom_tekstblokker = []
for i, rom in enumerate(format_row_chunks(RFP)):
    if i >= 5:
        break
    rom_tekstblokker.append(rom)

# see it in text
with open("rom_output2.txt", "w", encoding="utf-8") as f:
    for block in rom_tekstblokker:
        f.write(block + "\n" + "="*60 + "\n")