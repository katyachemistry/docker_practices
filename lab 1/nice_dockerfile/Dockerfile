FROM python:3.9-slim

RUN pip install --upgrade pip && \
    pip install rdkit && \
    pip install numpy==1.26.0

COPY . .

ENTRYPOINT ["python", "Mol_to_SMILES.py"]