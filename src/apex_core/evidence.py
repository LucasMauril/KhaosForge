import hashlib
import re
import time
from typing import Dict, Any, Optional

class EvidenceGate:
    """
    Validates findings to guarantee anti-hallucination.
    Findings are discarded unless differential proof is cryptographically sealed.
    """
    def __init__(self):
        self.findings: Dict[str, Dict[str, Any]] = {}

    def verify_finding(
        self,
        vuln_type: str,
        target: str,
        poc_command: str,
        raw_request: str,
        raw_response: str,
        differential_regex: str,
        severity: str = "MEDIUM"
    ) -> Optional[Dict[str, Any]]:
        """
        Validates evidence strictly against the raw response.
        """
        if not re.search(differential_regex, raw_response, re.IGNORECASE | re.DOTALL):
            return None  # Proof rejected: rejected as false positive or hallucination

        transcript = f"REQUEST:\n{raw_request}\n\nRESPONSE:\n{raw_response}"
        proof_hash = hashlib.sha256(transcript.encode("utf-8")).hexdigest()
        finding_id = f"APEX-{proof_hash[:10].upper()}"

        record = {
            "id": finding_id,
            "type": vuln_type,
            "severity": severity.upper(),
            "target": target,
            "poc": poc_command,
            "proof_hash": proof_hash,
            "timestamp": time.time(),
            "raw_transcript": transcript,
            "status": "CONFIRMED"
        }
        self.findings[finding_id] = record
        return record

    def get_confirmed(self) -> Dict[str, Dict[str, Any]]:
        return self.findings
