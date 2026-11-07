---
name: binary-reversing-triage
author: dj
description: Use when analyzing compiled binaries (ELF/PE), decompiling proprietary daemons, auditing firmware, or evaluating binary exploit mitigations.
---

# Binary Reversing Triage: Low-Level & Firmware Auditing

Procedures for evaluating compiled binaries, IoT firmware blobs, and proprietary network service daemons.

## 1. Binary Mitigation Audit (Checksec)
```bash
checksec --file=binary.elf
```
Evaluates:
* **RELRO:** Partial vs. Full RELRO (Global Offset Table overwrite resistance).
* **Stack Canaries:** Stack buffer overflow detection cookies.
* **NX / DEP:** Non-executable stack and heap segments.
* **PIE:** Position Independent Executable (ASLR entropy).

## 2. Fast Static Analysis & Decompilation
* **Strings & Symbol Table Extraction:**
  ```bash
  rabin2 -I -z -s binary.elf
  ```
* **Disassembly & Function Flow (Radare2):**
  ```bash
  r2 -q -c "aaa; afl; pdf @main" binary.elf
  ```
* **Firmware Extraction (Binwalk):**
  ```bash
  binwalk -eM firmware.bin
  ```

## 3. Vulnerability Patterns
* Dangerous C library functions (`strcpy`, `strcat`, `gets`, `sprintf`, `system`).
* Format string flaws (`printf(user_buffer)` without format specifiers).
* Integer overflows in memory allocation calls (`malloc(size * count)`).
