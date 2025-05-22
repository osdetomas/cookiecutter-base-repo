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

2. Go to repo and develop

```bash
cd project_slug-repo && code .
```

## Updating template

To update an existing project, that was created using cruft, run cruft update in the root of the project.
If there are any updates, cruft will have you review them before applying. If you accept the changes cruft will apply them to your project and update the .cruft.json file for you. 

```bash
cruft update
```

> If you need to go deeper into how the update works, you can visit the [official Cruft documentation](https://cruft.github.io/cruft/#updating-a-project) where it is clearly explained.