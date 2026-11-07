#!/usr/bin/env python3
"""
Sync Reference Repositories
Clones or updates the 11 foundational open-source cybersecurity repositories.
Author: Lucas Mauril
"""
import subprocess
from pathlib import Path

REPOS = {
    "0xor0ne-awesome-list": "https://github.com/0xor0ne/awesome-list.git",
    "anthropic-skills": "https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git",
    "awesome-gpt-agents": "https://github.com/fr0gger/Awesome-GPT-Agents.git",
    "awesome-pentest": "https://github.com/enaqx/awesome-pentest.git",
    "cai-runner": "https://github.com/aliasrobotics/cai.git",
    "carterperez-projects": "https://github.com/CarterPerez-dev/Cybersecurity-Projects.git",
    "gundb": "https://github.com/amark/gun.git",
    "khaos-mcp": "https://github.com/henriqqw/KhaosMCP-Pentester-Agent.git",
    "ntopng": "https://github.com/ntop/ntopng.git",
    "pentestgpt": "https://github.com/GreyDGL/PentestGPT.git",
    "security-101": "https://github.com/microsoft/Security-101.git"
}

def sync():
    root = Path(__file__).parent.parent / "references"
    root.mkdir(parents=True, exist_ok=True)
    print(f"[*] Syncing {len(REPOS)} reference repositories into: {root}")

    for name, url in REPOS.items():
        dest = root / name
        if dest.exists():
            print(f"[+] '{name}' already present. Skipping.")
        else:
            print(f"[*] Cloning '{name}' from {url}...")
            subprocess.run(["git", "clone", "--depth", "1", url, str(dest)], check=False)

    print("[+] All reference repositories synchronized successfully.")

if __name__ == "__main__":
    sync()
