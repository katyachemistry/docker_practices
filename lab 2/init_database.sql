create table CHEMICAL_DATA (
	id serial primary key,
	CID integer unique not null,
	SMILES text,
	embedding BYTEA
	);
