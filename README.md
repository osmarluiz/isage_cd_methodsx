# iSAGE-CD MethodsX article

Manuscript for MethodsX (Elsevier) describing **iSAGE-CD**, the bi-temporal
change-detection extension of the [iSAGE](https://github.com/osmarluiz/iSAGE)
sparse point supervision framework
([arXiv:2606.10136](https://arxiv.org/abs/2606.10136)).

Companion tool repository: [osmarluiz/isage_cd](https://github.com/osmarluiz/isage_cd).

## Layout

```
main.tex              top-level document (elsarticle)
sections/             one file per section, included from main.tex
  03_background.tex   Background (max 500 words)
  04_method_details.tex
  05_method_validation.tex
  06_limitations.tex
  ...
figures/              PDF/PNG figures
references.bib        BibTeX
```

## Build

```
latexmk -pdf main.tex
```

## Status

- [x] Repo scaffolded
- [x] Background draft (~500 words)
- [ ] Highlights + Specifications table
- [ ] Method Details (session format, UI, iteration workflow)
- [ ] Method Validation (Amazon PRODES 2022 case, convergence curve)
- [ ] Limitations + Ethics
- [ ] Figures (graphical abstract, UI, convergence, qualitative panels)
- [ ] Submission
