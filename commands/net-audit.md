---
name: net-audit
description: Execute network service audit, Active Directory, SMB, and Kerberos assessment.
arguments:
  - name: target
    description: Target IP address or range
    required: true
---

# /net-audit Command

Audit network infrastructure and Active Directory on `$target`.

## Execution Steps
1. Verify `$target` against Scope Guard.
2. Run deep service scanning: `nmap -sV -sC -Pn $target`.
3. If SMB (445) is open, probe null sessions and share permissions.
4. If Kerberos (88) is open, test for AS-REP roasting and Kerberoasting.
5. Record raw service banner diffs for verification.
