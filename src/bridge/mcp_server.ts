/**
 * Khaos Forge - TypeScript MCP Protocol Bridge
 * Author: Lucas Mauril
 */

export interface ScopeRule {
  allowedDomains: string[];
  allowedCidrs: string[];
}

export interface FindingProof {
  vulnType: string;
  target: string;
  pocCommand: string;
  rawRequest: string;
  rawResponse: string;
  differentialRegex: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
}

export interface TaskNode {
  id: string;
  layer: number;
  title: string;
  type: string;
  status: 'PENDING' | 'IN_PROGRESS' | 'COMPLETED' | 'VULNERABLE';
  metadata: Record<string, unknown>;
  children: string[];
}

export class KhaosBridge {
  private scope: ScopeRule;

  constructor(scope?: ScopeRule) {
    this.scope = scope || { allowedDomains: [], allowedCidrs: [] };
  }

  public isDomainAllowed(target: string): boolean {
    const cleanTarget = target.toLowerCase().trim().replace(/^https?:\/\//, '').split('/')[0].split(':')[0];
    return this.scope.allowedDomains.some((domain) => {
      const cleanDomain = domain.toLowerCase().trim();
      return cleanTarget === cleanDomain || cleanTarget.endsWith(`.${cleanDomain}`);
    });
  }

  public getToolsSchema(): Array<Record<string, unknown>> {
    return [
      {
        name: 'khaos_scope_lock',
        description: 'Enforces CIDR and FQDN rules of engagement in TypeScript runtime',
        parameters: {
          type: 'object',
          properties: {
            domains: { type: 'array', items: { type: 'string' } },
            cidrs: { type: 'array', items: { type: 'string' } },
          },
          required: ['domains', 'cidrs'],
        },
      },
      {
        name: 'khaos_verify_evidence',
        description: 'Cryptographically verifies raw differential responses',
        parameters: {
          type: 'object',
          properties: {
            vuln_type: { type: 'string' },
            target: { type: 'string' },
            poc_command: { type: 'string' },
            raw_response: { type: 'string' },
            differential_regex: { type: 'string' },
          },
          required: ['vuln_type', 'target', 'poc_command', 'raw_response', 'differential_regex'],
        },
      },
    ];
  }
}
