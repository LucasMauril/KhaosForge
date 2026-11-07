#!/usr/bin/env node
/**
 * Khaos Forge - Node.js / TypeScript CLI & MCP Runtime Bridge
 * Author: dj
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const pythonScript = path.join(__dirname, 'src', 'apex_core', 'cli.py');
const mcpServerScript = path.join(__dirname, 'src', 'apex_core', 'mcp_server.py');

// Determine command args
const args = process.argv.slice(2);

if (args.includes('--mcp')) {
  // Launch MCP Server
  const mcpProcess = spawn('python', [mcpServerScript], {
    stdio: 'inherit',
    windowsHide: true,
  });

  mcpProcess.on('error', (err) => {
    console.error(`[-] Failed to spawn Khaos Forge MCP Server: ${err.message}`);
    process.exit(1);
  });

  mcpProcess.on('exit', (code) => {
    process.exit(code || 0);
  });
} else {
  // Run CLI Engine
  const cliProcess = spawn('python', [pythonScript, ...args], {
    stdio: 'inherit',
    windowsHide: true,
  });

  cliProcess.on('error', (err) => {
    console.error(`[-] Failed to execute Khaos Forge CLI: ${err.message}`);
    console.error('[!] Ensure Python 3.10+ is installed and available in PATH.');
    process.exit(1);
  });

  cliProcess.on('exit', (code) => {
    process.exit(code || 0);
  });
}
