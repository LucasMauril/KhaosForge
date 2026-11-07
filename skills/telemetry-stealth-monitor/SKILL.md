---
name: telemetry-stealth-monitor
author: dj
description: Use when monitoring network flow telemetry, managing noise budgets, evading rate limits, or capturing out-of-band (OOB) vulnerability callbacks.
---

# Telemetry & Stealth Monitor: Network Flow & Rate Control

Enforces network operational hygiene, monitors noise budgets, detects firewall backoff signals, and tracks out-of-band callbacks.

## 1. Noise Budget Calculation
* **Baseline Scan Rate:** Limit to 100-150 packets/sec for initial sweeps.
* **Jitter Control:** Inject random sleep intervals (150ms to 800ms) between sequential HTTP requests.
* **Burst Detection:** Calculate packets sent over a rolling 10-second window.

## 2. Firewall & Rate-Limiting Triggers
* **TCP Reset (`RST`) Spike:** If `RST` ratio exceeds 10% of total packets, reduce transmission rate by 50%.
* **HTTP 429 / 403 Flood:** Trigger a 90-second cooldown period on that specific host/IP and rotate User-Agent strings.

## 3. Out-of-Band (OOB) Callback Verification
When testing for blind vulnerabilities (Blind SSRF, Blind SQLi, Blind RCE):
* Generate unique token per test: `<CANARY_ID>.oob.target.corp`.
* Monitor DNS queries and HTTP connections on the dedicated listener.
* Treat any callback matching `<CANARY_ID>` as deterministic proof.
