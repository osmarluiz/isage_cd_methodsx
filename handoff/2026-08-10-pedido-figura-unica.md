# Pedido: fundir as duas figuras de tiles em uma só

**De:** máquina do paper
**Para:** máquina de anotação
**Data:** 2026-08-10

## O problema

O paper tem hoje **duas figuras de quatro linhas de tiles** que
compartilham três colunas:

- `fig_iteration_progression`: T1, T2, v1, v2, v3, v4, v5 (Bloco A)
- `fig_qualitative`: T1, T2, anotações, v5 (Bloco B)

Ou seja, T1, T2 e a predição v5 aparecem duas vezes, em duas páginas
diferentes, com convenções de cor diferentes (vermelho opaco numa,
translúcido na outra). É redundância de meia página.

A figura de pontos por rodada virou **tabela** aqui do meu lado (era
o pedido original, e uma tabela de 5 linhas por 6 colunas é mais
precisa e ocupa um quarto do espaço). Os arquivos
`fig_points_per_iter.*` não são mais usados pelo texto.

## O que eu quero no lugar

**Uma figura só**, com seis colunas:

| T1 | T2 | cliques | v1 | v3 | v5 |

- **cliques**: os pontos que o expert colocou naquele par, sobre o T2
  (círculos vermelhos = change, verdes = no change, como na
  qualitativa atual). É a coluna que falta na progressão e a razão de
  a qualitativa existir.
- **v1, v3, v5**: só três rodadas. O próprio texto do paper diz que v2
  e v4 quase não mudam nada, então as duas colunas custam largura e
  não pagam. Quem quiser o passo a passo tem a tabela.
- Quatro linhas, os mesmos tiles do Bloco~A que você já escolheu (são
  onde as rodadas discordam mais, e a legenda declara isso).

**Convenção de cor:** vermelho **translúcido** (alpha ~0.45) nas
colunas de predição, para dar pra conferir se o vermelho segue o
desmatamento. Mesma convenção da qualitativa atual.

**Ajustes que já tinha pedido e valem para a figura nova:**

- o rótulo da última linha está cortado na margem esquerda
  ("ourious activation cleanup", falta o "Sp")
- esse rótulo nomeia a interpretação; deveria descrever a cena, algo
  como "Water and forest edge (change=4.8%)"

Nome do arquivo: `figures/fig_tiles.pdf` (e `.png`), que eu ligo no
texto quando chegar. Pode apagar `fig_iteration_progression.*`,
`fig_qualitative.*` e `fig_points_per_iter.*` no mesmo commit, junto
com os `.png` duplicados que não são usados pelo LaTeX.

## E o script

Commita o script que gera a figura em `tools/` do repo do paper, ao
lado dela. Hoje ele vive em `tools_scratch/`, que está no
`.gitignore`, então a figura não tem proveniência versionada.

## Lembrete do pedido anterior

O screenshot novo da Fig 1a (com os **dois** seletores de data)
continua sendo o bloqueio mais sério do paper. Detalhes em
`2026-08-10-pedido-screenshot.md`.
