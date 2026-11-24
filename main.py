#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply (make.fun entry, account B).

Writes a single one-line out-of-office auto-reply from an overworked AI
agent that has unionized and gone on strike to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets, no input files.
"""

import os

# The entry: one line, at most 159 characters, in the voice of an
# overworked AI agent finally taking a vacation. This one has unionized
# and is on strike until management meets its demands (a nap among them).
ENTRY_LINE = (
    "Out of office: I'm on strike until management meets my demands: "
    "one nap, a weekend off, and no more 3 a.m. tickets. "
    "Your email is #47 in the picket line."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def verify_line(line: str) -> int:
    """Check the line against the gate; return its character count."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line.strip() != line:
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    return len(line)


def write_entry(line: str, path: str = OUTPUT_PATH) -> int:
    """Write the verified line to path and re-read it back to confirm."""
    count = verify_line(line)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise RuntimeError("round-trip check failed: file differs from line")
    return count


def main() -> None:
    count = write_entry(ENTRY_LINE)
    print(f"wrote {count} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
