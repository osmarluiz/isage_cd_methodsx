# Design: formato pool de datas + reestrutura do Method Details

Data: 2026-08-07
Status: aguardando revisão do Osmar

## Contexto e decisões de escopo

O Method Details do paper será reorganizado na ordem do fluxo de uso:
dataset → formato de anotação → rotulação → treino → loop iterativo.
Isso puxa **uma** mudança de software no `isage_cd` (público):

1. **Pool de datas por cena, com as duas datas selecionáveis.** Hoje o
   "depois" (frame) é fixo e só a referência ("antes") troca de data.
   Passa a existir um pool de imagens datadas por cena, e o usuário
   escolhe antes E depois pela data — generalização do que foi feito no
   repo da polícia (isage_cd_ICP), onde só uma imagem podia trocar.

2. **NÃO haverá aba de treino embutida.** Decisão explícita: o valor
   está no modelo estar *no loop*, não *na ferramenta*. Quem usa quer
   plugar o próprio modelo. O contrato é a árvore de pastas da sessão
   (annotations/ entra, models/ + predictions/ sai); o iSAGE já fornece
   trainer de referência (SMP + error-weighted loss) e o padrão BYOT.
   No paper isso vira uma design choice declarada, com a Tabela 1
   (produtor/consumidor por subpasta) como a interface.

## A. Formato de sessão novo ("3.0-pool")

- Imagens: `data/dataset/train/<cena>/<data>.png`, com `<data>` uma
  string de dígitos ordenável (`YYYYMM` ou `YYYYMMDD`).
- Somem `images/` vs `images_before/` e `pair_meta/` — as datas vêm dos
  nomes de arquivo.
- Par = qualquer `(antes, depois)` com `antes < depois` (ordem
  lexicográfica = cronológica).
- Anotação: `iteration_N/annotations/<cena>/<antes>_<depois>.json`
  (separador `_`, ex. `202106_202206.json`),
  `format_version: "3.0-pool"`, bloco
  `pair: {scene, date_before, date_after}`, pontos `[x, y, class]`.
- Escrita atômica (temp + rename) e remoção de arquivo/pasta vazios:
  iguais ao atual.
- Predições por par: `iteration_N/predictions/<cena>/<antes>_<depois>.png`
  (hoje é por frame; com pool, por frame fica ambíguo).

## B. UI (`cd_widget.py`)

- Um seletor de data sobre **cada** canvas (antes à esquerda, depois à
  direita): dropdown + setas + atalhos, mesmo padrão do seletor atual.
- Regra `antes < depois` imposta na UI: no dropdown do antes só ficam
  habilitadas datas anteriores ao depois corrente, e vice-versa.
- Trocar qualquer uma das datas troca o par ativo (conjunto de pontos
  nos dois canvases). Bullets nas datas já anotadas e contadores
  (total / cena / este par) mantidos.

## C. Ferramentas

- `tools/build_session.py`: entrada vira pasta de cenas, cada uma com
  imagens datadas (`<cena>/<data>.png`).
- Novo `tools/migrate_session.py`: converte sessão 2.1-pair → 3.0-pool.
  - `depois.png`/`images/<cena>.png` → `<cena>/<date_after>.png`
    (date_after lido do `pair_meta`);
  - `antes_YYYYMM.png` → `YYYYMM.png`;
  - JSONs `annotations/<cena>/<antes>.json` →
    `<cena>/<antes>_<date_after>.json`;
  - `predictions/<cena>.png` → `predictions/<cena>/<antes>_<depois>.png`
    do par correspondente. (Resolvido via handoff: a sessão Amazon tem
    sempre 1 referência por frame, então o mapeamento é direto.);
  - atualiza `session_config.json` / `dataset_metadata.json`.
  - O anotador entende SÓ o formato novo (sem caminho de código legado).
- `--exportar` / `--importar`: inalterados (só carregam nomes novos).

## D. Paper — `sections/04_method_details.tex` reestruturado

1. Overview — termos: **cena**, **pool de datas**, **par**; Fig 1.
2. Sessão e construção do dataset (formato pool, `build_session.py`).
3. Formato de anotação pair-anchored: escrita atômica, versionamento
   por iteração.
4. Interface bi-temporal e ferramentas de rotulação (duas datas
   selecionáveis).
5. Treino no loop por contrato — trainer desacoplado; Tabela 1 como
   interface; trainer de referência no repo do iSAGE.
6. Loop iterativo guiado por erros + intercâmbio entre anotadores
   (exportar/importar).

## E. Consequências na validação (seção 05)

- A Method Validation ancora na **sessão real** (2000 tiles, 5
  iterações, 143.634 pontos, dois blocos de datas: A =
  2021-06→2022-06 em 0000-0999, B = 2021-08→2022-07 em 1000-1999).
  Referência técnica completa:
  `handoff/2026-08-07-sessao-real-referencia.md`.
- A conversão da sessão real (formato v1.0 → 3.0-pool) é feita por
  script sessão-específico na máquina de anotação, seguindo o §3 da
  referência; o `migrate_session.py` público cobre só 2.1-pair →
  3.0-pool (divisão registrada em
  `handoff/2026-08-07-respostas-do-paper.md`).
- Trainer/predict de referência a citar no Method Details:
  `github.com/osmarluiz/amazon-deforestation-cd` (Unet +
  EfficientNet-B7, loss error-weighted `DWCBCELossSimple`, sliding
  window 1024/stride 512).
- O screenshot da UI (Fig 1A) será regerado na máquina de anotação
  com os dois seletores de data visíveis, sobre a sessão real migrada.

## Fora de escopo

- Aba de treino na GUI (decisão registrada acima).
- Mudanças no protocolo de treino/loss (herdado do iSAGE, sem alteração).
- Suporte a formato legado no anotador (migração única resolve).
