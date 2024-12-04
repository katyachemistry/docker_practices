# Lab #1

## Good and Bad Dockerfile Practices

An app used in this laboratory generates SMILES of molecules from mol-format files.  
You can find good and bad Dockerfiles in respective directories.  

After cloning the repository, navigate to the directory and run the following commands:  

```bash
docker build -t <image_name>
```

e.g.

```bash
docker build -t nice_docker
```

In case you want to bind mount a directory to store SMILES locally, use:

```bash
docker run -v <absolute path to dir>:/smiles_files_temp nice_docker
```

e.g.

```bash
docker run -v /mnt/c/Users/noname/docker_practices/smiles_files_storage/:/smiles_files_temp nice_docker
```

Alternatively, you can use a named volume if you don't need the files for now. In this case, first create the volume:

```bash
docker volume create <volume_name>
```

and then:

```bash
docker run -v <volume_name>:/smiles_files_temp nice_docker
```

---

## Bad Practices Used

1. The bad Dockerfile uses a heavy image (`python-3.9`) instead of a lightweight one (`python-3.9-slim`), which is unnecessary for a simple app.
2. `RUN` commands are split across three layers when they could have been merged into one.
3. `COPY` is placed before running installations. If the `COPY` line changes, installation layers will re-run in a new build.
4. No `.dockerignore` file is present, which can lead to unnecessary files being copied into the image.

Another bad practice is writing passwords or tokens in dockerfile.  