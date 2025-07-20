#!/bin/bash
set -e

echo "[install.sh] Building Docker image..."
docker build -t fastapi-auth-err .
echo "[install.sh] Stopping and removing any existing container..."
docker rm -f fastapi-auth-err-cntnr 2>/dev/null || true
echo "[install.sh] Starting new Docker container..."
docker run -d --name fastapi-auth-err-cntnr -p 8000:8000 fastapi-auth-err
echo "[install.sh] FastAPI container started on port 8000."
