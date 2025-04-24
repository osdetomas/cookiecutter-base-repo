# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Getting Started

...

Ensure you have the following software installed on your machine:
- [Docker](https://docs.docker.com/get-docker/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Development Tools

This project uses [uv](https://docs.astral.sh/uv/), an extremely fast Python package installer and resolver. uv serves as a replacement for pip and virtualenv with significant performance improvements:

- Package installation 10-100x faster than pip
- Optimized dependency resolution
- Compatible with pip and virtualenv

#### Using uv for dependency management:

#### Local Development

1. Create a virtual environment and install dependencies:

To create the virtual environment, you must first install the package manager: [uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv venv
source .venv/bin/activate
uv sync
```

### Format and Lint your code

Inside your venv install pre commit packages with the following command:

```bash
 uv run pre-commit install
```

 Now you can execute the linter and format tool with the following command:
```bash
uv run pre-commit run --all-files
```

In case you just want run the linter part you can execute this command to see the errors:

```bash
uv run ruff check .
```

Some linters issues can be fixed automaticaly with the following command:

```bash
uv run ruff check . --fix
```

In case you want to check the format part you can execute the following command (In that case you have to fix manually one by one all the issues):

```bash
uv run ruff format .
```
