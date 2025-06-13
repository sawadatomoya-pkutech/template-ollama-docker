
# ollama-template

An ollama project template.

## Usage

Build

```sh
docker compose build
```

Run [main.py](./src/main.py)

```sh
docker compose up --build
```

Changes to source codes inside `src` requires rebuild.
Or you can bind `src` to the working directory in the container. Make sure you bind it under the uv project folder (/app/).
