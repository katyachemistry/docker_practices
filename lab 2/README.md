# CID to SMILES Converter

This project converts a list of PubChem CIDs (Chemical Identifiers) into SMILES (Simplified Molecular Input Line Entry System) notation and stores the data in a PostgreSQL database.

## Requirements

- Docker
- Docker Compose

## Setup

1. Clone the repository.
2. Create a `.env` file in the root directory with the following variables:

```env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=my_database
```

3. Build and run the project with Docker Compose:

```bash
docker-compose up --build
```

This will:
- Start a PostgreSQL container.
- Build and run the application that converts CIDs to SMILES using the provided input file and type (canonical or isomeric).
- Store the results in the PostgreSQL database.

## Docker Compose Services

- **postgres**: PostgreSQL database service.
- **get_smiles**: Python service that converts CIDs to SMILES.

## Database

The resulting data (CIDs and SMILES) will be saved in the PostgreSQL database under the `CHEMICAL_DATA` table.

## Health Checks

- PostgreSQL service health is checked using `pg_isready`.