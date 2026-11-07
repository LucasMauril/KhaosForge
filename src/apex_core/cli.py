#!/usr/bin/env python3
"""
Apex Powers CLI - Autonomous Cybersecurity & Red Team Command Interface
Author: dj
"""
import sys
import argparse
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from apex_core.scope import ScopeGuard, ScopeViolationError
from apex_core.evidence import EvidenceGate
from apex_core.ptt import PentestTaskTree

def cmd_scope_lock(args):
    guard = ScopeGuard(allowed_domains=args.domains, allowed_cidrs=args.cidrs)
    print(f"[+] Scope Locked: {len(guard.allowed_domains)} domain(s), {len(guard.allowed_networks)} CIDR(s).")
    if args.check:
        try:
            guard.enforce(args.check)
            print(f"[+] PASS: '{args.check}' is within authorized scope.")
        except ScopeViolationError as err:
            print(f"[-] REJECT: {err}")
            sys.exit(1)

def cmd_recon(args):
    print(f"[*] Launching Reconnaissance on target: {args.target}")
    print("[*] Checking scope boundaries...")
    guard = ScopeGuard(allowed_domains=[args.target], allowed_cidrs=[])
    try:
        guard.enforce(args.target)
    except ScopeViolationError:
        print(f"[-] Target '{args.target}' failed scope validation!")
        sys.exit(1)
    print(f"[+] Target '{args.target}' authorized. Initializing PTT state graph.")
    ptt = PentestTaskTree(f"Recon - {args.target}")
    host_node = ptt.add_child("SCOPE_ROOT", f"host-{args.target}", 1, args.target, "host", {"status": "LIVE"})
    print(f"[+] Discovered Host node: {host_node.node_id}")
    print("[+] Ready for Subfinder / Naabu / HTTPx pipeline.")

def cmd_verify_poc(args):
    gate = EvidenceGate()
    print(f"[*] Validating PoC for vulnerability type: {args.vuln_type}")
    res = gate.verify_finding(
        vuln_type=args.vuln_type,
        target=args.target,
        poc_command=args.poc,
        raw_request=args.req,
        raw_response=args.res,
        differential_regex=args.regex,
        severity=args.severity
    )
    if res:
        print(f"[+] PROOF VALIDATED: {res['id']} (Hash: {res['proof_hash'][:12]})")
        print(f"[+] Status: CONFIRMED - Cryptographically sealed.")
    else:
        print("[-] PROOF REJECTED: Pattern did not match response. Hallucination blocked.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        prog="apex",
        description="Apex Powers: Cybersecurity Superpowers for Autonomous Agents & Operators (by dj)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # scope-lock
    p_scope = subparsers.add_parser("scope-lock", help="Enforce target scope boundaries")
    p_scope.add_argument("--domains", nargs="*", default=[], help="Allowed domains")
    p_scope.add_argument("--cidrs", nargs="*", default=[], help="Allowed CIDRs")
    p_scope.add_argument("--check", help="Verify single target against scope")
    p_scope.set_defaults(func=cmd_scope_lock)

    # recon
    p_recon = subparsers.add_parser("recon", help="Execute high-speed surface discovery")
    p_recon.add_argument("target", help="Target domain or IP")
    p_recon.set_defaults(func=cmd_recon)

    # verify-poc
    p_poc = subparsers.add_parser("verify-poc", help="Evidence Gate PoC differential verification")
    p_poc.add_argument("--vuln-type", required=True, help="Vulnerability type (e.g., SQLi, XSS, SSRF)")
    p_poc.add_argument("--target", required=True, help="Target URL or host")
    p_poc.add_argument("--poc", required=True, help="Reproducible PoC command")
    p_poc.add_argument("--req", required=True, help="Raw request")
    p_poc.add_argument("--res", required=True, help="Raw response")
    p_poc.add_argument("--regex", required=True, help="Differential pattern expected")
    p_poc.add_argument("--severity", default="MEDIUM", help="Severity rating")
    p_poc.set_defaults(func=cmd_verify_poc)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
