"""Copy entry.txt byte-identical into $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib-only. No temp files, no network, no extra output: the output file
is written directly and chmodded 0644 so the grader can read it.
"""

import os
import sys
from pathlib import Path

ENTRY = "entry.txt"


def main():
    try:
        here = Path(__file__).resolve().parent
        src = here / ENTRY
        out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    except KeyError:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    out_dir.mkdir(parents=True, exist_ok=True)
    data = src.read_bytes()
    if not data.strip():
        print("entry.txt is empty or whitespace-only", file=sys.stderr)
        raise SystemExit(1)
    out = out_dir / ENTRY
    out.write_bytes(data)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
