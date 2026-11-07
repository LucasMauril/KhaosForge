---
name: web-audit
description: Execute OWASP WSTG web application, API, and business logic audit.
arguments:
  - name: url
    description: Target web application URL
    required: true
---

# /web-audit Command

Audit the web application at `$url` following OWASP WSTG standards.

## Execution Steps
1. Verify `$url` against Scope Guard.
2. Crawl endpoints and parameters using `katana`.
3. Execute targeted template scans using `nuclei` (tags: cve, misconfig, auth).
4. Fuzz routes and hidden parameters with `ffuf`.
5. For any candidate finding, generate raw request/response transcripts for `/verify-poc`.
