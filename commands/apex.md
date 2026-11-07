---
name: apex
description: Launch full autonomous red team assessment and orchestrate Pentest Task Tree.
arguments:
  - name: target
    description: Target domain, IP, or CIDR block
    required: true
---

# /apex Command

Launch the autonomous red team engine on `$target`.

## Execution Steps
1. Verify `$target` against the Scope Guard. If out of scope, halt immediately.
2. Initialize the Pentest Task Tree (`PTT`) root node with `$target`.
3. Dispatch the Scout agent (`/recon $target`) to enumerate subdomains, ports, and live HTTP services.
4. For every discovered service:
   - Web ports (80, 443, 8080) $\rightarrow$ invoke `/web-audit`.
   - Network services (445, 88, 389) $\rightarrow$ invoke `/net-audit`.
   - Custom binaries $\rightarrow$ invoke `/bin-triage`.
5. Pipe all candidate vulnerabilities through `/verify-poc`.
6. Compile final report with `/threat-report`.
