---
name: network-service-audit
author: Lucas Mauril
description: Use when auditing network infrastructure, Active Directory environments, SMB shares, SSH/RDP services, and internal routing.
---

# Network Service Audit: Infrastructure & AD Assessment

Provides systematic procedures for auditing network daemons, RPC interfaces, and Active Directory domains.

## 1. Service Enumeration & Fingerprinting
* **Deep Service Version Scanning:**
  ```bash
  nmap -sV -sC -Pn -p 21,22,23,25,53,88,111,139,389,445,1433,1521,3306,3389,5985,5986 -oX nmap_services.xml <TARGET_IP>
  ```
* **SMB Share & Null Session Enumeration:**
  ```bash
  crackmapexec smb <TARGET_IP> -u '' -p '' --shares
  ```
* **Active Directory Kerberos Auditing:**
  * Kerberoasting (`GetUserSPNs.py`).
  * AS-REP Roasting (`GetNPUsers.py`).

## 2. Evidence Verification
Capture the authenticated response, service banner diff, or Kerberos ticket response as raw bytes and generate the cryptographic proof hash.
