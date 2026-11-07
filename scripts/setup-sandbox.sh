#!/usr/bin/env bash
# ==============================================================================
# Khaos Forge - Docker Sandbox Provisioner
# Author: Lucas Mauril
# ==============================================================================

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[*] Provisioning Khaos Forge Docker Sandbox..."

if ! command -v docker &> /dev/null; then
    echo "[-] Error: docker is not installed or not in PATH."
    exit 1
fi

echo "[*] Building 'khaos-tools-sandbox' image..."
docker build -t khaos-tools-sandbox -f "${ROOT_DIR}/docker/Dockerfile.tools" "${ROOT_DIR}"

echo "[*] Launching container instance..."
if docker ps -a --format '{{.Names}}' | grep -Eq "^khaos-tools-sandbox$"; then
    echo "[*] Container already exists. Restarting..."
    docker restart khaos-tools-sandbox
else
    docker run -d --name khaos-tools-sandbox \
      -v "${ROOT_DIR}/storage:/workspace/storage" \
      khaos-tools-sandbox tail -f /dev/null
fi

echo "[+] Khaos Forge Docker Sandbox is ready and operational."
