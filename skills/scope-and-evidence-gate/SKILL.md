---
name: scope-and-evidence-gate
author: dj
description: Use when validating target boundaries, enforcing rules of engagement, or verifying raw differential PoC evidence to eliminate hallucinations.
---

# Scope & Evidence Gate: Safety & Anti-Hallucination Guard

Enforces physical network and hostname boundaries prior to probe execution and mandates deterministic proof of concept verification before accepting vulnerabilities.

## 1. Scope Enforcement Protocol
Before any socket or subprocess command is executed:
* Check IP against `allowed_cidrs`.
* Check FQDN against `allowed_domains` with wildcard suffix validation.
* Reject private network crossovers unless explicitly defined in RFC1918 scope parameters.

```python
from apex_core.scope import ScopeGuard
guard = ScopeGuard(allowed_domains=["target.corp"], allowed_cidrs=["10.10.0.0/16"])
guard.enforce("sub.target.corp") # Passes
guard.enforce("evil.corp")       # Raises ScopeViolationError
```

## 2. Evidence Verification Protocol
Findings are classified as **HALLUCINATION** until passing the three gates:
1. **Replayability:** A standalone `curl` or raw socket command reproduces the anomalous state.
2. **Differential Response:** The response demonstrates a concrete condition delta:
   * String reflection (e.g. Canary `x7e9a1`).
   * SQL error signature or timing variance > 3000ms.
   * Status code variance (e.g., bypass 403 $\rightarrow$ 200).
3. **Cryptographic Sealing:** Generate a SHA-256 hash of the complete raw exchange.

```python
from apex_core.evidence import EvidenceGate
gate = EvidenceGate()
result = gate.verify_finding(
    vuln_type="Reflected XSS",
    target="https://target.corp/search?q=CANARY123",
    poc_command="curl -s 'https://target.corp/search?q=CANARY123'",
    raw_request="GET /search?q=CANARY123 HTTP/1.1\r\nHost: target.corp\r\n\r\n",
    raw_response="HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<div>CANARY123</div>",
    differential_regex="CANARY123"
)
```
