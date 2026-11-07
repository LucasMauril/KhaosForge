import unittest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from apex_core.scope import ScopeGuard, ScopeViolationError
from apex_core.evidence import EvidenceGate
from apex_core.ptt import PentestTaskTree

class TestApexCore(unittest.TestCase):
    def test_scope_guard_domain(self):
        guard = ScopeGuard(allowed_domains=["target.com"], allowed_cidrs=["192.168.1.0/24"])
        self.assertTrue(guard.is_allowed("api.target.com"))
        self.assertTrue(guard.is_allowed("target.com"))
        self.assertFalse(guard.is_allowed("evil.com"))
        self.assertFalse(guard.is_allowed("target.com.attacker.com"))

    def test_scope_guard_cidr(self):
        guard = ScopeGuard(allowed_domains=[], allowed_cidrs=["192.168.1.0/24"])
        self.assertTrue(guard.is_allowed("192.168.1.45"))
        self.assertFalse(guard.is_allowed("192.168.2.1"))

    def test_scope_enforce_raises(self):
        guard = ScopeGuard(allowed_domains=["target.com"], allowed_cidrs=[])
        with self.assertRaises(ScopeViolationError):
            guard.enforce("unauthorized.com")

    def test_evidence_gate_validation(self):
        gate = EvidenceGate()
        valid = gate.verify_finding(
            vuln_type="XSS",
            target="https://target.com/test",
            poc_command="curl https://target.com/test?q=CANARY",
            raw_request="GET /test?q=CANARY HTTP/1.1",
            raw_response="HTTP/1.1 200 OK\r\n\r\nHello CANARY",
            differential_regex="CANARY"
        )
        self.assertIsNotNone(valid)
        self.assertEqual(valid["status"], "CONFIRMED")

        # False positive test
        invalid = gate.verify_finding(
            vuln_type="SQLi",
            target="https://target.com/test",
            poc_command="curl ...",
            raw_request="GET /test",
            raw_response="HTTP/1.1 200 OK\r\n\r\nNormal response",
            differential_regex="SQL syntax error"
        )
        self.assertIsNone(invalid)

    def test_ptt_hierarchy(self):
        ptt = PentestTaskTree("Test Assessment")
        host = ptt.add_child("SCOPE_ROOT", "host-1", 1, "192.168.1.50", "host", {"status": "LIVE"})
        port = ptt.add_child("host-1", "port-80", 2, "Port 80/HTTP", "service", {"protocol": "http"})
        self.assertIn("port-80", host.children)
        ctx = ptt.get_focused_context("port-80")
        self.assertIn("Port 80/HTTP", ctx)

if __name__ == "__main__":
    unittest.main()
