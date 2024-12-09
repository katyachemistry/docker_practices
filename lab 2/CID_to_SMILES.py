import requests
import pandas as pd
import argparse
from sqlalchemy import create_engine, text
import os

def fetch_smiles_canonical(cid):
    """Fetch canonical SMILES string for a given CID from PubChem."""
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/CanonicalSMILES/TXT"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    return None

def fetch_smiles_isomeric(cid):
    """Fetch canonical SMILES string for a given CID from PubChem."""
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IsomericSMILES/TXT"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    return None

def convert_cids_to_smiles(input_file, smiles_type, db_connection_string):
    """Convert a list or DataFrame of CIDs to SMILES."""
    df = pd.read_csv(input_file)
    if smiles_type == 'canonical':
        df['SMILES'] = df['CID'].apply(fetch_smiles_canonical)
    else:
        df['SMILES'] = df['CID'].apply(fetch_smiles_isomeric)
    engine = create_engine(db_connection_string)

    with engine.begin() as connection:
        for _, row in df.iterrows():
            print(f"CID: {row['CID']}, SMILES: {row['SMILES']}")
            query = text("INSERT INTO CHEMICAL_DATA (CID, SMILES) VALUES (:CID, :SMILES) ON CONFLICT (CID) DO NOTHING;")
            connection.execute(query, {'CID': row['CID'], 'SMILES': row['SMILES']})
        connection.commit()
    
    print(f"Data successfully written to table 'CHEMICAL_DATA'.")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="CID_to_SMILES")
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file')
    parser.add_argument(
        '-t',
        '--type',
        type=str,
        choices=['isomeric', 'canonical'],  # Restrict to these values
        required=True,
        help="Choose either isomeric or canonical."
    )
    args = parser.parse_args()

    db_connection_string = os.getenv("DATABASE_URL")

    convert_cids_to_smiles(args.input, args.type, db_connection_string)
