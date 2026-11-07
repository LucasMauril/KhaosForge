---
name: bin-triage
description: Audit compiled binaries (ELF/PE), firmware blobs, checksec mitigations, and disassembly.
arguments:
  - name: binary
    description: Path to binary or firmware file
    required: true
---

# /bin-triage Command

Perform low-level vulnerability triage on `$binary`.

## Execution Steps
1. Run `checksec --file=$binary` to audit RELRO, Canaries, NX, and PIE.
2. Extract strings and symbols with `rabin2 -z -s $binary`.
3. Disassemble entry points and dangerous functions (`strcpy`, `system`, `printf`) using `r2`.
4. If firmware, unpack file systems using `binwalk -eM $binary`.
