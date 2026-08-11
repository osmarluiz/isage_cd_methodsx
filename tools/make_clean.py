#!/usr/bin/env python3
"""Gera uma copia do manuscrito sem comentarios, para enviar a terceiros.

    python tools/make_clean.py

Saida em entrega/: main.tex, sections/, references.bib e so as figuras
que o texto usa. Os arquivos de trabalho nao sao tocados.

Cuidados que este script toma e que um sed ingenuo nao toma:

  * `\\%` e porcentagem literal, nao inicio de comentario;
  * dentro de verbatim/Verbatim/lstlisting o `%` e' texto;
  * um `%` no FIM da linha, sem nada depois, existe para colar a linha
    seguinte (supressao de espaco). Tirar isso muda o espacamento, entao
    a linha vira apenas `%`, sem o texto do comentario.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "entrega"
VERB_ON = re.compile(r"\\begin\{(verbatim|Verbatim|lstlisting)\}")
VERB_OFF = re.compile(r"\\end\{(verbatim|Verbatim|lstlisting)\}")


def split_comment(line: str) -> tuple[str, bool]:
    """Devolve (codigo, tinha_comentario). Respeita \\%."""
    i = 0
    while i < len(line):
        if line[i] == "\\":
            i += 2
            continue
        if line[i] == "%":
            return line[:i], True
        i += 1
    return line, False


def strip(text: str) -> str:
    out, in_verb = [], False
    for line in text.split("\n"):
        if VERB_ON.search(line):
            in_verb = True
        if in_verb:
            out.append(line)
            if VERB_OFF.search(line):
                in_verb = False
            continue
        code, had = split_comment(line)
        if not had:
            out.append(line)
        elif code.strip() == "":
            continue                      # linha inteira de comentario: some
        else:
            out.append(code + "%")        # mantem a colagem de linha
    return "\n".join(out)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "sections").mkdir(parents=True)
    (OUT / "figures").mkdir()

    texts = {}
    for src in [ROOT / "main.tex", *sorted((ROOT / "sections").glob("*.tex"))]:
        rel = src.relative_to(ROOT)
        cleaned = strip(src.read_text(encoding="utf-8"))
        (OUT / rel).write_text(cleaned, encoding="utf-8")
        texts[str(rel)] = cleaned
    shutil.copy(ROOT / "references.bib", OUT / "references.bib")

    def referidas(txt: str) -> set[str]:
        got = set(re.findall(
            r"\\includegraphics(?:\[[^\]]*\])?\{(?:figures/)?([^}]*)\}", txt))
        got |= {m + ".tex" for m in re.findall(r"\\input\{figures/([^}]*)\}", txt)}
        return got

    # uma figura .tex pode incluir outra imagem, entao repete ate' fechar
    wanted, feito = referidas(" ".join(texts.values())), set()
    while wanted - feito:
        name = sorted(wanted - feito)[0]
        feito.add(name)
        src = ROOT / "figures" / name
        if not src.exists():
            print(f"  AUSENTE: {name}")
            continue
        shutil.copy(src, OUT / "figures" / name)
        print(f"  figura: {name}")
        if name.endswith(".tex"):         # a figura TikZ tambem perde comentarios
            p = OUT / "figures" / name
            limpo = strip(p.read_text(encoding="utf-8"))
            p.write_text(limpo, encoding="utf-8")
            wanted |= referidas(limpo)

    n_tex = len(texts) + 1
    print(f"\nOK: {n_tex} fontes sem comentarios em {OUT}")


if __name__ == "__main__":
    main()
