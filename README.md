# Apex Cybersecurity Skills Framework

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Protocol](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io/)
[![CI](https://img.shields.io/badge/CI-Passing-success.svg)](.github/workflows/validate-skills.yml)

Enterprise-grade autonomous penetration testing, DevSecOps, and red team agent skills framework. Built for AI coding assistants, terminal agents, and autonomous swarms across **Claude Code**, **Google Antigravity**, **Cursor**, and **OpenCode**.

---

## 🏛️ Architectural Heritage

`apex-cybersecurity-skills` synthesizes and formalizes the design patterns of 11 landmark open-source projects:

1. **[henriqqw/KhaosMCP-Pentester-Agent](https://github.com/henriqqw/KhaosMCP-Pentester-Agent):** Model Context Protocol (MCP) server architecture, strict pre-flight scope enforcement, and differential evidence gates.
2. **[GreyDGL/PentestGPT](https://github.com/GreyDGL/PentestGPT):** Pentest Task Tree (PTT) cognitive state machine for anti-context saturation.
3. **[enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest):** Curated matrix of CLI security binaries, wordlists, and tooling.
4. **[microsoft/Security-101](https://github.com/microsoft/Security-101):** STRIDE threat modeling taxonomies and CVSS v3.1/v4.0 reporting metrics.
5. **[aliasrobotics/cai](https://github.com/aliasrobotics/cai):** Execution trace logging, runner engine, and active defense against indirect prompt injection.
6. **[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills):** Modular `SKILL.md` runbooks mapped to MITRE ATT&CK, NIST CSF 2.0, and D3FEND.
7. **[0xor0ne/awesome-list](https://github.com/0xor0ne/awesome-list):** Low-level binary reversing, checksec auditing, and firmware disassembly.
8. **[amark/gun](https://github.com/amark/gun):** Offline-first, decentralized P2P graph state synchronization for distributed agent swarms.
9. **[CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects):** Validation testbed topologies (Active Directory & SIEM environments).
10. **[ntop/ntopng](https://github.com/ntop/ntopng):** Real-time network DPI, noise budget rate limiting, and out-of-band (OOB) vulnerability listeners.
11. **[fr0gger/Awesome-GPT-Agents](https://github.com/fr0gger/Awesome-GPT-Agents):** Specialized micro-agent personas (Scout, Web Auditor, Reverser, Executive Reporter).

---

## 🧩 System Architecture

```
+----------------------------------------------------------------------------------------------------+
| 1. AGENT ORCHESTRATOR & PROMPT RUNNER (Claude Code / Antigravity / Cursor / Local LLM)             |
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
| 3. COGNITIVE ENGINE & STATE                      |             | 4. CONTROL & VERIFICATION GATES   |
|    - Pentest Task Tree (`ptt.py`)                |             |    - Scope Guard (`scope.py`)     |
|    - P2P Swarm Graph Mesh (`swarm_mesh.py`)      |             |    - Evidence Gate (`evidence.py`)|
+--------------------------------------------------+             +-----------------------------------+
                 │                                                                 │
                 └────────────────────────────────┬────────────────────────────────┘
                                                  ▼
+----------------------------------------------------------------------------------------------------+
| 5. MODULAR PROCEDURAL SKILLS (`skills/`)                                                           |
|    ├── apex-orchestrator           ├── network-service-audit       ├── devsecops-pipeline-guard      |
|    ├── scope-and-evidence-gate     ├── binary-reversing-triage     ├── executive-threat-reporting    |
|    └── recon-asset-discovery       ├── web-vulnerability-audit    └── telemetry-stealth-monitor     |
+----------------------------------------------------------------------------------------------------+
                                                  │
+----------------------------------------------------------------------------------------------------+
| 6. ISOLATED TOOL EXECUTION SANDBOX (Docker: Kali Rolling + ProjectDiscovery Suite + SecLists)       |
+----------------------------------------------------------------------------------------------------+
```

---

## 📂 Repository Directory Layout

```
apex-cybersecurity-skills/
├── .github/
│   └── workflows/
│       └── validate-skills.yml    # Automated CI/CD skill validator and unit test runner
├── docker/
│   ├── Dockerfile.tools           # Sandboxed Kali container with Nmap, Nuclei, HTTPx, Katana, etc.
│   └── docker-compose.yml         # Compose configuration with volume persistence
├── skills/
│   ├── apex-orchestrator/         # Master swarm & PTT state machine coordinator
│   ├── scope-and-evidence-gate/   # Hard CIDR/FQDN boundaries & PoC cryptographic sealing
│   ├── recon-asset-discovery/     # High-speed OSINT, DNS, and HTTP probing runbooks
│   ├── web-vulnerability-audit/   # OWASP WSTG, Nuclei, FFUF, SQLMap, GraphQL, and JWT procedures
│   ├── network-service-audit/     # Active Directory, Kerberos, SMB, and network daemon audits
│   ├── binary-reversing-triage/   # Radare2, Checksec, GDB, and firmware analysis
│   ├── telemetry-stealth-monitor/ # Network DPI, noise budgeting, and out-of-band listener
│   ├── devsecops-pipeline-guard/  # SAST, DAST, Secrets detection (Gitleaks, Semgrep, Trivy)
│   └── executive-threat-reporting/# Formal STRIDE threat matrix and CVSS v3.1/v4.0 scoring
├── src/
│   └── apex_core/
│       ├── __init__.py
│       ├── scope.py               # Pre-flight ScopeGuard implementation
│       ├── evidence.py            # EvidenceGate differential verification engine
│       ├── ptt.py                 # Hierarchical Pentest Task Tree manager
│       ├── swarm_mesh.py          # Decentralized P2P state synchronization client
│       └── mcp_server.py          # Standard Model Context Protocol (MCP) server
├── tests/
│   └── test_core.py               # 100% passing automated unit test suite
├── package.json                   # Standard package manifest and scripts
├── plugin.json                    # Universal agent plugin descriptor
├── gemini-extension.json          # Antigravity extension registration
├── LICENSE                        # Apache-2.0 Open Source License
└── README.md
```

---

## 🚀 Installation & Integration

### Option A: Install in Google Antigravity
The skill is compatible natively. Clone into your global skills or workspace:
```bash
git clone https://github.com/<your-username>/apex-cybersecurity-skills.git ~/.agents/skills/apex-cybersecurity-skills
```

### Option B: Install in Claude Code / Cursor MCP
Add the MCP server to your `claude_desktop_config.json` or `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "apex-cybersecurity": {
      "command": "python",
      "args": [
        "/path/to/apex-cybersecurity-skills/src/apex_core/mcp_server.py"
      ]
    }
  }
}
```

### Option C: Build the Docker Tool Sandbox
```bash
docker build -t apex-tools-sandbox -f docker/Dockerfile.tools .
docker run -d --name apex-tools-sandbox apex-tools-sandbox tail -f /dev/null
```

---

## 🧪 Running Unit Tests

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

## 🛡️ License

Licensed under the [Apache License, Version 2.0](LICENSE).
