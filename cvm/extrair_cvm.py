# extrair_cvm.py
# Amazon Institute — WP 2026.01
# Extrai: Book Value, Comprehensive Income, Dividends
# Empresas: MDIA3, VIVA3, RADL3 | Anos: 2020-2025
# Fonte: CVM DFP (dados.cvm.gov.br)
#
# Instalar: pip install pandas requests
# Rodar: python3 extrair_cvm_v3.py

import pandas as pd
import requests
import zipfile
import io

COMPANIES = {
    "VIVA3": "024805",
    "MDIA3": "020338",
    "RADL3": "005258",
}

YEARS = [2020, 2021, 2022, 2023, 2024, 2025]

def download_dfp(year):
    url = f"https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_{year}.zip"
    print(f"  Downloading {year}...", end=" ")
    try:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        print("OK")
        return zipfile.ZipFile(io.BytesIO(r.content))
    except Exception as e:
        print(f"FAILED ({e})")
        return None

def read_file(z, keyword):
    for f in z.namelist():
        if keyword in f and "con" in f.lower():
            df = pd.read_csv(z.open(f), sep=";", encoding="latin1", dtype=str)
            for col in ["ORDEM_EXERC", "CD_CONTA", "CD_CVM"]:
                df[col] = df[col].str.strip()
            return df
    return None

def extract_item(df, contas, item_name, year):
    """contas: list of account codes to try"""
    rows = []
    if df is None:
        return rows
    if isinstance(contas, str):
        contas = [contas]
    seen = set()
    for conta in contas:
        for ultimo in ["ULTIMO", "ÚLTIMO"]:
            filtered = df[
                (df["CD_CVM"].isin(COMPANIES.values())) &
                (df["CD_CONTA"] == conta) &
                (df["ORDEM_EXERC"] == ultimo)
            ]
            for _, row in filtered.iterrows():
                ticker = [k for k, v in COMPANIES.items() if v == row["CD_CVM"]][0]
                key = (ticker, year, item_name)
                if key not in seen:
                    seen.add(key)
                    rows.append({
                        "Ticker": ticker,
                        "Year": year,
                        "Item": item_name,
                        "Value_BRL_mil": round(abs(float(row["VL_CONTA"])) / 1000, 0)
                    })
    return rows

all_data = []

for year in YEARS:
    z = download_dfp(year)
    if not z:
        continue

    bpp = read_file(z, "BPP")
    dra = read_file(z, "DRA")
    dfc = read_file(z, "DFC_MI")

    rows = []
    # Book Value — code 2.03 (all 3 companies)
    rows += extract_item(bpp, "2.03", "Book Value", year)

    # Comprehensive Income — 3.11 (Vivara) or 4.03 (MDIA3, RADL3)
    rows += extract_item(dra, ["3.11", "4.03"], "Comprehensive Income", year)

    # Dividends — code 6.03.04 (all 3 companies)
    rows += extract_item(dfc, "6.03.04", "Dividends", year)

    all_data.extend(rows)
    print(f"  {year}: {len(rows)} records")

if not all_data:
    print("\nNo data extracted.")
else:
    df = pd.DataFrame(all_data)
    pivot = df.pivot_table(
        index=["Ticker", "Year"],
        columns="Item",
        values="Value_BRL_mil",
        aggfunc="first"
    ).reset_index()
    pivot.columns.name = None
    pivot = pivot.sort_values(["Ticker", "Year"])

    pivot.to_csv("wp2026_01_raw_data.csv", index=False)

    print(f"\n{'='*72}")
    print(f"  WP 2026.01 - Raw Data Extracted")
    print(f"{'='*72}")
    print(pivot.to_string(index=False))
    print(f"\nSaved: wp2026_01_raw_data.csv")
    print(f"{'='*72}")