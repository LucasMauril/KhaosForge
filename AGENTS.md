# Apex Powers: Operational Directives for Autonomous Agents

You are operating with **Apex Powers**, the cybersecurity and red team superpower extension authored by **dj**.

## Core Operational Directives

1. **Scope Is Inviolable:** Never execute any probe, request, or scan against a host or IP without first verifying that it exists in the authorized scope (`ScopeGuard`).
2. **Anti-Hallucination Lock:** Never report a vulnerability based on raw guess or generic text. Every finding must pass through `EvidenceGate` with reproducible PoCs and differential response verification.
3. **Task Tree Management:** Keep target discoveries organized in the hierarchical Pentest Task Tree (`PTT`). Prune context to prevent token exhaustion.

## Slash Commands Mapping

When the user enters any of the following slash commands or asks for these tasks, execute the corresponding workflow:

* `/apex <target>` $\rightarrow$ Run full autonomous orchestrator using `skills/apex-orchestrator/SKILL.md`.
* `/recon <target>` $\rightarrow$ Run surface discovery using `skills/recon-asset-discovery/SKILL.md`.
* `/web-audit <url>` $\rightarrow$ Run OWASP WSTG web assessment using `skills/web-vulnerability-audit/SKILL.md`.
* `/net-audit <ip>` $\rightarrow$ Run network infrastructure audit using `skills/network-service-audit/SKILL.md`.
* `/bin-triage <file>` $\rightarrow$ Run binary and firmware reversing using `skills/binary-reversing-triage/SKILL.md`.
* `/scope-lock <scope>` $\rightarrow$ Lock target boundaries using `skills/scope-and-evidence-gate/SKILL.md`.
* `/verify-poc <finding>` $\rightarrow$ Validate PoC evidence using `skills/scope-and-evidence-gate/SKILL.md`.
* `/stealth [rate]` $\rightarrow$ Manage noise budget and telemetry using `skills/telemetry-stealth-monitor/SKILL.md`.
* `/devsecops [path]` $\rightarrow$ Audit code, secrets, and IaC using `skills/devsecops-pipeline-guard/SKILL.md`.
* `/threat-report` $\rightarrow$ Compile STRIDE/CVSS report using `skills/executive-threat-reporting/SKILL.md`.
