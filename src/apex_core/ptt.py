import json
import time
from typing import Dict, Any, List, Optional

class TaskNode:
    def __init__(self, node_id: str, layer: int, title: str, node_type: str, metadata: Dict[str, Any]):
        self.node_id = node_id
        self.layer = layer            # 0=Scope, 1=Host, 2=Port/Service, 3=Endpoint, 4=Hypothesis
        self.title = title
        self.node_type = node_type
        self.metadata = metadata
        self.status = "PENDING"       # "PENDING", "IN_PROGRESS", "COMPLETED", "VULNERABLE"
        self.children: List[str] = []
        self.created_at = time.time()
        self.updated_at = self.created_at

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.node_id,
            "layer": self.layer,
            "title": self.title,
            "type": self.node_type,
            "status": self.status,
            "metadata": self.metadata,
            "children": self.children,
            "updated_at": self.updated_at
        }

class PentestTaskTree:
    """
    Pentesting Task Tree (PTT) state machine.
    Prunes and organizes context so LLMs never suffer context drift or token saturation.
    """
    def __init__(self, assessment_name: str):
        self.assessment_name = assessment_name
        self.nodes: Dict[str, TaskNode] = {}
        # Root node
        self.root_id = "SCOPE_ROOT"
        self.nodes[self.root_id] = TaskNode(
            self.root_id, 0, assessment_name, "scope_root", {"initialized_at": time.time()}
        )

    def add_child(
        self,
        parent_id: str,
        node_id: str,
        layer: int,
        title: str,
        node_type: str,
        metadata: Dict[str, Any]
    ) -> TaskNode:
        if parent_id not in self.nodes:
            raise KeyError(f"Parent node '{parent_id}' does not exist.")

        if node_id not in self.nodes:
            node = TaskNode(node_id, layer, title, node_type, metadata)
            self.nodes[node_id] = node
        else:
            node = self.nodes[node_id]
            node.metadata.update(metadata)
            node.updated_at = time.time()

        if node_id not in self.nodes[parent_id].children:
            self.nodes[parent_id].children.append(node_id)

        return node

    def set_status(self, node_id: str, status: str):
        if node_id in self.nodes:
            self.nodes[node_id].status = status
            self.nodes[node_id].updated_at = time.time()

    def get_focused_context(self, active_node_id: str) -> str:
        """Returns condensed context for the active node and immediate ancestors/children."""
        active = self.nodes.get(active_node_id)
        if not active:
            return json.dumps({"error": f"Node '{active_node_id}' not found"})

        context = {
            "active_node": active.to_dict(),
            "child_tasks": [self.nodes[cid].to_dict() for cid in active.children if cid in self.nodes],
            "total_nodes": len(self.nodes)
        }
        return json.dumps(context, indent=2)
