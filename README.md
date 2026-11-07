<div align="center">

```
  ██╗  ██╗██╗  ██╗ █████╗  ██████╗ ███████╗   ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
  ██║ ██╔╝██║  ██║██╔══██╗██╔═══██╗██╔════╝   ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
  █████═╝ ███████║███████║██║   ██║███████╗   █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
  ██╔═██╗ ██╔══██║██╔══██║██║   ██║╚════██║   ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
  ██║ ╚██╗██║  ██║██║  ██║╚██████╔╝███████║   ██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```

### **Autonomous Cybersecurity Forge, Red Team Swarms & DevSecOps Engine**
*Engineered by **dj** for Claude Code, Google Antigravity, Cursor, and Terminal Operators.*

---

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Protocol: MCP](https://img.shields.io/badge/Protocol-MCP%20Stdio%2FSSE-purple.svg)](https://modelcontextprotocol.io/)
[![Author: dj](https://img.shields.io/badge/Author-dj-red.svg)](https://github.com/dj)
[![Test Suite: Passing](https://img.shields.io/badge/Tests-100%25%20Passing-success.svg)](tests/test_core.py)
[![Docker: Ready](https://img.shields.io/badge/Docker-Sandboxed%20Arsenal-orange.svg)](docker/Dockerfile.tools)

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [The Three Pillars](#-the-three-pillars)
- [Slash Commands Matrix](#-slash-commands-matrix)
- [Architecture Blueprint](#-architecture-blueprint)
- [Tool Arsenal (Docker Sandbox)](#-tool-arsenal-docker-sandbox)
- [Installation & Setup](#-installation--setup)
  - [1. Google Antigravity](#1-google-antigravity)
  - [2. Claude Code & Cursor MCP](#2-claude-code--cursor-mcp)
  - [3. Terminal CLI Mode](#3-terminal-cli-mode)
  - [4. Docker Tool Sandbox](#4-docker-tool-sandbox)
- [Operational Walkthrough](#-operational-walkthrough)
- [Foundations: The 11 Repositories](#-foundations-the-11-repositories)
- [Directory Structure](#-directory-structure)
- [Development & Unit Tests](#-development--unit-tests)
- [Author & License](#-author--license)

---

## 🔭 Overview

**Khaos Forge** bridges the gap between Large Language Models and offensive security operations. Standard LLMs hallucinate vulnerabilities, lack execution state, and easily escape defined target perimeters. 

Khaos Forge wraps AI agents inside an ironclad operational shell:
* **Pre-flight boundary enforcement:** Zero unauthorized scans.
* **Cryptographic evidence validation:** Zero hallucinated findings.
* **Hierarchical state management:** Zero context window saturation.
* **Multi-agent swarm coordination:** Decentralized P2P attack graph synchronization.

---

## 🛡️ The Three Pillars

```
       [SCOPE GUARD]                     [EVIDENCE GATE]                 [TASK TREE (PTT)]
   Pre-Flight CIDR & FQDN          Raw Differential Response Diff         Pruned Cognitive Graph
  Hard Boundary Interceptor           Cryptographic SHA-256 Seal          Anti-Context Degradation
```

1. **Inviolable Scope Enforcement (`src/apex_core/scope.py`):**
   Every probe, socket, and CLI tool invocation passes through `ScopeGuard`. Targets outside authorized CIDR blocks or FQDN domains are rejected before network traffic can be generated.
2. **Deterministic Evidence Gate (`src/apex_core/evidence.py`):**
   A vulnerability is discarded as hallucination unless it includes a reproducible command (`curl`, script), a verified differential pattern in the raw response, and a SHA-256 digest of the raw transcript.
3. **Pentest Task Tree (`src/apex_core/ptt.py`):**
   Prevents context drift by maintaining an in-memory/P2P attack surface graph. The LLM receives only high-density summaries of its active target node.

---

## ⚡ Slash Commands Matrix

Like Superpowers, Khaos Forge exposes instant slash commands recognized across all agent environments:

| Slash Command | Operational Scope | Targeted Module |
| :--- | :--- | :--- |
| **`/khaos <target>`** | Full autonomous pentest loop & PTT orchestration | `skills/khaos-orchestrator` |
| **`/recon <target>`** | OSINT surface discovery, port scanning & HTTP probing | `skills/recon-asset-discovery` |
| **`/web-audit <url>`** | OWASP WSTG web, GraphQL, JWT, and API assessment | `skills/web-vulnerability-audit` |
| **`/net-audit <ip>`** | Active Directory, Kerberos, SMB & network services | `skills/network-service-audit` |
| **`/bin-triage <file>`** | Checksec, Radare2, memory corruption & firmware triage | `skills/binary-reversing-triage` |
| **`/scope-lock <scope>`** | Lock CIDR/FQDN rules of engagement (KhaosMCP) | `skills/scope-and-evidence-gate` |
| **`/verify-poc`** | Evidence Gate: validate response diffs & kill hallucinations | `skills/scope-and-evidence-gate` |
| **`/stealth [rate]`** | Noise budget, rate limits, ntopng telemetry & OOB listener | `skills/telemetry-stealth-monitor` |
| **`/devsecops [path]`** | Secrets detection (Gitleaks), SAST (Semgrep) & IaC (Trivy) | `skills/devsecops-pipeline-guard` |
| **`/threat-report`** | Compile findings into formal STRIDE & CVSS v3.1/v4.0 report | `skills/executive-threat-reporting` |

---

## 🏛️ Architecture Blueprint

```
+----------------------------------------------------------------------------------------------------+
| 1. OPERATOR / AGENT HARNESS (Claude Code / Google Antigravity / Cursor / Local LLM)                |
+----------------------------------------------------------------------------------------------------+
                                                  │ (JSON-RPC 2.0 via stdio)
+----------------------------------------------------------------------------------------------------+
| 2. MODEL CONTEXT PROTOCOL (MCP) INTERFACE LAYER (`src/apex_core/mcp_server.py`)                    |
|    - Tool Definition Schemas: Scope Lock, Tool Execution, Evidence Validation                      |
+----------------------------------------------------------------------------------------------------+
                                                  │
                 ┌────────────────────────────────┴────────────────────────────────┐
                 ▼                                                                 ▼
+--------------------------------------------------+             +-----------------------------------+
| 3. COGNITIVE STATE & RUNNER                      |             | 4. CONTROL & VERIFICATION GATES   |
|    - Pentest Task Tree (`ptt.py`)                |             |    - Scope Guard (`scope.py`)     |
|    - P2P Swarm Graph Mesh (`swarm_mesh.py`)      |             |    - Evidence Gate (`evidence.py`)|
+--------------------------------------------------+             +-----------------------------------+
                 │                                                                 │
                 └────────────────────────────────┬────────────────────────────────┘
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 5. MODULAR PROCEDURAL SKILLS (`skills/`)                                                           |
|    ├── khaos-orchestrator          ├── network-service-audit       ├── devsecops-pipeline-guard      |
|    ├── scope-and-evidence-gate     ├── binary-reversing-triage     ├── executive-threat-reporting    |
|    └── recon-asset-discovery       ├── web-vulnerability-audit    └── telemetry-stealth-monitor     |
+----------------------------------------------------------------------------------------------------+
                                                  │
+----------------------------------------------------------------------------------------------------+
| 6. ISOLATED TOOL EXECUTION SANDBOX (Docker: Kali Rolling + ProjectDiscovery Suite + SecLists)       |
+----------------------------------------------------------------------------------------------------+
```

---

## 🧰 Tool Arsenal (Docker Sandbox)

The sandbox container (`docker/Dockerfile.tools`) bundles the entire verified security arsenal:

| Category | Utilities Bundled | Function in Khaos Forge |
| :--- | :--- | :--- |
| **Reconnaissance** | `subfinder`, `naabu`, `httpx`, `dnsutils`, `whois` | High-speed passive discovery, port sweeps, and tech stack fingerprinting. |
| **Web & API** | `katana`, `nuclei`, `ffuf`, `sqlmap`, `nikto` | Deep crawling, OWASP WSTG fuzzing, and template-based vulnerability scans. |
| **Network & AD** | `nmap`, `masscan`, `impacket`, `crackmapexec` | Deep daemon version probing, SMB share audits, and Kerberos roasting. |
| **Binary & Firmware** | `checksec`, `radare2`, `rabin2`, `gdb`, `binwalk` | Mitigation checking (Canaries/NX/PIE), function disassembly, and IoT unpacking. |
| **DevSecOps** | `gitleaks`, `semgrep`, `trivy`, `checkov` | Commit secrets detection, SAST code analysis, and Terraform/K8s posture. |
| **Wordlists** | `SecLists` (raft-medium, common, fuzzing) | Pre-installed in `/opt/seclists` for rapid fuzzing. |

---

## 🚀 Installation & Setup

### 1. Google Antigravity
Clone directly into your global agent skills directory:
```bash
git clone https://github.com/SEU_USUARIO/khaos-forge.git ~/.agents/skills/khaos-forge
```

### 2. Claude Code & Cursor MCP
Add the server entry to your MCP configuration (`claude_desktop_config.json` or `.cursor/mcp.json`):
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

### 3. Terminal CLI Mode
You can invoke Khaos Forge directly from PowerShell or Bash without an agent:

```powershell
cd C:\Users\lucas\OneDrive\Desktop\Projetos\khaos-forge

# 1. Enforce scope boundaries
.\bin\khaos.cmd scope-lock --domains target.com --cidrs 192.168.1.0/24 --check api.target.com

# 2. Launch high-speed reconnaissance
.\bin\khaos.cmd recon target.com

# 3. Validate evidence via differential regex
.\bin\khaos.cmd verify-poc --vuln-type "SQLi" --target "https://target.com/api" `
  --poc "curl -s 'https://target.com/api?id=1%27'" `
  --req "GET /api?id=1' HTTP/1.1" `
  --res "SQL syntax error near..." `
  --regex "syntax error"
```

### 4. Docker Tool Sandbox
```bash
docker-compose -f docker/docker-compose.yml up -d
```

---

## 🕹️ Operational Walkthrough

### Step 1: Pre-Flight Scope Lock
```bash
/scope-lock enterprise.corp,10.20.0.0/16
```
> *ScopeGuard engages. Any attempt to probe subdomains outside `enterprise.corp` or IPs outside `10.20.0.0/16` will be dropped instantly.*

### Step 2: Surface Discovery & Graph Population
```bash
/recon enterprise.corp
```
> *Runs Subfinder, Naabu, and HTTPx. Ingests all discovered ports, endpoints, and technologies directly into the Pentest Task Tree.*

### Step 3: Targeted Web Vulnerability Audit
```bash
/web-audit https://api.enterprise.corp/v1
```
> *Deploys Katana to crawl endpoints and Nuclei for targeted WSTG flaw identification.*

### Step 4: Evidence Verification
```bash
/verify-poc
```
> *Checks candidate findings against differential response indicators and signs them with a SHA-256 hash.*

### Step 5: Report Generation
```bash
/threat-report
```
> *Generates executive STRIDE and CVSS v3.1/v4.0 markdown documentation with exact remediation blueprints.*

---

## 🏛️ Foundations: The 11 Repositories

Khaos Forge unifies the architectures of 11 landmark open-source projects:

1. **[henriqqw/KhaosMCP-Pentester-Agent](https://github.com/henriqqw/KhaosMCP-Pentester-Agent):** Scope boundary enforcement and cryptographic evidence gates.
2. **[GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT):** Pentest Task Tree (PTT) cognitive state machine.
3. **[enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest):** Curated tooling matrix, CLI binaries, and SecLists.
4. **[microsoft/Security-101](https://github.com/microsoft/Security-101):** STRIDE threat modeling & CVSS metrics.
5. **[aliasrobotics/cai](https://github.com/aliasrobotics/cai):** Execution trace logging & anti-prompt injection defense.
6. **[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills):** Dynamic MITRE ATT&CK / D3FEND procedural skills library (818 skills).
7. **[0xor0ne/awesome-list](https://github.com/0xor0ne/awesome-list):** Low-level binary reversing, checksec, and firmware audits.
8. **[amark/gun](https://github.com/amark/gun):** Decentralized P2P graph state synchronization for multi-agent swarms.
9. **[CarterPerez-dev/CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects):** Active Directory & SIEM validation environments.
10. **[ntop/ntopng](https://github.com/ntop/ntopng):** Real-time network DPI, noise budgeting, and OOB listeners.
11. **[fr0gger/Awesome-GPT-Agents](https://github.com/fr0gger/Awesome-GPT-Agents):** Specialized micro-agent personas.

*To synchronize all 11 original repositories locally, run:*
```bash
python scripts/sync_references.py
```

---

## 📂 Directory Structure

```
khaos-forge/
├── .github/
│   └── workflows/
│       └── validate-skills.yml    # CI/CD test runner & skill schema validator
├── bin/
│   ├── khaos                      # Linux/macOS executable CLI
│   └── khaos.cmd                  # Windows native executable CLI
├── commands/                      # Slash command definitions
│   ├── khaos.md                   # /khaos <target>
│   ├── recon.md                   # /recon <target>
│   ├── web-audit.md               # /web-audit <url>
│   ├── net-audit.md               # /net-audit <ip>
│   ├── bin-triage.md              # /bin-triage <file>
│   ├── scope-lock.md              # /scope-lock <scope>
│   ├── verify-poc.md              # /verify-poc
│   ├── stealth.md                 # /stealth [rate]
│   ├── devsecops.md               # /devsecops [path]
│   └── threat-report.md           # /threat-report
├── docker/
│   ├── Dockerfile.tools           # Sandboxed Kali container with ProjectDiscovery suite
│   └── docker-compose.yml         # Container orchestration
├── references/                    # Offline local knowledge vault of all 11 repos
├── rules/
│   ├── AGENTS.md                  # Universal rules of engagement for AI models
│   ├── GEMINI.md                  # Context injection for Google Antigravity
│   └── CLAUDE.md                  # Context injection for Claude Code
├── skills/                        # Modular operational skills
│   ├── khaos-orchestrator/        # Master swarm & PTT state coordinator
│   ├── scope-and-evidence-gate/   # Hard scope rules & PoC cryptographic sealing
│   ├── recon-asset-discovery/     # Surface discovery & OSINT runbooks
│   ├── web-vulnerability-audit/   # OWASP WSTG, Nuclei, FFUF, SQLMap, GraphQL
│   ├── network-service-audit/     # Active Directory, Kerberos, SMB audits
│   ├── binary-reversing-triage/   # Radare2, Checksec, memory corruption
│   ├── telemetry-stealth-monitor/ # Network DPI, noise budget, OOB listener
│   ├── devsecops-pipeline-guard/  # SAST, Secrets detection, IaC posture
│   └── executive-threat-reporting/# STRIDE matrix & CVSS scoring
├── src/
│   └── apex_core/
│       ├── cli.py                 # Standalone CLI interface
│       ├── scope.py               # Pre-flight ScopeGuard
│       ├── evidence.py            # EvidenceGate differential verification
│       ├── ptt.py                 # Hierarchical Pentest Task Tree
│       ├── swarm_mesh.py          # Decentralized P2P state synchronization
│       └── mcp_server.py          # Model Context Protocol stdio server
├── tests/
│   └── test_core.py               # 100% passing automated unit test suite
├── package.json                   # Package manifest & CLI registration
├── plugin.json                    # Universal agent plugin descriptor
├── gemini-extension.json          # Google Antigravity extension descriptor
├── LICENSE                        # Apache-2.0 License (Copyright 2026 dj)
└── README.md
```

---

## 🧪 Development & Unit Tests

Run the test suite to verify core engines:

```bash
python -m unittest discover -s tests
```

Output:
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK
```

---

## 👤 Author & License

* **Author & Lead Architect:** **dj**
* **Framework:** **Khaos Forge**
* **License:** Licensed under the [Apache License, Version 2.0](LICENSE). Copyright (c) 2026 dj.
