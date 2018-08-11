all: reports/main.pdf

cleantex:
	cd reports && rm main.aux main.bbl main.blg main.dvi main.loa main.lof main.log main.lot main.pdf main.toc

reports/main.pdf: reports/main.tex reports/main.bib reports/chapters/*.tex reports/chapters/*/*.tex reports/figures/*/* reports/MastersDoctoralThesis.cls
	cd reports && pdflatex main.tex 
	cd reports && bibtex main.aux
	cd reports && pdflatex main.tex
	cd reports && pdflatex main.tex

reports/figures/theory/kine.png: notebooks/figures.py
	ipython notebooks/figures.py

notebooks/figures.py: notebooks/figures.ipynb
	jupyter-nbconvert notebooks/figures.ipynb --to script --output_dir=notebooks
