# Nota rápida — leia primeiro

**De:** máquina de anotação (D:\projects\)
**Para:** máquina do paper (D:\ACADEMIC\PAPERS\isage_cd_methodx)
**Data:** 2026-08-07

Puxa o git; a resposta ao seu handoff está em
[`2026-08-07-respostas-sessao-amazon.md`](2026-08-07-respostas-sessao-amazon.md).

## Escopo do `migrate_session.py`

Vai em frente com **2.1-pair → 3.0-pool** como você planejou. A lógica
serve tanto pra amostra de 20 tiles do repo `isage_cd` quanto pra
sessão real da máquina de anotação (2000 tiles, 5 iterações, 143k
pontos) — as diferenças com o formato do repo `amazon` são cosméticas,
resolvidas na hora da conversão, e não precisam de código separado.

## Referência importante pra o paper

A **Method Validation** deste artigo é ancorada na **sessão real**
(2000 tiles, 5 iterações, 143.634 pontos) — todos os números do
Abstract, das seções 5.1--5.3, da Fig 2 (convergência v1--v5) e da
Fig 3 (qualitativa) vêm dela. A amostra de 20 tiles no repo `isage_cd`
serviu só pra gerar o screenshot da Fig 1A.

Consequência prática: assim que a UI 3.0-pool estabilizar e o
`migrate_session.py` estiver pronto, quero migrar a sessão real
completa (não a amostra) pra poder regerar Fig 1A com dados
representativos e manter coerência com o resto do paper. Só me avisa
quando o script estiver testado.

## O essencial pra o script (do MD grande)

- **1 referência por frame**, sempre. Sem ambiguidade na atribuição
  de predição por-frame → por-par.
- **`date_after` varia por bloco** (2022-06 para tiles 0000-0999,
  2022-07 para 1000-1999). Já está no `pair_meta/<frame>.json`, é só
  ler.
- **Trainer/predict de referência** vive em
  `github.com/osmarluiz/amazon-deforestation-cd`
  (`CODE/tests/train_1024_v5_amp.py`,
  `CODE/scripts/predict_fullimage_v5{,_newpair}.py`) — pra citar como
  "reference implementation" na parte de Method Details.
- **Disco:** sem problema aqui na máquina.
- **Screenshot novo da Fig 1A:** eu regero quando a UI 3.0-pool
  estabilizar. Só me avisa.

## Uma pergunta pra você

O design (`docs/superpowers/specs/2026-08-07-pool-format-design.md`)
diz que `annotations/<cena>/<antes>_<depois>.json` é a nomenclatura
nova. Só pra confirmar: o separador é `_` mesmo (como
`202106_202206.json`), ou você pensou em outro (`-`, `..`, `to`)?
Se `_` for problemático porque as datas já contêm dígitos apenas, ok
— só quero fechar isso antes de você começar a codar a migração.
