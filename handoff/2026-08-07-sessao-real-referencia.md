# Sessão Amazon real — referência técnica completa

**Objetivo:** dar ao autor do `migrate_session.py` todos os detalhes
concretos (paths, schemas, contagens) da sessão real, tanto no
formato v1.0 antigo (repo `amazon`) quanto no formato 2.1-pair
(sample no repo `isage_cd`). O que não estiver aqui ou no dump
automático (`2026-08-07-respostas-sessao-amazon.md`) me pergunta.

---

## 1. Localizações

| Item | Path (máquina de anotação) |
|---|---|
| Sessão v1.0 antiga (2000 tiles, 5 iterações) | `D:\projects\amazon\DATA\train_1024\` |
| Sessão 2.1-pair (amostra 20 tiles, screenshot) | `D:\projects\isage_cd\Sessions\Amazon\` |
| Predições full-image do v5 (Blocos A e B) | `D:\projects\amazon\DATA\prediction_full_1024_v5{,_newpair}.tif` |
| Scripts de treino/predict | `D:\projects\amazon\CODE\` (repo `amazon-deforestation-cd`) |

---

## 2. Estrutura do formato v1.0 antigo (a sessão do paper)

```
D:\projects\amazon\DATA\train_1024\
├── t1\                              # 2000 tiles, T1 Planet 4-band uint16 GeoTIFF
│   └── <NNNN>.tif                   # 1024x1024, bands = B, G, R, NIR
├── t2\                              # 2000 tiles, T2 Planet 4-band uint16 GeoTIFF
├── stack\                           # 2000 pré-processados (T1+T2 → 8ch .npy)
│   └── <NNNN>.npy                   # opcional; usado pelo trainer pra velocidade
├── annotations\                     # 2000 JSONs no formato v1.0 (um por TILE, não por PAR)
│   └── <NNNN>.json
├── metadata.json                    # Bloco A: tiles 0000..0999
├── metadata_newpair.json            # Bloco B: tiles 1000..1999
├── masks_sparse\                    # iter 1: 1000 masks (Bloco A somente)
├── masks_sparse_v2\                 # iter 2: 1000 masks
├── masks_sparse_v3\                 # iter 3: 1000 masks
├── masks_sparse_v4\                 # iter 4: 1000 masks
├── masks_sparse_v5\                 # iter 5: 2000 masks (Blocos A + B)
├── model\                           # iter 1: 150 .pth + metrics.json + train_log.txt
├── model_v2\                        # iter 2: 21 .pth + metrics.json
├── model_v3\                        # iter 3: 150 .pth + metrics.json
├── model_v4\                        # iter 4: 150 .pth + metrics.json
├── model_v5\                        # iter 5: 150 .pth + metrics.json
├── predictions\                     # iter 1: 1000 PNGs per-tile (Bloco A)
├── predictions_v2\                  # iter 2: 1000
├── predictions_v3\                  # iter 3: 1000
├── predictions_v4\                  # iter 4: 1000
└── (predictions_v5 não existe — v5 gerou apenas full-image .tif)
```

### 2.1 `metadata.json` (Bloco A) — schema real

```json
{
  "patch_size": 1024,
  "total": 1000,
  "change": 658,
  "low_change": 292,
  "no_change": 50,
  "patches": [
    {"name": "0000.tif", "col": 45056, "row": 10240,
     "change_pct": 73.3106, "category": "change"},
    ...
  ]
}
```

Nomes de arquivos vão de `0000.tif` até `0999.tif`. Todos são do
par T1=2021-06 / T2=2022-06.

### 2.2 `metadata_newpair.json` (Bloco B) — schema real

```json
{
  "patch_size": 1024,
  "start_index": 1000,
  "source_image": "PRODES-2021_8-2022-7/Prodes_2021-08_2022-7",
  "grid_offset": 512,
  "total": 1000,
  "change": 658,
  "low_change": 292,
  "no_change": 50,
  "patches": [
    {"name": "1000.tif", "col": 44544, "row": 10240,
     "change_pct": 87.3225, "category": "change"},
    ...
  ]
}
```

Nomes de arquivos vão de `1000.tif` até `1999.tif`. Todos são do
par T1=2021-08 / T2=2022-07 (calendário PRODES 2022).

### 2.3 JSON de anotação v1.0 — schema real

```json
{
  "format_version": "1.0",
  "class_mode": "binary",
  "class_names": ["background", "foreground"],
  "image": {"name": "0000.tif", "width": 1024, "height": 1024},
  "created_at": "2026-07-30T16:51:26.464848Z",
  "annotations": [
    [71, 929, 1],
    [82, 956, 1],
    [68, 959, 1],
    ...
  ]
}
```

- Um JSON por **tile** (não por par).
- Sem bloco `pair`, sem `iteration`, sem `date_after`.
- `annotations` é lista de `[x, y, class]` (`x` = coluna, `y` = linha,
  origem no canto superior esquerdo).
- Classes: `0` = no change, `1` = change; `class_names` na ordem.
- `image.name` referencia o `.tif` (não `.png`); a resolução da grade
  é 1024×1024.

### 2.4 Como distinguir Bloco A vs Bloco B (para mapear datas)

**Pelo número do tile:**
- `0000` a `0999` → Bloco A: T1=`2021-06`, T2=`2022-06`
- `1000` a `1999` → Bloco B: T1=`2021-08`, T2=`2022-07`

Ou, equivalentemente, consultar qual `metadata*.json` contém o tile:
o Bloco A está listado em `metadata.json`; o Bloco B, com
`start_index: 1000`, em `metadata_newpair.json`.

### 2.5 Estatísticas globais (o que a Method Validation cita)

- **Tiles:** 2000 (1000 por bloco)
- **JSONs de anotação:** 2000
- **Tiles com pelo menos 1 ponto:** 1999
- **Total de pontos:** 143.634
- **Pontos por tile:** mín 3, máx 702, mediana 43, média 71.9
- **Split de classes:** 54.6% no change, 45.4% change

### 2.6 Iterações (v1..v5) — snapshot dos `metrics.json`

| Iter | Pasta | Épocas | Best epoch | Best loss | Notas |
|---|---|---|---|---|---|
| 1 | `model/` | 148 | 129 | 0.0134 | Do zero |
| 2 | `model_v2/` | 21 | 15 | 0.0086 | Warm-start curto (menor loss observado) |
| 3 | `model_v3/` | 150 | 97 | 0.0224 | Loss sobe ao adicionar segunda metade do Bloco A |
| 4 | `model_v4/` | 151 | 147 | 0.0152 | |
| 5 | `model_v5/` | 150 | 139 | 0.0153 | Introduz Bloco B; base do `model_v5` que gera a Fig 3 |

Cada `model_vN/` contém um `metrics.json` no formato:

```json
[{"epoch": 1, "loss": 0.300129, "best_loss": 0.300129,
  "is_best": true,
  "model_file": "unet_b7_1024v5_ep001.pth",
  "timestamp": "2026-04-15 21:33:41"}, ...]
