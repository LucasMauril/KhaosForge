---
name: verify-poc
description: Evidence Gate - validate raw differential response proof to prevent hallucinations.
arguments:
  - name: finding_id
    description: Unique finding ID or draft vulnerability description
    required: true
---

# /verify-poc Command

Validate Proof of Concept through the Evidence Gate.

## Execution Steps
1. Require reproducible CLI command (`curl`, script, packet).
2. Validate differential indicator (string reflection, timing delta, or error banner) in the raw response.
3. Compute SHA-256 hash of `REQ + RESP`.
4. Register finding as `CONFIRMED`. If pattern fails, discard as hallucination.
