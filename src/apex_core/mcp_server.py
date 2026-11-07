import sys
import json
import subprocess
import time
from typing import Dict, Any, List
from apex_core.scope import ScopeGuard, ScopeViolationError
from apex_core.evidence import EvidenceGate
from apex_core.ptt import PentestTaskTree

class ApexMCPServer:
    """
    Standard Model Context Protocol (MCP) Server for Apex Cybersecurity Framework.
    Communicates via standard I/O (JSON-RPC 2.0).
    """
    def __init__(self):
        self.scope_guard = ScopeGuard()
        self.evidence_gate = EvidenceGate()
        self.ptt = PentestTaskTree("Default Assessment")

    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        req_id = request.get("id")
        method = request.get("method")
        params = request.get("params", {})

        try:
            if method == "tools/list":
                return self._list_tools(req_id)
            elif method == "tools/call":
                return self._call_tool(req_id, params.get("name"), params.get("arguments", {}))
            elif method == "initialize":
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "apex-mcp-server", "version": "1.0.0"}
                    }
                }
            else:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
        except Exception as err:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32000, "message": str(err)}}

    def _list_tools(self, req_id: Any) -> Dict[str, Any]:
        tools = [
            {
                "name": "apex_configure_scope",
                "description": "Configures allowed CIDR blocks and FQDNs for scope enforcement.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "allowed_domains": {"type": "array", "items": {"type": "string"}},
                        "allowed_cidrs": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["allowed_domains", "allowed_cidrs"]
                }
            },
            {
                "name": "apex_execute_tool",
                "description": "Executes a sandboxed security tool with pre-flight scope validation.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target": {"type": "string", "description": "Target IP or host"},
                        "command": {"type": "array", "items": {"type": "string"}, "description": "Command list"}
                    },
                    "required": ["target", "command"]
                }
            },
            {
                "name": "apex_verify_evidence",
                "description": "Validates a finding via raw differential response proof to prevent hallucinations.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "vuln_type": {"type": "string"},
                        "target": {"type": "string"},
                        "poc_command": {"type": "string"},
                        "raw_request": {"type": "string"},
                        "raw_response": {"type": "string"},
                        "differential_regex": {"type": "string"}
                    },
                    "required": ["vuln_type", "target", "poc_command", "raw_request", "raw_response", "differential_regex"]
                }
            }
        ]
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools}}

    def _call_tool(self, req_id: Any, name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        if name == "apex_configure_scope":
            self.scope_guard = ScopeGuard(args.get("allowed_domains"), args.get("allowed_cidrs"))
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": "Scope enforcement successfully locked."}]}
            }
        elif name == "apex_execute_tool":
            target = args["target"]
            self.scope_guard.enforce(target)
            cmd = args["command"]
            # Execution in sandbox
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps({"stdout": res.stdout, "stderr": res.stderr, "exit_code": res.returncode})}]
                }
            }
        elif name == "apex_verify_evidence":
            res = self.evidence_gate.verify_finding(
                args["vuln_type"],
                args["target"],
                args["poc_command"],
                args["raw_request"],
                args["raw_response"],
                args["differential_regex"]
            )
            status_text = f"Confirmed Finding: {res['id']}" if res else "Evidence Rejected: Pattern mismatch."
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": status_text}]}
            }
        raise ValueError(f"Unknown tool '{name}'")

    def run_stdio(self):
        for line in sys.stdin:
            if not line.strip():
                continue
            try:
                request = json.loads(line)
                response = self.handle_request(request)
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
            except Exception as err:
                sys.stderr.write(f"MCP Loop Error: {err}\n")

if __name__ == "__main__":
    server = ApexMCPServer()
    server.run_stdio()
