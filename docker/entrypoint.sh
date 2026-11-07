#!/usr/bin/env bash
# ==============================================================================
# Khaos Forge Sandbox Entrypoint
# ==============================================================================
set -e

echo "[*] Initializing Khaos Forge Security Toolchain..."
mkdir -p /workspace/storage/sessions /workspace/storage/targets

exec "$@"