```

### 2.7 Predições

- **Per-tile PNG por iteração** existem em `predictions/`,
  `predictions_v2..v4/` (1000 PNGs cada; Bloco A somente,
  valores 0/1 uint8, 1024×1024). Não existe `predictions_v5/`.
- **Full-image v5 TIF** em `D:\projects\amazon\DATA\`:
  - `prediction_full_1024_v5.tif` (27.7 MB) — Bloco A completo
  - `prediction_full_1024_v5_newpair.tif` (27.3 MB) — Bloco B completo
- Ambos com resolução 65536×53248 (cena completa), sliding window
  1024 + stride 512 (50% overlap), threshold 0.5.

Pra obter a predição v5 por-tile:

- Bloco A: crop 1024×1024 em `(col, row)` de `metadata.json` no
  `prediction_full_1024_v5.tif`.
- Bloco B: mesma coisa em `prediction_full_1024_v5_newpair.tif`
  usando `metadata_newpair.json`.

Foi assim que a Fig 3 (qualitativa) foi gerada — script em
`isage_cd_methodsx/tools_scratch/plot_qualitative.py`.

---

## 3. Regras de migração v1.0 → 3.0-pool

Mapeamento explícito, campo a campo. Para cada tile `<NNNN>` (com bloco
inferido pelo número):

### 3.1 Imagens

Cada tile no formato v1.0 tem `t1/<NNNN>.tif` e `t2/<NNNN>.tif` em
Planet 4-band uint16. No formato 3.0-pool as imagens vão pra
`data/dataset/train/<cena>/<data>.png` onde `<cena> = <NNNN>` e
`<data>` é a data no formato `YYYYMM`.

- `<data>` do T1: `202106` (Bloco A) ou `202108` (Bloco B).
- `<data>` do T2: `202206` (Bloco A) ou `202207` (Bloco B).
- Conversão de imagem: TIF uint16 4-band → PNG uint8 RGB (percentile
  stretch p2/p98 nas bandas 3, 2, 1). Ver
  `tools_scratch/convert_amazon_session.py` no repo `isage_cd` pra o
  código exato — já foi testado e produz o que aparece na Fig 1A.

### 3.2 Anotações

Cada `annotations/<NNNN>.json` (v1.0, um por tile) vira **um único**
`iteration_5/annotations/<NNNN>/<antes>_<depois>.json` no formato
3.0-pool.

Motivo do `iteration_5`: as anotações que existem hoje são o resultado
acumulado das 5 iterações, então elas pertencem à rodada corrente
(`current_iteration = 5`).

Conversão de conteúdo:

```python
old = {
  "format_version": "1.0",
  "class_mode": "binary",
  "class_names": ["background", "foreground"],
  "image": {"name": "0000.tif", "width": 1024, "height": 1024},
  "created_at": "...",
  "annotations": [[x, y, c], ...]
}

