---
name: recon
description: Execute attack surface discovery, OSINT, port scanning, and HTTP probing.
arguments:
  - name: target
    description: Target domain or IP
    required: true
---

# /recon Command

Execute reconnaissance and surface mapping on `$target`.

## Execution Steps
1. Run `ScopeGuard.enforce("$target")`.
2. Execute passive subdomain enumeration via `subfinder`.
3. Probe live ports with `naabu`.
4. Fingerprint web services and headers with `httpx`.
5. Ingest all discovered endpoints into the active Pentest Task Tree.
