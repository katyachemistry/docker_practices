FROM python:3.9

COPY . .

RUN pip install --upgrade pip
RUN pip install numpy==1.26.0
RUN pip install rdkit

ENTRYPOINT ["python", "Mol_to_SMILES.py"]