# Makefile for NVIDIA Privacy Model Web Service

# Variables
IMAGE_NAME = nvidia-privacy-model-service
CPU_IMAGE_NAME = $(IMAGE_NAME)-cpu
REGISTRY = registry.cluster:5000

# Default target
.PHONY: all
all: docker-build-cpu

# Build CPU Docker Image
.PHONY: docker-build-cpu
docker-build-cpu:
	docker build -t $(CPU_IMAGE_NAME) -f ./nvidia-privacy-model-service/Dockerfile.cpu ./nvidia-privacy-model-service

# Push to registry.cluster:5000 docker registry
.PHONY: docker-push-cpu
docker-push-cpu:
	docker tag $(CPU_IMAGE_NAME) $(REGISTRY)/$(CPU_IMAGE_NAME)
	docker push $(REGISTRY)/$(CPU_IMAGE_NAME)

# Run the docker CPU Docker Image
.PHONY: run-ws-cpu
run-ws-cpu:
	docker run --rm -p 8000:8000 $(CPU_IMAGE_NAME)

# Clean up
.PHONY: clean
clean:
	docker rmi -f $(CPU_IMAGE_NAME) || true

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  docker-build-cpu    - Build CPU Docker Image"
	@echo "  docker-push-cpu     - Push to registry.cluster:5000 docker registry"
	@echo "  run-ws-cpu          - Run the docker CPU Docker Image"
	@echo "  clean               - Clean up built images"
	@echo "  help                - Show this help"