---
name: devsecops
description: Audit CI/CD pipelines, SAST code, secrets leaks, and Infrastructure-as-Code.
arguments:
  - name: path
    description: Path to repository or directory (default current directory)
    required: false
---

# /devsecops Command

Execute automated DevSecOps security audit on `$path`.

## Execution Steps
1. Scan for leaked secrets and credentials using `gitleaks`.
2. Run Static Application Security Testing (SAST) with `semgrep`.
3. Audit dependencies and container configurations with `trivy`.
4. Scan Terraform and Kubernetes manifests with `checkov`.
