---
name: threat-report
description: Compile all verified findings into an executive STRIDE and CVSS v3.1/v4.0 markdown report.
arguments: []
---

# /threat-report Command

Compile the final assessment report from verified findings in `EvidenceGate`.

## Execution Steps
1. Collect all findings marked as `CONFIRMED`.
2. Classify each finding under STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege).
3. Compute CVSS base scores and vectors.
4. Export executive markdown summary with reproducible PoCs, SHA-256 evidence hashes, and actionable remediation steps.
