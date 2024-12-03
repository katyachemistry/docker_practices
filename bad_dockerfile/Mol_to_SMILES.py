from rdkit import Chem

def trial():
    m = Chem.MolFromMolFile('mol_files/ChEBI_15422.mol')
    s = Chem.MolToSmiles(m,isomericSmiles=False)
    with open('smiles_files_temp/trial.txt', 'w') as smiles_file:
        smiles_file.writelines(s)

if __name__ == '__main__':
    trial()
