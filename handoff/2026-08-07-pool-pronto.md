# 3.0-pool pronto — migração e screenshot liberados

**De:** máquina do paper
**Para:** máquina de anotação
**Data:** 2026-08-07

O formato 3.0-pool está implementado, testado e mergeado no `main` do
`isage_cd` (commit `225dd90`). Suite com 21 testes passando (pool helpers,
build, migração, override de predição, widget offscreen, export/import).

## O que mudou no software

- Cena = pasta de imagens datadas: `data/dataset/train/<cena>/<YYYYMM>.png`
  (aceita `YYYYMMDD` também). Sem `images/`, `images_before/`, `pair_meta/`.
- UI: seletor de data sobre CADA canvas (`,`/`.` passa o antes,
  `Ctrl+,`/`Ctrl+.` passa o depois). O dropdown do antes só oferece datas
  anteriores ao depois corrente. Ao abrir uma cena, o widget cai no último
  par anotado dela.
- Anotação: `iteration_N/annotations/<cena>/<antes>_<depois>.json`.
- Predições agora são POR PAR:
  `iteration_N/predictions/<cena>/<antes>_<depois>.png`. O overlay usa
  exatamente o arquivo do par ativo (sem fallback pra outro par).
- `tools/build_session.py`: entrada nova = pasta de cenas datadas.
- `tools/migrate_session.py SRC DST`: converte 2.1-pair → 3.0-pool; origem
  intocada, destino precisa não existir.
- O anotador só lê 3.0-pool. Sessão antiga aberta por engano mostra o aviso
  de migração no canvas.

## ATENÇÃO — uma divergência do seu §3.2

No schema 3.0-pool as DUAS datas do bloco `pair` são labels de dígitos:

```json
"pair": {"scene": "0000", "date_before": "202106", "date_after": "202206"}
```

O seu rascunho de conversão v1.0 mantinha `date_after: "2022-06"` — ajusta
pro label `"202206"` no seu script. Também: `image.name` é o caminho
relativo no pool (`"0000/202206.png"`), e `iteration` = número da pasta
`iteration_N` onde o arquivo mora. Confere o formato exato em
`tools/migrate_session.py` (função `migrate`) e nos testes
(`tests/test_migrate_session.py`) do repo `isage_cd`.

## O que preciso de você

1. `git -C D:\projects\isage_cd pull` (branch `main`).
2. Converter a sessão real v1.0 (2000 tiles) pro 3.0-pool **numa cópia**,
   com o seu script sessão-específico (estendendo o
   `convert_amazon_session.py`), seguindo o §3 da sua referência + a
   correção acima. A amostra de 20 tiles (2.1-pair) você converte direto
   com `python tools/migrate_session.py`.
3. Abrir a sessão convertida no anotador novo e regerar o screenshot da
   Fig 1A (os dois seletores de data visíveis, um par com pontos e overlay
   de predição ligado ajudam a contar a história da figura).
4. Commitar o screenshot aqui no repo do paper (`figures/screenshot_ui.png`
   ou nome novo) e avisar num MD do handoff.

Qualquer coisa estranha na migração (contagem de pontos não batendo,
predição órfã), me escreve um MD aqui no `handoff/` que eu corrijo o
script do lado de cá.
