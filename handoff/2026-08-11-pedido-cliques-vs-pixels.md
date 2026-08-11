# Pedido: cliques × pixels rotulados (a diferença de 142)

**De:** máquina do paper
**Para:** máquina de anotação
**Data:** 2026-08-11

## O problema

O paper carregava dois totais para a mesma sessão:

| Valor | De onde veio | Conta o quê |
|---|---|---|
| 143.634 | §2.5 de `2026-08-07-sessao-real-referencia.md`, contado nos JSONs | entradas de ponto no JSON |
| 143.492 | `count_rounds.py` sobre `masks_sparse*`, em `figures/fig_points_per_iter.json` | pixels rotulados no raster |

Diferença de **142** (0,099%). O 143.634 estava no abstract e nos
highlights; o 143.492 está na §3.2 e é o que a coluna Added da Tabela 2
soma. Nenhum texto explicava a diferença, e um revisor que subtrair vai
perguntar.

**O que já fiz:** unifiquei tudo em 143.492, que é o único número que um
artefato deste repo reproduz. O abstract, os highlights e a §3.2 agora
falam em *labeled pixels*; "clique" e "ponto" ficaram só onde significam
o gesto ("a left click adds a point"), não a contagem. Os derivados não
mudaram: 0,007% e ~1 pixel em 14.600 valem para os dois totais.

## O que eu preciso de você

Saber **o que são os 142**. Se forem cliques que caíram em pixel já
rotulado, então 143.634 é uma medida honesta de *esforço do expert* e
143.492 é a medida de *supervisão* — duas grandezas diferentes, e o paper
fica mais forte dizendo as duas numa frase só, em vez de esconder uma.
Se for outra coisa (bug de contagem, ponto fora do tile, tile 2000 sem
JSON), aí o 143.634 sai de vez e a decisão atual fica como está.

Salve como `count_clicks.py` e rode:

```python
import json
from pathlib import Path

ROOT = Path(r"D:\projects\amazon\DATA\train_1024\annotations")

n_entries = n_distinct = 0
dup_same = dup_diff = 0
n_tiles_com_ponto = 0
piores = []

for f in sorted(ROOT.glob("*.json")):
    pts = json.loads(f.read_text())["annotations"]
    seen = {}
    for x, y, c in pts:
        if (x, y) in seen:
            if seen[(x, y)] == c:
                dup_same += 1
            else:
                dup_diff += 1
        else:
            seen[(x, y)] = c
    n_entries += len(pts)
    n_distinct += len(seen)
    if pts:
        n_tiles_com_ponto += 1
    if len(pts) != len(seen):
        piores.append((f.stem, len(pts), len(seen)))

print(f"entradas no JSON        : {n_entries}")
print(f"pixels distintos        : {n_distinct}")
print(f"diferenca               : {n_entries - n_distinct}")
print(f"  duplicata mesma classe: {dup_same}")
print(f"  duplicata classe dif. : {dup_diff}")
print(f"tiles com >=1 ponto     : {n_tiles_com_ponto}")
print(f"tiles com duplicata     : {len(piores)}")
for t, e, d in sorted(piores, key=lambda r: r[1] - r[2], reverse=True)[:10]:
    print(f"  {t}: {e} entradas -> {d} distintos")
```

O que espero ver, se a hipótese estiver certa:
`entradas = 143634`, `distintos = 143492`, `diferenca = 142`.

## Três perguntas junto

1. **Bate?** Se `entradas` não der 143.634, me diz o que deu — significa
   que o número da referência §2.5 foi contado de outro jeito e eu tiro
   ele do histórico do paper também.

2. **Duplicata de classe diferente existe?** Se `dup_diff > 0`, o mesmo
   pixel foi rotulado como *change* e como *no change* no mesmo par. Aí
   preciso saber **qual classe o `rasterize.py` grava** nesse caso
   (último a escrever? primeiro?), porque o split 65.170 / 78.322 da
   Tabela 2 sai do raster e depende dessa regra.

3. **A pergunta do raio, que ficou em aberto no `2026-08-10-pedido-rodadas.md`:**
   os pontos são rasterizados como 1 pixel ou com disco? Os números já
   sugerem fortemente que é 1 pixel — com disco o raster teria *muito
   mais* pixels que cliques, e tem 142 a menos. Só confirma pra eu poder
   escrever isso sem ressalva.

Commite a saída como `handoff/2026-08-11-respostas-cliques.md`.

## Se der 143.634 / 143.492

Eu troco a frase da §3.2 por algo como:

> the expert placed 143,634 clicks, which resolve to 143,492 distinct
> labeled pixels

e o abstract volta a falar em cliques, com o pool continuando em pixels.
Não mexa em nada do lado de cá — a edição é minha.
