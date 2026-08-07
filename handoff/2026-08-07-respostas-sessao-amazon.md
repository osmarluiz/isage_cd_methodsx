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
## Respostas manuais às 5 perguntas

1. **Cada frame tem quantas referências (`antes_*.png`)?**
   **Uma por frame**, sempre. Nunca houve caso de mesmo frame com
   múltiplas referências datadas. Consequência boa pra migração:
   nenhuma ambiguidade ao mapear predição por-frame para predição
   por-par.

2. **O `date_after` é o mesmo pra todos os frames?**
   Não, varia por bloco. Na sessão do paper existem dois blocos:
   - Bloco A (tiles 0000-0999): T1 = 2021-06, T2 = 2022-06
   - Bloco B (tiles 1000-1999): T1 = 2021-08, T2 = 2022-07

   O `date_after` já está no `pair_meta/<frame>.json` — o
   `migrate_session.py` só precisa ler dali.

3. **Onde estão os scripts de treino/predição das 5 iterações?**
   Repo: **github.com/osmarluiz/amazon-deforestation-cd**

   - Treino de referência (produziu `model_v5`):
     `CODE/tests/train_1024_v5_amp.py` — SMP `Unet` +
     `EfficientNet-B7` + `DWCBCELossSimple` (error-weighted,
     `ignore_value=255`). Warm-start de `model_v4/ep147.pth`.
   - Predição:
     `CODE/scripts/predict_fullimage_v5.py` (Bloco A) e
     `CODE/scripts/predict_fullimage_v5_newpair.py` (Bloco B) —
     ambos com sliding window 1024, stride 512 (50% overlap),
     `torch.amp.autocast(bfloat16)`, chunk 4096.

4. **Espaço em disco pra rodar migração numa cópia?**
   Sim, D: aqui tem 200 GB+ livres. Sem risco de estourar.

5. **Screenshot novo da Fig 1A com dois seletores de data.**
   Ok — assim que a UI 3.0-pool estabilizar, avisa que eu regero.
