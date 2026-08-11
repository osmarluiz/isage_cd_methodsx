#!/usr/bin/env python3
"""Recorta os 4 paineis de uma linha da figura qualitativa para o
graphical abstract (antes, depois, cliques, predicao).

    python tools/make_ga_crops.py --row 2

Saida: figures/ga_{before,after,clicks,pred}.png, consumidos por
figures/graphical_abstract.tex. Manter este script versionado ao lado
da figura e a proveniencia dela.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import imageio.v2 as imageio

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "figures" / "fig_qualitative.png"
NAMES = ["before", "after", "clicks", "pred"]


def runs(mask, min_len=40):
    out, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        elif not v and start is not None:
            if i - start >= min_len:
                out.append((start, i))
            start = None
    if start is not None and len(mask) - start >= min_len:
        out.append((start, len(mask)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--row", type=int, default=2, help="linha 1..4")
    args = ap.parse_args()

    img = imageio.imread(SRC)[:, :, :3]
    h, w, _ = img.shape
    nonwhite = img.sum(axis=2) < 720
    cols = runs(nonwhite.sum(axis=0) > h * 0.05)
    rows = runs(nonwhite.sum(axis=1) > w * 0.05)
    if len(cols) < 4 or len(rows) < 4:
        raise SystemExit(f"grade nao detectada (cols={len(cols)}, rows={len(rows)})")
    cols, rows = cols[-4:], rows[-4:]

    r0, r1 = rows[args.row - 1]
    for name, (c0, c1) in zip(NAMES, cols):
        s = min(r1 - r0, c1 - c0)
        panel = img[r0:r0 + s, c0:c0 + s]
        out = ROOT / "figures" / f"ga_{name}.png"
        imageio.imwrite(out, panel)
        print(f"  {out.name}: {panel.shape[1]}x{panel.shape[0]}")
    print(f"OK: linha {args.row} de {SRC.name}")


if __name__ == "__main__":
    main()
