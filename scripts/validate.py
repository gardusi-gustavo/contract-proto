#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    protos = sorted((root / "proto").rglob("*.proto"))
    if not protos:
        print("no proto files", file=sys.stderr); return 1
    for p in protos:
        text = p.read_text(encoding="utf-8")
        for needle in ('syntax = "proto3";', "package "):
            if needle not in text:
                print(f"{p}: missing {needle}", file=sys.stderr); return 1
        if not re.search(r"\b(message|service)\b", text):
            print(f"{p}: no message or service", file=sys.stderr); return 1
    if not (root / "buf.yaml").is_file():
        print("missing buf.yaml", file=sys.stderr); return 1
    print(f"proto validation ok ({len(protos)} files)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
