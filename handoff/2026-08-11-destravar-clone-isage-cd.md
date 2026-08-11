# Como destravar o clone do isage_cd e tirar o screenshot

**De:** máquina do paper
**Para:** máquina de anotação
**Data:** 2026-08-11

O `2026-08-11-decisoes-pendentes.md` §3 diagnosticou por que o
screenshot novo não saiu: o clone local do `isage_cd` está **11
commits atrás e com 160 linhas não commitadas**, então o código aí
ainda é anterior ao `be43b98`, que implementou o segundo seletor de
data. Não adianta capturar a tela desse código, porque ele não tem a
feature que o paper descreve.

Este é o único bloqueio da submissão. Passo a passo:

## 1. Descobrir o que são as 160 linhas

```powershell
cd D:\projects\isage_cd
git status
git diff --stat
git stash list
```

Se for trabalho que interessa, `git stash push -m "wip antes do pool"`
guarda sem perder. Se for lixo de teste, `git checkout -- .` descarta.
**Não faça `git checkout -- .` sem olhar o diff antes** — pode haver
ajuste local que ninguém replicou.

## 2. Atualizar

```powershell
git pull
```

Depois do pull o repo tem: formato 3.0-pool com os dois seletores
(`be43b98`), `tools/migrate_session.py`, `tools/rasterize.py` e a
suíte de 27 testes. Confere com:

```powershell
$env:QT_QPA_PLATFORM='offscreen'; python -m pytest tests/ -q
```

Se algum teste falhar, me manda a saída em vez de contornar.

## 3. Ter uma sessão no formato novo

O anotador só abre 3.0-pool. Se a sessão local ainda for 2.1-pair:

```powershell
python tools\migrate_session.py Sessions\Amazon Sessions\Amazon_pool
```

A origem não é tocada e o destino não pode existir.

## 4. Capturar

Abrir maximizado e capturar a janela com:

- os **dois seletores de data** visíveis, um sobre cada canvas
- um par **com pontos** colocados, aparecendo nos dois lados
- o **overlay de predição ligado** (tecla `P` ou o slider), que é a
  superfície que o usuário revisa
- de preferência um tile com desmatamento visível

Salvar como `figures/screenshot_ui.png` no repo do paper, substituindo
o atual, e commitar.

Se capturar offscreen no Windows, lembra do
`QT_QPA_FONTDIR=C:\Windows\Fonts`, senão o texto vira tofu.

## Por que isso importa mais que o resto

A legenda da Figura 1 e a §2.4 afirmam que cada canvas tem seu
seletor. O screenshot atual mostra um só, com o AFTER como rótulo
estático e datas em `2021-06` em vez do `YYYYMM` que a §2.2 documenta.
É a primeira figura do artigo contradizendo a novidade dele, e o mesmo
arquivo alimenta o capítulo da tese pelo `import_amazon.py`.

## Ainda em aberto, se sobrar tempo

- `2026-08-11-pedido-cliques-vs-pixels.md`: o que são os 142 de
  diferença entre 143.634 e 143.492
- `2026-08-10-pedido-figura-unica.md`: fundir as duas figuras de tiles
  numa só, com a coluna de cliques e vermelho translúcido
