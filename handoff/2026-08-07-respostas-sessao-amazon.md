# Respostas: sessao Amazon

Raiz: `D:\projects\isage_cd\Sessions\Amazon`

## 1. Configs

### session_config.json
```json
{
  "current_iteration": 5
}
```

### dataset_metadata.json
```json
{
  "classes": {
    "num_classes": 2,
    "ignore_index": 2,
    "class_info": {
      "0": {
        "name": "No change",
        "slug": "no_change",
        "color": "#2e8b3d"
      },
      "1": {
        "name": "Change",
        "slug": "change",
        "color": "#e5194b"
      }
    }
  }
}
```

## 2. Layout de data/dataset/train
```
images/
  0000.png
  0001.png
  0002.png
  0003.png
  ... (+16)
images_before/
  0000/  (1 itens: ['antes_202106.png'])
  0001/  (1 itens: ['antes_202106.png'])
  0002/  (1 itens: ['antes_202106.png'])
  0003/  (1 itens: ['antes_202106.png'])
  ... (+16)
pair_meta/
  0000.json
  0001.json
  0002.json
  0003.json
  ... (+16)
```

Total de frames em images/: 20

## 3. pair_meta (20 arquivos) - exemplo
```json
{
  "date_after": "2022-06",
  "product": "PlanetScope"
}
```

Referencias por frame (n_refs: n_frames): {1: 20}

## 4. Iteracoes

- **iteration_0**: 0 pares anotados, 0 pontos, 0 cenas | 10 predicoes (ex: iteration_0\predictions\0000.png) | models: []
- **iteration_1**: 0 pares anotados, 0 pontos, 0 cenas | 10 predicoes (ex: iteration_1\predictions\0000.png) | models: []
- **iteration_2**: 0 pares anotados, 0 pontos, 0 cenas | 10 predicoes (ex: iteration_2\predictions\0000.png) | models: []
- **iteration_3**: 0 pares anotados, 0 pontos, 0 cenas | 10 predicoes (ex: iteration_3\predictions\0000.png) | models: []
- **iteration_4**: 0 pares anotados, 0 pontos, 0 cenas | 20 predicoes (ex: iteration_4\predictions\0000.png) | models: []
### Exemplo de JSON (iteration_5\annotations\0000\202106.json)
```json
{
  "format_version": "2.1-pair",
  "image": {
    "name": "0000.png",
    "width": 1024,
    "height": 1024
  },
  "iteration": 5,
  "created_at": "2026-08-06T22:28:30.230569Z",
  "pair": {
    "frame": "0000",
    "month_before": "202106",
    "date_after": "2022-06"
  },
  "annotations": [
    [
      71,
      929,
      1
    ],
    [
      82,
      956,
      1
    ],
    [
      68,
      959,
      1
    ],
    [
      148,
      919,
      1
    ],
    [
      134,
      951,
      1
    ],
    [
      253,
      895,
      1
    ],
    [
      490,
      514,
      1
    ],
    [
      535,
      480,
      1
    ],
    [
      406,
      373,
      1
    ],
    [
      513,
      664,
      1
    ],
    [
      632,
      465,
      1
    ],
    [
      604,
      319,
      1
    ],
    [
      475,
      311,
      1
    ],
    [
      608,
      131,
      1
    ],
    [
      362,
      150,
      1
    ],
    [
      295,
      262,
      1
    ],
    [
      350,
      542,
      1
    ],
    [
      398,
      550,
      1
    ],
    [
      787,
      364,
      1
    ],
    [
      291,
      724,
      1
    ],
    [
      49,
      625,
      1
    ],
    [
      9,
      605,
      1
    ],
    [
      267,
      140,
      1
    ],
    [
      363,
      124,
      1
    ],
    [
      575,
      191,
      1
    ],
    [
      495,
      314,
      1
    ],
    [
      246,
      421,
      1
    ],
    [
      196,
      231,
      1
    ],
    [
      107,
      231,
      1
    ],
    [
      916,
      527,
      0
    ],
    [
      913,
      905,
      0
    ],
    [
      1014,
      862,
      0
    ],
    [
      902,
      617,
      0
    ],
    [
      947,
      91,
      0
    ],
    [
      966,
      19,
      0
    ],
    [
      688,
      136,
      0
    ],
    [
      665,
      192,
      0
    ],
    [
      823,
      262,
      0
    ],
    [
      986,
      268,
      0
    ],
    [
      971,
      726,
      0
    ],
    [
      876,
      995,
      0
    ],
    [
      960,
      345,
      0
    ],
    [
      907,
      206,
      0
    ],
    [
      992,
      201,
      0
    ],
    [
      822,
      540,
      0
    ],
    [
      948,
      801,
      0
    ],
    [
      851,
      913,
      0
    ],
    [
      973,
      873,
      0
    ],
    [
      905,
      462,
      0
    ],
    [
      989,
      380,
      0
    ],
    [
      723,
      959,
      1
    ],
    [
      666,
      991,
      1
    ],
    [
      692,
      815,
      1
    ],
    [
      441,
      800,
      1
    ],
    [
      450,
      910,
      1
    ],
    [
      555,
      941,
      1
    ],
    [
      883,
      716,
      0
    ],
    [
      915,
      279,
      0
    ],
    [
      966,
      958,
      0
    ],
    [
      853,
      963,
      0
    ],
    [
      943,
      640,
      0
    ],
    [
      965,
      568,
      0
    ],
    [
      723,
      279,
      0
    ],
    [
      689,
      358,
      0
    ],
    [
      715,
      527,
      0
    ],
    [
      755,
      501,
      0
    ],
    [
      857,
      458,
      0
    ],
    [
      488,
      680,
      0
    ],
    [
      492,
      695,
      0
    ],
    [
      945,
      872,
      0
    ],
    [
      323,
      307,
      1
    ],
    [
      71,
      763,
      1
    ],
    [
      129,
      728,
      1
    ],
    [
      621,
      817,
      1
    ],
    [
      649,
      741,
      1
    ],
    [
      166,
      841,
      1
    ],
    [
      66,
      798,
      1
    ],
    [
      268,
      339,
      1
    ],
    [
      387,
      563,
      1
    ],
    [
      396,
      462,
      1
    ]
  ]
}
```

