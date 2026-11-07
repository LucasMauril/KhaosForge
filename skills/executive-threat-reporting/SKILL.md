---
name: executive-threat-reporting
description: Use when generating professional penetration testing reports, calculating CVSS scores, mapping findings to STRIDE/MITRE ATT&CK, and proposing remediation.
---

# Executive Threat Reporting: STRIDE & CVSS Documentation

Transforms verified findings into formal executive summaries and technical remediation blueprints following Microsoft Security-101 and OWASP standards.

## 1. Classification & Scoring Standard
Every finding must include:
* **STRIDE Category:** Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.
* **CVSS v3.1 / v4.0 Score:** Base Score and Vector String (e.g., `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`).
* **MITRE ATT&CK Technique ID:** e.g., `T1190` (Exploit Public-Facing Application).

## 2. Standard Finding Template

```markdown
### [APEX-VULN-ID] Title of Finding

| Attribute | Value |
| :--- | :--- |
| **Severity** | CRITICAL / HIGH / MEDIUM / LOW |
| **STRIDE** | Tampering / Information Disclosure |
| **CVSS v3.1** | 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) |
| **Target** | `https://api.target.com/v1/user` |
| **Proof Hash** | `a1b2c3d4e5f6...` (SHA-256) |

#### Description
Detailed technical explanation of the root cause and vulnerable component.

#### Reproduction Steps (PoC)
```bash
curl -X POST https://api.target.com/v1/user -H "..."
```

#### Remediation Plan
1. **Immediate:** Configuration tweak or WAF rule.
2. **Permanent:** Code-level fix with defensive architectural guidance.
```
