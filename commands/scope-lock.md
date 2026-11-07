---
name: scope-lock
description: Lock and enforce authorized domains and CIDR blocks.
arguments:
  - name: scope
    description: Comma-separated list of domains and CIDRs (e.g., target.com,192.168.1.0/24)
    required: true
---

# /scope-lock Command

Lock target boundaries into `ScopeGuard`.

## Execution Steps
1. Parse `$scope` into domains and IP networks.
2. Store authorized rules in the runtime Scope Enforcer.
3. Terminate any subagent task that attempts to query out-of-scope targets.
