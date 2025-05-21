# TODO: (Antonio) we should refactor this to avoid this change
export PYTHONPATH:= src:$PYTHONPATH
# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1
# Load environment variables from .env file
include .env

##@ Utility
.PHONY: help
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make <target>\033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: uv
uv:  ## Install uv if it's not present.
	@command -v uv >/dev/null 2>&1 || curl -LsSf https://astral.sh/uv/install.sh | sh

.PHONY: dev
dev: uv ## Install dev dependencies into a .venv environment
	uv sync --dev

.PHONY: locka
lock: uv ## lock dependencies
	uv lock

.PHONY: install
install: uv ## Install dependencies
	uv sync --frozen

.PHONY: doc
doc:  ## Serve documentation with mkdocs docker compose service
	docker compose up mkdocs