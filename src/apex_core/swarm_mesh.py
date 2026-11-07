import json
import time
from typing import Dict, Any, List, Optional

class SwarmMeshNode:
    """
    Decentralized graph synchronization client inspired by GunDB.
    Enables offline-first, peer-to-peer state propagation across red team agent swarms.
    """
    def __init__(self, node_identifier: str, relay_endpoints: Optional[List[str]] = None):
        self.node_identifier = node_identifier
        self.relay_endpoints = relay_endpoints or []
        self.state_cache: Dict[str, Any] = {}

    def publish_update(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Records a state change with vector-clock metadata for P2P convergence."""
        timestamp = time.time()
        delta = {
            "path": path,
            "origin": self.node_identifier,
            "timestamp": timestamp,
            "data": payload
        }
        self.state_cache[path] = delta
        return delta

    def ingest_remote_delta(self, delta: Dict[str, Any]) -> bool:
        """Applies remote delta using Last-Write-Wins (LWW) conflict resolution."""
        path = delta.get("path")
        if not path:
            return False

        existing = self.state_cache.get(path)
        if not existing or delta.get("timestamp", 0) > existing.get("timestamp", 0):
            self.state_cache[path] = delta
            return True
        return False

    def export_graph_json(self) -> str:
        return json.dumps(self.state_cache, indent=2)