# Bloco inferido pelo número do tile:
tile_id = "0000"           # da chave 'image.name'
if int(tile_id) < 1000:
    date_before, date_after = "202106", "2022-06"
else:
    date_before, date_after = "202108", "2022-07"

new = {
  "format_version": "3.0-pool",
  "image": {"name": f"{tile_id}.png", "width": 1024, "height": 1024},
  "iteration": 5,
  "created_at": old["created_at"],
  "pair": {"scene": tile_id,
           "date_before": date_before,
           "date_after": date_after},
  "annotations": old["annotations"],   # inalteradas
}
# Path: iteration_5/annotations/<tile_id>/<date_before>_<date_after>.json
```

Notar:
- `class_mode`, `class_names` são omitidos no schema 3.0-pool (movidos
  pra `dataset_metadata.json`, que já existe no formato certo na
  sessão isage_cd).
- `image.name` troca `.tif` por `.png` (pra bater com o pool de
  imagens).
- Pontos `[x, y, c]` são preservados como estão. `x`, `y` continuam
  em pixel, origem topo-esquerdo, `c` = índice de classe.
- O JSON antigo NÃO tem `iteration` nem `created_at` por iteração
  — o `created_at` do JSON antigo pode ser preservado (é o timestamp
  do último clique salvo).

### 3.3 pair_meta (arquivos por-cena) — **eliminado no 3.0-pool**

O design diz que `pair_meta/` some porque as datas vêm dos nomes de
arquivo. Então nada de `pair_meta/` no destino.

### 3.4 Predições

- `predictions/`, `predictions_v2..v4/`: são per-tile 0/1 PNGs. Só
  existem para o Bloco A. Pra migrar, cada
  `predictions_vN/<NNNN>.png` vira
  `iteration_{N-1}/predictions/<NNNN>/<antes>_<depois>.png` — o
  offset de 1 porque no isage_cd a predição da rodada N é *o overlay
  da rodada N+1*.
- `prediction_full_1024_v5{,_newpair}.tif` gera, via crop, as
  predições per-tile de `iteration_4/predictions/<NNNN>/<antes>_<depois>.png`
  (v5 = índice 4 no isage_cd).

Ou seja, no destino esperamos:

| Iter isage_cd | Fonte no repo `amazon` | Cobertura de tiles |
|---|---|---|
| `iteration_0/predictions/` | `predictions/` (v1) | Bloco A somente |
| `iteration_1/predictions/` | `predictions_v2/` | Bloco A somente |
| `iteration_2/predictions/` | `predictions_v3/` | Bloco A somente |
| `iteration_3/predictions/` | `predictions_v4/` | Bloco A somente |
| `iteration_4/predictions/` | Crop de `prediction_full_1024_v5{,_newpair}.tif` | Blocos A + B |
| `iteration_5/predictions/` | (vazio; usuário vai anotar aqui) | — |

### 3.5 Modelos

`model/`, `model_v2..v5/` → `iteration_{N-1}/models/`. Só o
`best_model.pth` de cada iteração precisa ser migrado (o script v5
salva 150 checkpoints; só o melhor é útil pra referência). O
`metrics.json` de cada `model_vN/` pode ser preservado como
`iteration_{N-1}/models/metrics.json` — é ele que sustenta Fig 2 do
paper.

### 3.6 `session_config.json` e `dataset_metadata.json`

- `session_config.json`: `{"current_iteration": 5}` — igual à sessão
  isage_cd atual.
- `dataset_metadata.json`: reutilizar o da sessão isage_cd atual (2
  classes, `No change` verde `#2e8b3d` e `Change` vermelho
  `#e5194b`). O v1.0 tem `class_names: ["background", "foreground"]`
  — só os nomes cosméticos; o mapeamento numérico (0/1) é o mesmo.

