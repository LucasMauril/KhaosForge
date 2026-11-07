---
name: khaos-orchestrator
author: Lucas Mauril
description: Use when launching, managing, or coordinating autonomous penetration tests, multi-agent swarms, and cognitive task trees across targets.
---

# Khaos Orchestrator: Master Swarm & PTT Coordinator

Coordinates multi-agent red team operations, synchronizes task trees (PTT), manages dynamic skill loading, and maintains real-time P2P swarm graph convergence within **Khaos Forge**.

## 1. Operating Concept
The Orchestrator operates as the root brain. It decomposes a broad scope into a structured graph:
* **Level 0 (Root):** Target scope parameters and authorization.
* **Level 1 (Hosts):** Discovered IP addresses and active domains.
* **Level 2 (Services):** Open ports, banners, and protocol identification.
* **Level 3 (Endpoints):** HTTP routes, RPC interfaces, and parameters.
* **Level 4 (Hypotheses):** Structured vulnerability tests and evidence validations.

## 2. Dynamic Procedure Dispatching
When child agents report newly fingerprinted services, the Orchestrator pulls targeted procedural runbooks on the fly:
* Port 80/443 $\rightarrow$ Dispatch `web-vulnerability-audit`.
* Port 445/88 $\rightarrow$ Dispatch `network-service-audit`.
* Custom binary daemon $\rightarrow$ Dispatch `binary-reversing-triage`.
* Code repository commit $\rightarrow$ Dispatch `devsecops-pipeline-guard`.

## 3. Swarm Synchronization (P2P GunDB)
All agent instances broadcast and ingest delta updates using Last-Write-Wins (LWW) conflict resolution:
```python
from apex_core.swarm_mesh import SwarmMeshNode
mesh = SwarmMeshNode("scout-node-01")
mesh.publish_update("target.com/hosts", {"ip": "192.168.1.50", "status": "LIVE"})
```

## 4. Execution Guardrails
1. Never execute tools on targets before calling `ScopeGuard.enforce(target)`.
2. Prune context before querying LLM backends using `PentestTaskTree.get_focused_context()`.
3. Require cryptographic confirmation via `EvidenceGate` prior to logging findings.
