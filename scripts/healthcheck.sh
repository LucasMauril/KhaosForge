#!/usr/bin/env bash
# ==============================================================================
# Khaos Forge - Environment & Toolchain Healthcheck
# Author: Lucas Mauril
# ==============================================================================

set -uo pipefail

echo "========================================================"
echo "  KHAOS FORGE: SYSTEM & RUNTIME HEALTHCHECK"
echo "========================================================"

check_cmd() {
    local cmd="$1"
    local desc="$2"
    if command -v "$cmd" &> /dev/null; then
        echo -e "[+] PASS: $desc ($cmd) found: $(command -v "$cmd")"
    else
        echo -e "[-] WARN: $desc ($cmd) not detected in host PATH."
    fi
}

check_cmd "python3" "Python 3 Runtime"
check_cmd "node" "Node.js Engine"
check_cmd "docker" "Docker Container Engine"
check_cmd "git" "Git Version Control"

echo "========================================================"
echo "  HEALTHCHECK COMPLETE"
echo "========================================================"
