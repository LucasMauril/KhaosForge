import ipaddress
import re
from typing import List, Union

class ScopeViolationError(PermissionError):
    """Raised when an operation attempts to target an unauthorized host, IP, or network."""
    pass

class ScopeGuard:
    """
    Enforces strict rules of engagement boundaries.
    Validates targets before any network probe, scanner, or tool is invoked.
    """
    def __init__(self, allowed_domains: List[str] = None, allowed_cidrs: List[str] = None):
        self.allowed_domains = [d.lower().strip() for d in (allowed_domains or [])]
        self.allowed_networks = []
        for cidr in (allowed_cidrs or []):
            try:
                self.allowed_networks.append(ipaddress.ip_network(cidr.strip(), strict=False))
            except ValueError as err:
                raise ValueError(f"Invalid CIDR block '{cidr}': {err}")

    def is_allowed(self, target: str) -> bool:
        target_clean = target.lower().strip()
        # Strip port or scheme if provided
        target_clean = re.sub(r"^https?://", "", target_clean)
        target_clean = target_clean.split("/")[0].split(":")[0]

        # 1. IP Check
        try:
            ip_obj = ipaddress.ip_address(target_clean)
            return any(ip_obj in net for net in self.allowed_networks)
        except ValueError:
            pass

        # 2. Domain Check
        for domain in self.allowed_domains:
            if target_clean == domain or target_clean.endswith("." + domain):
                return True

        return False

    def enforce(self, target: str):
        if not self.is_allowed(target):
            raise ScopeViolationError(
                f"[SCOPE VIOLATION] Target '{target}' is not in authorized scope. Aborting execution."
            )
