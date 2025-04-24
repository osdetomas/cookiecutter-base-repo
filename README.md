#  cookiecutter-base-repo template

This repository serves as a development template for our projects, providing a standardized environment using Docker and uv for dependency management. It offers a basic structure, configuration for linters, and best practices for developing AI applications in Python.

## Getting Started

### Prerequisites

Before you start, ensure you have the following installed on your system:

```bash
which python
which uv
which cruft
```

Ensure you have the following software installed on your machine:
- [Docker](https://docs.docker.com/get-docker/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [cruft](https://cruft.github.io/cruft/)

## Development Tools

This project uses [uv](https://docs.astral.sh/uv/), an extremely fast Python package installer and resolver. uv serves as a replacement for pip and virtualenv with significant performance improvements:

- Package installation 10-100x faster than pip
- Optimized dependency resolution
- Compatible with pip and virtualenv

#### Using uv for dependency management:

#### Local Development

1. Create new cruft repo from template

```bash
cruft create https://github.com/INSUD-AI-Labs/cookiecutter-base-repo/
```

cruft will then ask you any necessary questions to create your new project (Behind the scenes, cruft uses Cookiecutter)

2. 
2. Create a virtual environment and install dependencies:

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

3. Updating template

To update an existing project, that was created using cruft, run cruft update in the root of the project.
If there are any updates, cruft will have you review them before applying. If you accept the changes cruft will apply them to your project and update the .cruft.json file for you. 

```bash
cruft update
```