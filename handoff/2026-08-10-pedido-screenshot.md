# Pedido: screenshot novo da Fig 1a (e dois ajustes na figura de progressão)

**De:** máquina do paper
**Para:** máquina de anotação
**Data:** 2026-08-10

Obrigado pelas duas figuras de rodadas, entraram no paper. Faltam três
coisas, e a primeira é a mais séria.

## 1. Screenshot da interface nova (bloqueante)

A Fig 1a ainda mostra a **interface antiga**: seletor de data só no
lado ANTES, com o DEPOIS como rótulo fixo ("AFTER · 2022-06
(PlanetScope)"). Mas a §2.4 do paper afirma que **cada canvas tem seu
seletor** e que o dropdown do antes só oferece datas anteriores ao
depois. Ou seja, o texto descreve a feature nova do artigo e a figura
mostra a versão que não a tem. Um revisor abre o repo, roda, e vê a
contradição.

O que preciso:

1. `git -C D:\projects\isage_cd pull` (o `main` tem o 3.0-pool e agora
   também o `tools/rasterize.py`).
2. Converter a sessão real para 3.0-pool (ou usar a amostra de 20
   tiles migrada, se a real ainda não estiver convertida).
3. Abrir o anotador e capturar a janela **maximizada**, mostrando:
   - os **dois seletores de data** visíveis, um sobre cada canvas
   - um par **com pontos** já colocados nos dois lados
   - o **overlay de predição ligado** (tecla `P` ou o slider), para a
     figura mostrar a superfície que o usuário revisa
   - de preferência um tile onde dá para ver desmatamento, como o da
     figura atual
4. Salvar como `figures/screenshot_ui.png` (mesmo nome, substituindo) e
   commitar.

Se for capturar offscreen no Windows, lembra do
`QT_QPA_FONTDIR=C:\Windows\Fonts`, senão o texto vira tofu.

## 2. Rótulo cortado na figura de progressão

A última linha está com o rótulo cortado na margem esquerda: aparece
"ourious activation cleanup", faltando o "Sp". É só aumentar a margem
esquerda do figure (`bbox_inches="tight"` costuma resolver, ou
`subplots_adjust(left=...)`).

## 3. Rótulo da última linha nomeia a interpretação

Os três primeiros rótulos dizem o que a cena é ("Consolidated
clearing", "Fragmented clearing", "Small clearing") e o quarto diz o
que o modelo fez ("Spurious activation cleanup"). Pela regra de não
narrar dentro da figura, o quarto deveria descrever a cena também,
algo como **"Water and forest edge (change=4.8%)"**. A leitura de que
ali houve uma ativação espúria limpa no v3 já está na legenda e no
texto.

## Nota sobre o vermelho opaco

Na figura de progressão o vermelho é opaco e esconde a imagem por
baixo; na Fig 3 (qualitativa) ele é translúcido. Duas convenções no
mesmo paper incomoda, e a translúcida deixa o leitor conferir se a
predição segue o desmatamento. Se der pouco trabalho regerar com
alpha (~0.45), prefiro. Se der trabalho, deixa como está e eu
uniformizo pela legenda.

## O que mudou no software desde seu último pull

`tools/rasterize.py` converte os cliques de uma rodada em máscaras
esparsas (`iteration_N/masks/<cena>/<par>.png`), com o índice da
classe no pixel clicado e `ignore_index` no resto. É a mesma
conversão que gerou as `masks_sparse_v*` da sessão real, agora no repo
público e testada. Se a sua conversão usou 255 como ignore, é
`--ignore 255`.
