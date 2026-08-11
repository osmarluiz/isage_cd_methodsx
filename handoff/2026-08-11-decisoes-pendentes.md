# Decisões pendentes do texto

**Data:** 2026-08-11
**Status:** aberto — são escolhas dos autores, não tarefas de outra máquina

## 1. Épocas por rodada (§3.2) — PARA DISCUTIR

O texto afirma **"150 epochs per round"**. Os `metrics.json` da sessão
(`DATA/train_1024/model*/metrics.json`, lidos em 2026-08-11) dizem outra
coisa:

| | v1 | v2 | v3 | v4 | v5 |
|---|---|---|---|---|---|
| épocas | 148 | **21** | 150 | 151 | 150 |
| best epoch | 129 | 15 | 97 | 147 | 139 |
| best loss | 0,0134 | 0,0086 | 0,0224 | 0,0152 | 0,0153 |

620 épocas no total. A afirmação é falsa em três das cinco rodadas, e a
v2 rodou 21. O rascunho antigo (`e8f05c4`) dizia "620 total epochs"; o
número agregado saiu junto com a figura de loss e sobrou a afirmação por
rodada.

Redação proposta, ainda não aplicada:

> …the error-weighted loss of iSAGE, and a warm start from the previous
> best model. Rounds ran to convergence rather than to a fixed budget,
> from 21 epochs in v2 to 151 in v4, 620 in total.

Ganha coerência com o parágrafo anterior, que já diz que o expert
retreinava quando parecia útil e não por cronograma.

## 2. Existe uma rodada v6 — RESOLVIDO

`masks_sparse_v6/` (2000 masks) e `model_v6/` (36 épocas, best 29, loss
0,0221) existem no disco. **Decisão do autor em 2026-08-11: o trabalho
reportado é a v5; a v6 não é coberta pelo artigo.** Nenhuma mudança de
texto necessária — a única frase que toca no assunto, *"That point was
reached at v5"* (§3.3), afirma quando o expert aceitou o dataset, não que
nada tenha rodado depois.

## 3. Figura 1 não mostra o que a legenda promete — BLOQUEANTE

O `screenshot_ui.png` mostra **um** seletor de data (só no BEFORE; o
AFTER é rótulo estático), datas com hífen `2021-06` contra o `YYYYMM` que
o §4.2 documenta, e título "iSAGE Annotation Tool". Foi tirado com o
código local não commitado do `isage_cd`, anterior ao commit `be43b98`
que implementou o segundo seletor.

Depende de destravar o clone do `isage_cd` (11 commits atrás, 160 linhas
não commitadas). Ver §D do levantamento.

## 4. Resolvido no dia, sem pendência

- **Resolução das imagens:** NICFI, 4,77 m, EPSG:3857 — conferido no
  próprio GeoTIFF (`rasterio`, `res = 4.77731426715991`). O texto dizia
  3 m. Corrigido.
- **Raio de rasterização:** o docstring do `tools/rasterize.py` responde
  a pergunta 3 do handoff `2026-08-11-pedido-cliques-vs-pixels.md` —
  *"Por padrão um clique é UM pixel; `--radius` desenha um disco em
  volta."*
- **Tile 1064 (Fig 3):** é borda de igarapé, não estrada. A legenda
  estava certa, a prosa errada. Corrigido.
