#!/usr/bin/env python3
"""Compare .env against .env.example and report drift."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key in values:
            print(f"duplicate key in {path}: {key}", file=sys.stderr)
        values[key] = value.strip()
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare .env against .env.example and report drift.")
    parser.add_argument("--env", type=Path, default=Path(".env"))
    parser.add_argument("--example", type=Path, default=Path(".env.example"))
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    env = parse(args.env)
    example = parse(args.example)
    missing = sorted(set(example) - set(env))
    extra = sorted(set(env) - set(example))
    for key in missing:
        print(f"missing in .env: {key}")
    for key in extra:
        print(f"not in .env.example: {key}")
    if not missing and not extra and not args.quiet:
        print(f"ok: {len(env)} keys")
    return 1 if missing or extra else 0


if __name__ == "__main__":
    sys.exit(main())
