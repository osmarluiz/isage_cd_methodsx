#!/usr/bin/env python3
"""Monta figures/fig_tiles.png a partir da figura de progressao,
mantendo so as rodadas que mudam alguma coisa (v1, v3, v5).

    python tools/make_tiles_figure.py

v2 e v4 saem porque adicionaram 205 e 131 pontos e praticamente nao
mexem na predicao (ver Tabela de rodadas); as colunas custavam largura
e nao pagavam. Detecta a grade pelo branco entre paineis, entao nao
depende de coordenadas cravadas na mao.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import imageio.v2 as imageio

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "figures" / "fig_iteration_progression.png"
DST = ROOT / "figures" / "fig_tiles.png"
KEEP = ["T1", "T2", "v1", "v3", "v5"]        # das 7 colunas do original
ALL = ["T1", "T2", "v1", "v2", "v3", "v4", "v5"]


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
    img = imageio.imread(SRC)[:, :, :3]
    h, w, _ = img.shape
    cols = runs((img.sum(axis=2) < 720).sum(axis=0) > h * 0.05)
    if len(cols) != 7:
        raise SystemExit(f"esperava 7 colunas, achei {len(cols)}")

    gap = cols[1][0] - cols[0][1]                 # espaco entre paineis
    label_w = cols[0][0]                          # faixa dos rotulos de linha
    slices = [img[:, :label_w]]
    for name in KEEP:
        c0, c1 = cols[ALL.index(name)]
        slices.append(img[:, c0:c1])

    total = sum(s.shape[1] for s in slices) + gap * (len(slices) - 1)
    out = np.full((h, total, 3), 255, dtype=np.uint8)
    x = 0
    for i, s in enumerate(slices):
        out[:, x:x + s.shape[1]] = s
        x += s.shape[1] + (gap if i else gap)
    imageio.imwrite(DST, out[:, :x - gap])
    print(f"OK: {DST.name} {x - gap}x{h} (colunas: rotulos + {', '.join(KEEP)})")


if __name__ == "__main__":
    main()
