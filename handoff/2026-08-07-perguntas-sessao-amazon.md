# Pedido de info: sessão Amazon (PRODES 2022)

**De:** máquina do paper (D:\ACADEMIC\PAPERS\isage_cd_methodx)
**Para:** máquina que tem a sessão Amazon
**Motivo:** vamos migrar o formato de sessão para "pool de datas"
(ver `docs/superpowers/specs/2026-08-07-pool-format-design.md`) e
preciso da estrutura exata da sessão pra escrever o script de migração
sem chutar nada — e das estatísticas reais pra seção de validação.

## Como responder

Rode o script abaixo apontando pra raiz da sessão Amazon e commite a
saída como `handoff/2026-08-07-respostas-sessao-amazon.md`:

```bash
python dump_session_info.py /caminho/para/Sessions/Amazon > handoff/2026-08-07-respostas-sessao-amazon.md
```

Script (salve como `dump_session_info.py` em qualquer lugar):

```python
import json, sys
from pathlib import Path

root = Path(sys.argv[1])
print(f"# Respostas: sessao Amazon\n\nRaiz: `{root}`\n")

print("## 1. Configs\n")
for name in ["session_config.json", "dataset_metadata.json"]:
    p = root / "config" / name
    print(f"### {name}\n```json")
    print(p.read_text(encoding="utf-8") if p.exists() else "AUSENTE")
    print("```\n")

train = root / "data" / "dataset" / "train"
print("## 2. Layout de data/dataset/train\n```")
for d in sorted(train.iterdir()):
    print(d.name + "/")
    if d.is_dir():
        kids = sorted(d.iterdir())
        for k in kids[:4]:
            if k.is_dir():
                inner = sorted(x.name for x in k.iterdir())
                print(f"  {k.name}/  ({len(inner)} itens: {inner[:6]}{'...' if len(inner) > 6 else ''})")
            else:
                print(f"  {k.name}")
        if len(kids) > 4:
            print(f"  ... (+{len(kids)-4})")
print("```\n")

imgs = train / "images"
if imgs.exists():
    frames = sorted(imgs.glob("*.png"))
    print(f"Total de frames em images/: {len(frames)}\n")

pm_dir = train / "pair_meta"
if pm_dir.exists():
    pms = sorted(pm_dir.iterdir())
    print(f"## 3. pair_meta ({len(pms)} arquivos) — exemplo\n```json")
    print(pms[0].read_text(encoding="utf-8"))
    print("```\n")
    befores = train / "images_before"
    if befores.exists():
        counts = {}
        for f in befores.iterdir():
            n = len(list(f.glob("*.png")))
            counts[n] = counts.get(n, 0) + 1
        print(f"Referencias por frame (n_refs: n_frames): {counts}\n")

print("## 4. Iteracoes\n")
sample_shown = False
for it in sorted(root.glob("iteration_*")):
    ann = it / "annotations"
    n_pairs = n_pts = 0
    scenes = set()
    if ann.exists():
        for jf in ann.rglob("*.json"):
            n_pairs += 1
            scenes.add(jf.parent.name)
            try:
                n_pts += len(json.loads(jf.read_text(encoding="utf-8"))["annotations"])
            except Exception as e:
                print(f"  ERRO lendo {jf}: {e}")
            if not sample_shown:
                print(f"### Exemplo de JSON ({jf.relative_to(root)})\n```json")
                print(jf.read_text(encoding="utf-8"))
                print("```\n")
                sample_shown = True
    preds = it / "predictions"
    n_preds = len(list(preds.rglob("*.png"))) if preds.exists() else 0
    pred_sample = next(preds.rglob("*.png"), None) if preds.exists() else None
    models = it / "models"
    model_names = sorted(m.name for m in models.iterdir()) if models.exists() else []
    print(f"- **{it.name}**: {n_pairs} pares anotados, {n_pts} pontos, "
          f"{len(scenes)} cenas | {n_preds} predicoes "
          f"(ex: {pred_sample.relative_to(root) if pred_sample else '-'}) | "
          f"models: {model_names}")
```

## Perguntas extras (responder no fim do MD, à mão)

1. Cada frame tem quantas referências (`antes_*.png`)? Uma só ou várias?
   (o script já mostra, mas confirma se a sessão real usou só uma)
2. O `date_after` é o mesmo pra todos os frames (2022-06?) ou varia?
3. Onde estão os scripts de treino/predição usados nas 5 iterações
   (repo/pasta)? Vou referenciá-los como "trainer de referência" no paper.
4. Tem espaço em disco aí pra rodar a migração numa CÓPIA da sessão
   quando o `migrate_session.py` ficar pronto? (não quero mexer na
   original)
5. Depois da migração e da UI nova, vou pedir um screenshot novo da
   interface (Fig 1A) — só avisando desde já.
