---
name: stealth
description: Configure network telemetry, noise budget, rate limits, and OOB listener.
arguments:
  - name: rate_limit
    description: Maximum packets or requests per second (default 100)
    required: false
---

# /stealth Command

Configure traffic parameters and noise budgets.

## Execution Steps
1. Set max throughput to `$rate_limit` pkts/sec.
2. Enable jitter backoff (150ms-800ms between requests).
3. Monitor `ntopng` flow counters. If TCP `RST` ratio exceeds 10%, throttle rate by 50%.
4. Spin up the out-of-band (OOB) DNS/HTTP callback listener for blind vulnerability tests.
