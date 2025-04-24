# Use the base UV image with Python 3.12 and Debian Bookworm Slim
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory inside the container
WORKDIR /app

# Define environment variables
ENV RUNNING_IN_DOCKER=true
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

  RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --frozen --no-install-project --no-install-workspace --no-dev

# Copy dependency files to /app and synchronize dependencies
COPY uv.lock pyproject.toml README.md /app/

COPY ./src /app/src/

RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --dev

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "main"]
