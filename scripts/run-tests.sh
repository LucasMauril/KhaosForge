#!/usr/bin/env bash
# ==============================================================================
# Khaos Forge - Comprehensive Test Suite Runner (Linux / macOS / WSL)
# Author: Lucas Mauril
# ==============================================================================

set -euo pipefail

echo "========================================================"
echo "  KHAOS FORGE: RUNNING COMPREHENSIVE TEST SUITE"
echo "========================================================"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${ROOT_DIR}"

echo "[*] 1. Executing Python Core Unit Tests..."
python3 -m unittest discover -s tests -v

echo "[*] 2. Validating Skills & Commands Frontmatter..."
python3 -c "
from pathlib import Path
import sys

skills = list(Path('skills').rglob('*.md'))
commands = list(Path('commands').rglob('*.md'))

print(f'Validating {len(skills)} skills and {len(commands)} commands...')
for item in skills + commands:
    txt = item.read_text(encoding='utf-8')
    assert txt.startswith('---'), f'Missing YAML frontmatter in {item}'
    assert 'name:' in txt, f'Missing name tag in {item}'
print('All markdown frontmatters validated successfully.')
"

echo "[*] 3. Verifying CLI Executables..."
bash "${ROOT_DIR}/bin/khaos" --help > /dev/null
echo "[+] CLI executable verified."

echo "========================================================"
echo "  ALL KHAOS FORGE TESTS PASSED (100% GREEN)"
echo "========================================================"
