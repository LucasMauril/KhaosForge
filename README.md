# 🔥 Khaos Forge

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Protocol](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io/)
[![Author](https://img.shields.io/badge/Author-dj-red.svg)](https://github.com/dj)
[![Build](https://img.shields.io/badge/Build-Passing-success.svg)](.github/workflows/validate-skills.yml)

> **Autonomous Cybersecurity Forge, Red Team Swarms & DevSecOps Engine.**
> Built by **dj**. Engineered for **Claude Code**, **Google Antigravity**, **Cursor**, **Codex**, and **terminal operators**.

---

## ⚡ Slash Commands Matrix

Khaos Forge arms agents and human operators with instant high-impact commands:

| Command | Action | Operational Runbook |
| :--- | :--- | :--- |
| **`/khaos <target>`** | Launch autonomous pentest loop and PTT orchestrator | `skills/khaos-orchestrator` |
| **`/recon <target>`** | Passive OSINT, port scanning, and HTTP probing | `skills/recon-asset-discovery` |
| **`/web-audit <url>`** | OWASP WSTG web, GraphQL, JWT, and API assessment | `skills/web-vulnerability-audit` |
| **`/net-audit <ip>`** | Active Directory, Kerberos, SMB, and network services | `skills/network-service-audit` |
| **`/bin-triage <file>`** | Checksec, Radare2, memory corruption, and firmware triage | `skills/binary-reversing-triage` |
| **`/scope-lock <scope>`** | Enforce CIDR/FQDN rules of engagement (KhaosMCP) | `skills/scope-and-evidence-gate` |
| **`/verify-poc`** | Evidence Gate: validate raw response diffs to kill hallucinations | `skills/scope-and-evidence-gate` |
| **`/stealth [rate]`** | Telemetry noise budget, ntopng flow control, and OOB listener | `skills/telemetry-stealth-monitor` |
| **`/devsecops [path]`** | Secrets detection (Gitleaks), SAST (Semgrep), and IaC (Trivy) | `skills/devsecops-pipeline-guard` |
| **`/threat-report`** | Compile verified findings into formal STRIDE & CVSS report | `skills/executive-threat-reporting` |

---

## 🏛️ Foundations: The 11 Repositories Synthesis

Khaos Forge unifies the architectures of 11 landmark security and agentic repositories:

1. **[henriqqw/KhaosMCP-Pentester-Agent](https://github.com/henriqqw/KhaosMCP-Pentester-Agent):** Scope boundary enforcement and cryptographic evidence gates.
2. **[GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT):** Pentest Task Tree (PTT) cognitive state machine.
3. **[enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest):** Tooling matrix, CLI binaries, and SecLists.
4. **[microsoft/Security-101](https://github.com/microsoft/Security-101):** STRIDE threat modeling & CVSS metrics.
5. **[aliasrobotics/cai](https://github.com/aliasrobotics/cai):** Execution trace logging & anti-prompt injection defense.
6. **[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills):** Dynamic MITRE ATT&CK / D3FEND procedural skills.
7. **[0xor0ne/awesome-list](https://github.com/0xor0ne/awesome-list):** Low-level binary reversing, checksec, and firmware audits.
8. **[amark/gun](https://github.com/amark/gun):** Decentralized P2P graph state synchronization for multi-agent swarms.
9. **[CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects):** Active Directory & SIEM validation environments.
10. **[ntop/ntopng](https://github.com/ntop/ntopng):** Real-time network DPI, noise budgeting, and OOB listeners.
11. **[fr0gger/Awesome-GPT-Agents](https://github.com/fr0gger/Awesome-GPT-Agents):** Role division (Scout, Web Auditor, Reverser, Reporter).

---

## 💻 CLI Usage (Terminal Operator Mode)

Khaos Forge includes a standalone CLI executable in `bin/`:

```bash
# Verify or enforce scope
./bin/khaos scope-lock --domains target.com --cidrs 192.168.1.0/24 --check api.target.com

# Launch surface discovery
./bin/khaos recon target.com

# Cryptographically verify candidate finding
./bin/khaos verify-poc --vuln-type "SQLi" --target "https://target.com/api" \
  --poc "curl -s 'https://target.com/api?id=1%27'" \
  --req "GET /api?id=1' HTTP/1.1" \
  --res "SQL syntax error near..." \
  --regex "syntax error"
```

---

## 📦 Cross-Platform Agent Installation

### 1. Google Antigravity
Clone directly into your global skills or workspace:
```bash
git clone https://github.com/SEU_USUARIO/khaos-forge.git ~/.agents/skills/khaos-forge
```

### 2. Claude Code / Cursor MCP
Add the server entry to your MCP configuration:
```json
{
  "mcpServers": {
    "khaos-forge": {
      "command": "python",
      "args": [
        "C:/Users/lucas/OneDrive/Desktop/Projetos/khaos-forge/src/apex_core/mcp_server.py"
      ]
    }
  }
}
```

---

## 🧪 Testing

```bash
python -m unittest discover -s tests
```

---

## 👤 Author & Maintainer

* **Author:** dj
* **Framework:** Khaos Forge
* **License:** Apache License 2.0 (Copyright 2026 dj)
