# Pedido: pontos por rodada + progressão visual v1..v5

**De:** máquina do paper
**Para:** máquina de anotação
**Data:** 2026-08-10

## O que mudou no paper

**A Fig 2 (curva de loss por época acumulada) saiu.** Era evidência
fraca: o próprio texto tinha que se defender dela ("we do not compare
against a dense-supervision baseline"), e um revisor de MethodsX quer
ver o *loop funcionando*, não a loss caindo. No lugar entram duas
coisas que preciso de você:

1. **Uma tabela de rodadas** — quantos pontos o expert colocou em cada
   rodada e quanto do pool já estava coberto ao fim dela.
2. **Uma figura de progressão** — a mesma região vista pelo modelo de
   cada rodada, de v1 a v5, mostrando a melhora.

## 1. Pontos por rodada

**Cuidado importante:** os JSONs em `annotations/` são o estado
**acumulado** das 5 rodadas, então não dá para tirar a contagem por
rodada deles. A fonte certa são as máscaras rasterizadas de cada
rodada, que existem separadas:

`masks_sparse/` (v1), `masks_sparse_v2/`, `_v3/`, `_v4/`, `_v5/`

Script (salve como `count_rounds.py` e rode em
`D:\projects\amazon\DATA\train_1024\`):

```python
import json
from pathlib import Path

import numpy as np
import imageio.v2 as imageio

ROOT = Path(r"D:\projects\amazon\DATA\train_1024")
IGNORE = 255                      # confirmar: valor de ignore das masks
ROUNDS = [("v1", "masks_sparse"), ("v2", "masks_sparse_v2"),
          ("v3", "masks_sparse_v3"), ("v4", "masks_sparse_v4"),
          ("v5", "masks_sparse_v5")]

rows = []
for name, folder in ROUNDS:
    d = ROOT / folder
    if not d.exists():
        print(f"AUSENTE: {d}")
        continue
    n_tiles = n_pts = n_change = n_nochange = 0
    for f in sorted(d.glob("*.png")):
        m = imageio.imread(f)
        lab = m[m != IGNORE]
        if lab.size:
            n_tiles += 1
            n_pts += int(lab.size)
            n_change += int((lab == 1).sum())
            n_nochange += int((lab == 0).sum())
    rows.append({"round": name, "folder": folder, "tiles": n_tiles,
                 "points": n_pts, "change": n_change,
                 "no_change": n_nochange})
    print(f"{name}: {n_tiles} tiles, {n_pts} pontos "
          f"({n_change} change / {n_nochange} no change)")

print("\nJSON:\n" + json.dumps(rows, indent=2))
```

Commite a saída como
`handoff/2026-08-10-respostas-rodadas.md`.

**Duas perguntas junto:**

- O valor de ignore das masks é 255 mesmo? (o script assume isso; se
  for outro, corrige a constante)
- Um pixel na mask equivale a um clique, ou os pontos foram
  rasterizados com um disco/raio? Se tiver raio, me diz qual, porque
  aí a contagem de pixels não é contagem de pontos e o script precisa
  contar componentes conexos.

## 2. Progressão visual da mesma região

Quero uma figura com uma faixa por rodada: a mesma janela, a predição
de v1, v2, v3, v4 e v5 sobre a imagem T2, mais T1 e T2 como
referência. A cena tem que ser do **Bloco A** (tiles 0000-0999),
porque só ele tem predição por-tile em todas as rodadas
(`predictions/`, `predictions_v2..v4/`, e v5 vindo do crop do
full-image).

Preciso dos recortes crus, não da figura montada — eu monto aqui com
o mesmo estilo da Fig 3. Para **três tiles candidatos** (escolhe com
`change_pct` entre 30% e 70% no `metadata.json`, que é onde a melhora
costuma aparecer melhor), exporta em
`handoff/rounds/<tile>/`:

- `t1.png` e `t2.png` (o mesmo stretch p2/p98 do
  `convert_amazon_session.py`)
- `pred_v1.png` ... `pred_v4.png` (de `predictions{,_v2,_v3,_v4}/<tile>.png`)
- `pred_v5.png` (crop de `prediction_full_1024_v5.tif` em `(col, row)`
  do `metadata.json`)

PNG 1024x1024, uint8 0/1 nas predições. São ~7 arquivos por tile,
alguns MB no total, cabe no repo tranquilo.

Se algum tile não tiver predição em alguma rodada, me avisa qual —
prefiro saber que a série tem buraco a descobrir na hora de montar.

## Por que três candidatos

Escolho aqui o que mostra a progressão mais legível e descarto os
outros dois, sem cherry-picking disfarçado: no caption vai dizer que o
tile foi escolhido entre candidatos por legibilidade, e os três ficam
no repo para quem quiser conferir.