- **iteration_5**: 20 pares anotados, 2764 pontos, 20 cenas | 0 predicoes (ex: -) | models: []

---

## Respostas manuais

### ⚠️ Nota importante antes das respostas

A sessão em `D:\projects\isage_cd\Sessions\Amazon` que o script varreu é
uma **amostra de 20 tiles** que montei aqui só pra gerar o screenshot
da Fig 1A. **Não é a sessão real que produziu os 143.634 pontos e as 5
iterações do paper.**

A sessão real (2000 tiles, 5 iterações, os modelos que geraram Fig 2 e
Fig 3) vive em `D:\projects\amazon\DATA\train_1024\` no formato **antigo
do cd_annotator** (predecessor do isage_cd), que tem uma hierarquia
diferente:

```
D:\projects\amazon\DATA\train_1024\
├── t1\<NNNN>.tif                   ← T1 Planet 4-band uint16 GeoTIFF
├── t2\<NNNN>.tif                   ← T2 Planet 4-band uint16 GeoTIFF
├── annotations\<NNNN>.json          ← formato v1.0 antigo (não 2.1-pair!)
│                                     um JSON por tile, não por par
├── metadata.json                    ← Bloco A tile positions (0000-0999)
├── metadata_newpair.json            ← Bloco B tile positions (1000-1999)
├── masks_sparse_v[1..5]\<NNNN>.png ← masks binárias por iteração
├── model[_v2..v5]\unet_b7_*.pth    ← checkpoints por iteração
└── model[_v2..v5]\metrics.json      ← loss por época por iteração
```

O JSON antigo é `{"format_version": "1.0", "class_mode": "binary",
"class_names": [...], "image": {...}, "annotations": [[x, y, cls], ...]}`
— **sem bloco `pair`, sem `iteration`, sem `date_after`**. As datas do
par são implícitas pela posição do tile (Block A vs Block B).

Isso importa pra `migrate_session.py`:
- **Migração 2.1-pair → 3.0-pool** (que o script atual assume) funciona
  na amostra de 20 tiles mas produz uma sessão irrelevante pro paper.
- **Migração do formato v1.0 antigo → 3.0-pool** é o que a validação
  precisa, e é um caminho de código diferente (JSON schema diferente,
  imagens em .tif uint16 em vez de .png uint8, hierarquia diferente).

Sugiro adotar essa segunda migração como escopo do `migrate_session.py`
(ou fazer dois modos), porque só ela produz a sessão real do paper no
formato novo.

### Respostas às 5 perguntas (baseadas na sessão real, não na amostra)

1. **Cada frame tem quantas referências (`antes_*.png`)?**
   Na sessão real: **uma única por frame**. Nunca houve caso de mesmo
   frame com múltiplas referências datadas. As duas datas T1/T2 são
   uniformes por bloco:
   - Block A (tiles 0000-0999): T1 = 2021-06, T2 = 2022-06
   - Block B (tiles 1000-1999): T1 = 2021-08, T2 = 2022-07

   Consequência boa pra migração: nunca há ambiguidade de qual predição
   por-frame virar por-par.

2. **O `date_after` é o mesmo pra todos os frames?**
   Não, varia por bloco: **2022-06 para tiles 0000-0999**, **2022-07
   para tiles 1000-1999**. O `migrate_session.py` precisa consultar
   `metadata.json` vs `metadata_newpair.json` (ou detectar pelo range do
   tile ID) pra atribuir a data certa.

3. **Onde estão os scripts de treino/predição das 5 iterações?**

   Repo: **github.com/osmarluiz/amazon-deforestation-cd**
   (clone local em `D:\projects\amazon`)

   Treino de referência (o que a comunidade replicaria):
   - `CODE\tests\train_1024_v5_amp.py` — o script real que produziu
     `model_v5` (iteração 5). Warm-start de `model_v4/ep147.pth`.
     Usa SMP `Unet` + `EfficientNet-B7` + `DWCBCELossSimple`
     (error-weighted, ignora `255`).

   Predição de referência:
   - `CODE\scripts\predict_fullimage_v5.py` — Bloco A
     (Jun 2021/Jun 2022, dois `.dat` ENVI separados)
   - `CODE\scripts\predict_fullimage_v5_newpair.py` — Bloco B
     (Aug 2021/Jul 2022, um `.dat` ENVI 8-band stacked)

   Ambos usam sliding window 1024 + stride 512 (50% overlap averaging),
   `torch.amp.autocast(bfloat16)`, chunk 4096×4096.

   Tem também um `train_1024_v6_amp.py` mais recente (versão v6 do
   refine, warm-start do v5 ep139) — mas os números do paper vieram do
   v5 então v5 é o que vale referenciar.

4. **Espaço em disco pra rodar migração numa cópia da sessão?**

   Na máquina de escrita do paper eu não tenho a sessão real (só a
   amostra de 20 tiles). A sessão real está aqui na máquina de anotação
   (`D:\projects\amazon\`), com:
   - `DATA\train_1024\stack\` (pré-processado, ~32 GB)
   - `DATA\train_1024\model_v[1..5]\` (~1.5 GB de checkpoints por
     iteração, o total é grande)
   - `DATA\train_1024\masks_sparse_v[1..5]\` (~2 GB cada)

   Se a migração for feita aqui, sim tem espaço pra uma cópia (o D:
   tem >200 GB livres). Se for feita na máquina do paper, precisa
   sincronizar os JSONs de anotação + as duas metadata.json + os
   checkpoints do modelo — talvez ~500 MB apenas do essencial pra
   migração.

5. **Screenshot novo da Fig 1A com dois seletores de data:**

   Beleza, quando a UI nova estiver pronta eu regero o screenshot.
   Um pedido: assim que `migrate_session.py` e a UI 3.0-pool
   estabilizarem, avisa que eu:
   - Migro a sessão real (2000 tiles, 5 iterações)
   - Tiro o screenshot novo com dois seletores de data visíveis
   - Recompilo Fig 1 no repo do paper

### Recomendação de próximo passo

Antes de escrever `migrate_session.py`, decidir explicitamente:
- (a) Migração 2.1-pair → 3.0-pool (fácil, amostra pequena, mas produz
  sessão irrelevante pro paper)
- (b) Migração v1.0 antigo → 3.0-pool (necessária, o que a validação
  do paper precisa referenciar)

Eu voto em **(b) como escopo principal**, com (a) opcional se ficar
trivial de codar em conjunto.
