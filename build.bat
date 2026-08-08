@echo off
rem Compila o paper completo (pdflatex + bibtex + 2x pdflatex) em build\
cd /d "%~dp0"
if not exist build mkdir build
pdflatex -interaction=nonstopmode -output-directory=build main.tex
bibtex build\main
pdflatex -interaction=nonstopmode -output-directory=build main.tex
pdflatex -interaction=nonstopmode -output-directory=build main.tex
echo.
echo PDF: build\main.pdf
findstr /b "!" build\main.log && echo *** ERROS ACIMA *** || echo Sem erros.
