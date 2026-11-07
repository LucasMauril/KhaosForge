# Khaos Forge

Khaos Forge is a complete autonomous cybersecurity, penetration testing, and red team methodology for your coding agents, built on top of a set of composable skills, an ironclad scope and evidence protocol, and initial instructions that make sure your agent uses them.

---

## Table of Contents

* [How it works](#how-it-works)
* [Getting Started (Installation)](#installation)
  * [Antigravity](#antigravity)
  * [Claude Code](#claude-code)
  * [Cursor](#cursor)
  * [Codex CLI & App](#codex-cli--app)
  * [Devin CLI](#devin-cli)
  * [Gemini CLI](#gemini-cli)
  * [GitHub Copilot CLI](#github-copilot-cli)
  * [Grok Build CLI](#grok-build-cli)
  * [OpenCode](#opencode)
  * [Pi](#pi)
  * [Standalone Terminal CLI](#standalone-terminal-cli)
  * [Docker Sandbox Arsenal](#docker-sandbox-arsenal)
* [The Basic Workflow](#the-basic-workflow)
* [When Something Goes Wrong](#when-something-goes-wrong)
* [Community & Author](#community--author)
* [What's Inside](#whats-inside)
  * [Skills Library](#skills-library)
  * [Core Python Engine](#core-python-engine)
  * [Docker Arsenal](#docker-arsenal)
* [Philosophy](#philosophy)
* [Contributing](#contributing)
* [Updating](#updating)
* [License](#license)
* [Zero-Telemetry Guarantee](#zero-telemetry-guarantee)

---

## How it works

It starts from the moment you fire up your security or coding agent. As soon as it sees that you're evaluating or auditing a target, it doesn't just jump into blindly firing random exploit payloads or running noisy port sweeps.

Instead, it steps back and enforces your rules of engagement.

First, it validates the target through **`ScopeGuard`**. If an IP, CIDR block, or domain is outside the authorized scope, execution halts immediately before a single packet can be sent to the network.

Once boundaries are locked, your agent initializes the **Pentest Task Tree (PTT)**. Instead of dumping megabytes of raw Nmap, HTTPx, or Nuclei logs directly into the prompt and burning your context window, it organizes the target hierarchically (`Scope > Host > Port/Service > Endpoint > Vulnerability Hypothesis`). The model only ever sees the concise, focused context of the node it is actively assessing.

Next up, when you give the command, it launches a specialized agent loop:
1. **Surface Discovery:** Maps subdomains, open ports, and live HTTP services.
2. **Just-In-Time Skill Loading:** When it encounters a specific service (like Kerberos, GraphQL, or JWT), it dynamically pulls the exact MITRE ATT&CK or OWASP WSTG runbook for that technology.
3. **Evidence Gate:** This is where Khaos Forge fundamentally differs from standard LLM setups. Before a finding can be accepted, it must pass through the **`EvidenceGate`**. The agent must provide a reproducible command (`curl`, Python snippet, or packet trace) and prove that the raw server response contains a verifiable differential signature. Findings without raw proof are discarded as hallucinations.
4. **Decentralized Swarm Sync:** If you're running multiple agent instances across cloud VPSs or local workstations, discoveries sync in real time via an offline-first P2P graph (GunDB).

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically via slash commands or agent prompt matches, you don't need to do anything special. Your security agent just has **Khaos Forge**.

---

## Installation

Installation differs by harness. If you use more than one, install Khaos Forge separately for each one.

### Antigravity

Install Khaos Forge as a plugin or skill from this repository:
```bash
agy plugin install https://github.com/LucasMauril/Khaos-Forge
```
Or clone it directly into your global agent skills folder:
```bash
git clone https://github.com/LucasMauril/Khaos-Forge.git ~/.agents/skills/khaos-forge
```
Antigravity automatically loads the `GEMINI.md` context and exposes all slash commands (`/khaos`, `/recon`, `/web-audit`, etc.).

### Claude Code

Khaos Forge connects natively to Claude Code via the Model Context Protocol (MCP) and custom plugin descriptors.

Install via local checkout:
```bash
claude plugin install /path/to/khaos-forge
```
Or register the MCP server directly in `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "khaos-forge": {
      "command": "python",
      "args": ["/path/to/khaos-forge/src/apex_core/mcp_server.py"]
    }
  }
}
```

### Cursor

In Cursor, add Khaos Forge as an MCP server in `.cursor/mcp.json` or under **Cursor Settings > Features > MCP**:
```json
{
  "mcpServers": {
    "khaos-forge": {
      "command": "python",
      "args": ["/path/to/khaos-forge/src/apex_core/mcp_server.py"]
    }
  }
}
```

### Codex CLI & App

In the Codex App:
1. Open **Plugins** in the sidebar.
2. Add custom repository: `https://github.com/LucasMauril/Khaos-Forge`.
3. Follow the prompts to enable.

In Codex CLI:
```bash
codex plugins install https://github.com/LucasMauril/Khaos-Forge
```

### Devin CLI

Install the plugin from this repository:
```bash
devin plugins install LucasMauril/Khaos-Forge
```
Update to the latest version with:
```bash
devin plugins update khaos-forge
```

### Gemini CLI

Install the extension:
```bash
gemini extensions install https://github.com/LucasMauril/Khaos-Forge
```
Update later with:
```bash
gemini extensions update khaos-forge
```

### GitHub Copilot CLI

Register and install the plugin:
```bash
copilot plugin marketplace add LucasMauril/Khaos-Forge
copilot plugin install khaos-forge
```

### Grok Build CLI

Install the plugin:
```bash
grok plugin install khaos-forge@custom --trust
```

### OpenCode

Tell OpenCode:
```
Fetch and follow instructions from https://raw.githubusercontent.com/LucasMauril/Khaos-Forge/main/rules/AGENTS.md
```

### Pi

Install Khaos Forge as a Pi package from this repository:
```bash
pi install git:github.com/LucasMauril/Khaos-Forge
```
For local development:
```bash
pi -e /path/to/khaos-forge
```

### Standalone Terminal CLI

Khaos Forge doesn't require an LLM interface to be useful. It comes with a standalone executable CLI:

```powershell
cd ./khaos-forge

# Windows native:
.\bin\khaos.cmd --help
.\bin\khaos.cmd scope-lock --domains target.com --cidrs 192.168.1.0/24 --check api.target.com
.\bin\khaos.cmd recon target.com

# Linux / macOS / WSL:
./bin/khaos --help
```

### Docker Sandbox Arsenal

Run the isolated Kali container bundling all CLI tools (Subfinder, Nuclei, Nmap, SecLists, etc.):
```bash
cd docker
docker-compose up -d
```

---

## The Basic Workflow

Khaos Forge coordinates operations across discrete, specialized skills:

* **`scope-and-evidence-gate`** — Activates before any command or tool execution. Parses and enforces CIDR subnets and FQDNs. Rejects out-of-scope targets before any packet leaves the host.
* **`recon-asset-discovery`** — Activates after scope lock. Runs passive OSINT (Subfinder), fast port sweeps (Naabu), HTTP fingerprinting (HTTPx), and crawling (Katana). Ingests results into the task tree.
* **`khaos-orchestrator`** — Activates with scope and recon data. Builds the Pentest Task Tree (PTT) and directs subagents to audit specific services without cross-polluting token context.
* **`web-vulnerability-audit`** — Activates when web/API endpoints are detected. Evaluates OWASP WSTG vectors (SQLi, BOLA, JWT signature bypasses, SSRF, GraphQL traversal) using Nuclei and FFUF.
* **`network-service-audit`** — Activates on infrastructure targets. Performs deep service fingerprinting (Nmap), SMB share auditing, and Active Directory Kerberos evaluation (AS-REP roasting, Kerberoasting).
* **`binary-reversing-triage`** — Activates on compiled binaries (ELF/PE) or IoT firmware. Runs Checksec, Radare2 disassembly, and Binwalk unpacking.
* **`telemetry-stealth-monitor`** — Runs alongside active scans. Monitors packet throughput, throttles on TCP `RST` spikes, and listens for out-of-band (OOB) blind callbacks.
* **`devsecops-pipeline-guard`** — Activates on repositories and CI/CD pipelines. Audits secrets leaks (Gitleaks), code flaws (Semgrep), and container posture (Trivy).
* **`executive-threat-reporting`** — Activates at assessment completion. Verifies all cryptographic proof hashes, categorizes findings under STRIDE, computes CVSS v3.1/v4.0 scores, and outputs remediation blueprints.

The agent checks for relevant skills before every task. Mandatory workflows, not suggestions.

---

## When Something Goes Wrong

Sometimes an autonomous session misbehaves: a subagent gets stuck in a recursive crawl, a tool times out, or the agent repeatedly attempts an out-of-scope target. 

Khaos Forge provides three layers of defense:
1. **Scope Violation Drops:** The `ScopeGuard` raises a hard exception that forces the agent to report the out-of-scope boundary and skip to the next task tree node.
2. **Hallucination Rejection:** If an agent drafts a finding that cannot be reproduced against the raw response, `EvidenceGate` marks it `REJECTED`, preventing false reports.
3. **Session Re-anchoring:** Ask your agent: `"Khaos status"` or `"audit current task tree"` to inspect the SQLite/P2P graph and see exactly which nodes are `PENDING`, `IN_PROGRESS`, or `COMPLETED`.

---

## Community & Author

Khaos Forge is engineered by **dj**.
* **Lead Architect:** **Lucas Mauril**
* **Repository:** `https://github.com/LucasMauril/Khaos-Forge`
* **Issues & Bug Reports:** `https://github.com/LucasMauril/Khaos-Forge/issues`

---

## What's Inside

### Skills Library

#### Control & Safety Gates
* **`scope-and-evidence-gate`** — Inviolable CIDR/FQDN enforcement & cryptographic SHA-256 evidence sealing.
* **`telemetry-stealth-monitor`** — Noise budgeting, rate throttling, and OOB callback listeners.

#### Offensive & Assessment Operations
* **`recon-asset-discovery`** — High-speed OSINT, subdomain discovery, port probing, and web crawling.
* **`web-vulnerability-audit`** — OWASP WSTG web, REST/GraphQL API, and token authentication testing.
* **`network-service-audit`** — Active Directory, SMB null sessions, Kerberos roasting, and network services.
* **`binary-reversing-triage`** — Low-level mitigation auditing (Checksec), disassembly (Radare2), and firmware analysis.

#### DevSecOps & Governance
* **`devsecops-pipeline-guard`** — Secrets detection (Gitleaks), SAST (Semgrep), and container security (Trivy).
* **`executive-threat-reporting`** — STRIDE classification, CVSS v3.1/v4.0 scoring, and executive markdown reports.

#### Meta & Orchestration
* **`khaos-orchestrator`** — Master cognitive runner, Pentest Task Tree (PTT) manager, and dynamic skill loader.

### Core Python Engine (`src/apex_core/`)
* **`scope.py`** — Fast IP/CIDR/FQDN validator with zero external dependencies.
* **`evidence.py`** — Differential response analyzer and cryptographic evidence sealer.
* **`ptt.py`** — Pentest Task Tree state machine with context pruning.
* **`swarm_mesh.py`** — Decentralized P2P state synchronization client (GunDB pattern).
* **`mcp_server.py`** — JSON-RPC 2.0 Model Context Protocol server over stdio.
* **`cli.py`** — Native command-line interface for human operators.

### Docker Arsenal (`docker/`)
* Bundles Kali Linux Rolling, ProjectDiscovery Suite (`subfinder`, `httpx`, `naabu`, `katana`, `nuclei`), `nmap`, `masscan`, `sqlmap`, `ffuf`, `radare2`, and `SecLists`.

---

## Philosophy

* **Inviolable Scope** — An agent that touches out-of-scope targets is a liability. Scope validation is non-negotiable and runs pre-execution.
* **Evidence Over Claims** — Never declare a vulnerability based on soft probability or banner matching. A finding is only real when a reproducible PoC and differential response prove it.
* **Cognitive Context Hygiene** — Large language models degrade when flooded with terminal noise. Prune context aggressively using hierarchical task trees.
* **Process Over Guesswork** — Follow established standards: OWASP WSTG for web, MITRE ATT&CK for red teaming, and STRIDE for threat modeling.
* **Local-First & Offline Resilience** — No mandatory external SaaS telemetry. Your findings and attack surface data stay on your machine.

---

## Contributing

1. Fork the repository.
2. Create a branch for your work (`git checkout -b feat/new-skill`).
3. Follow the `SKILL.md` format (YAML frontmatter with `name`, `author`, `description`, and exact procedural steps).
4. Run unit tests before submitting:
   ```bash
   python -m unittest discover -s tests
   ```
5. Submit a Pull Request.

---

## Updating

To update Khaos Forge:
```bash
cd /path/to/khaos-forge
git pull origin main
```
To update all 11 upstream reference repositories in `references/`:
```bash
python scripts/sync_references.py
```

---

## License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.  
Copyright (c) 2026 **Lucas Mauril**.

---

## Zero-Telemetry Guarantee

Khaos Forge collects **zero** telemetry. No usage stats, target domains, IP addresses, or scan outputs are ever transmitted to any third party. All state is stored locally on your machine or inside your own private P2P swarm mesh.
