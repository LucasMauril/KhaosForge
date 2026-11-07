---
name: recon-asset-discovery
author: dj
description: Use when performing passive OSINT, active DNS enumeration, port scanning, HTTP probing, and attack surface asset discovery.
---

# Recon & Asset Discovery: Surface Mapping Engine

Executes high-speed passive and active reconnaissance to populate the Pentest Task Tree with verified live assets.

## 1. Toolchain & Execution Sequence
1. **Passive Subdomain Enumeration:**
   ```bash
   subfinder -d target.com -all -silent -json -o subdomains.json
   ```
2. **Fast Port Scanning & Service Probing:**
   ```bash
   naabu -l subdomains.txt -p 80,443,8080,8443,8000,8888,445,3389,22,21 -silent -json -o open_ports.json
   ```
3. **HTTP Probing & Fingerprinting:**
   ```bash
   httpx -l open_ports.txt -title -tech-detect -status-code -content-length -follow-redirects -json -o web_assets.json
   ```
4. **Web Crawling & Route Mapping:**
   ```bash
   katana -u web_assets.txt -depth 3 -jc -kf -silent -json -o endpoints.json
   ```

## 2. PTT Graph Ingestion
All JSON lines emitted by `httpx` and `katana` are parsed directly into the attack graph:
* Host: `target.com` (IP: `104.21.5.12`)
* Port: `443` (Service: `https`, WebServer: `nginx`, Tech: `Spring Boot, React`)
* Endpoints: `/api/v1/auth/login`, `/graphql`, `/swagger-ui.html`