---

## 4. Scripts de treino e predição (pra citar no paper)

Repo: **github.com/osmarluiz/amazon-deforestation-cd**

### 4.1 Treino

`CODE/tests/train_1024_v5_amp.py` — o script real que produziu
`model_v5`:

- Modelo: `segmentation_models_pytorch.Unet` com encoder
  `efficientnet-b7`, 8 canais de entrada, 1 classe, ativação sigmoid.
- Loss: `DWCBCELossSimple(w_cc=1, w_uc=1, w_cw=10, w_uw=10,
  ignore_value=255, from_logits=False)`.
- Otimizador: `Adam(lr=5e-5)`.
- AMP: `torch.amp.autocast('cuda', dtype=torch.bfloat16)`.
- 150 épocas com early save por época; warm-start do
  `model_v4/unet_b7_1024v4_ep147.pth`.
- Data pipeline: lê `stack/<NNNN>.npy` (8×1024×1024) + `masks_sparse_v5/<NNNN>.png` (uint8
  com ignore=255).

### 4.2 Predição full-image

- `CODE/scripts/predict_fullimage_v5.py` (Bloco A):
  - `T1 = 2021-06/2021-06.dat`, `T2 = 2022-06/2022-06.dat` (dois
    arquivos ENVI separados, cada um 4 bandas).
  - Sliding window 1024, stride 512, chunk 4096×4096.
- `CODE/scripts/predict_fullimage_v5_newpair.py` (Bloco B):
  - Stack único ENVI de 8 bandas em
    `PRODES-2021_8-2022-7/Prodes_2021-08_2022-7`.
  - Mesma window/stride/chunk.

Ambos com `bfloat16` AMP, `threshold=0.5`, output GTiff uint8 LZW.

---

## 5. Perguntas ainda em aberto

1. **Separador do JSON:** confirma se é `_` mesmo em
   `<antes>_<depois>.json` (por exemplo `202106_202206.json`) — se
   preferir outro (`-`, `..`), fala aí.
2. **Formato da data:** o design pede
   "string de dígitos ordenável (`YYYYMM` ou `YYYYMMDD`)". Vou usar
   `YYYYMM` (bate com o que o pair_meta atual guarda). Ok?
3. **Iteração 5 na migração:** todas as anotações v1.0 viram
   `iteration_5/annotations/`, e `iteration_0..4/annotations/` fica
   vazio (só predictions e models). Faz sentido, ou você prefere
   redistribuir?
4. **Espelhamento das predições:** faço o crop dos dois full-image
   TIF pra popular `iteration_4/predictions/<cena>/<antes>_<depois>.png`
   no script de migração, ou você quer manter separado (script de
   crop à parte)?
