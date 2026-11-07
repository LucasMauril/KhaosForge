---
name: devsecops-pipeline-guard
description: Use when auditing CI/CD pipelines, container images, Infrastructure-as-Code (Terraform/K8s), secrets leaks, and static source code (SAST).
---

# DevSecOps Pipeline Guard: Automated CI/CD & IaC Security

Integrates security verification directly into software development workflows, pull requests, container builds, and cloud configurations.

## 1. Secrets Detection & Leak Prevention
Scan repositories and commit histories before build execution:
```bash
gitleaks detect --source=. --verbose --report-format=json --report-path=gitleaks_report.json
```

## 2. Static Application Security Testing (SAST)
Execute high-speed rule-based code auditing with Semgrep:
```bash
semgrep scan --config=auto --json -o semgrep_report.json .
```

## 3. Container & Dependency Vulnerability Scanning (SCA)
Audit Dockerfiles, container base images, and lockfiles:
```bash
trivy fs --scanners vuln,misconfig,secret --severity HIGH,CRITICAL .
```

## 4. Infrastructure as Code (IaC) Auditing
Evaluate Kubernetes manifests, Helm charts, and Terraform files against CIS benchmarks:
```bash
checkov -d . --framework terraform,kubernetes --output json
```
