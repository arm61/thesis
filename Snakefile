REP = 'reports/'
CHAP = 'chapters/'
THEO = 'theory/'
APP = 'appendices/'
FIG_DIR = REP + 'figures/'
FIG_THEO = FIG_DIR + 'theory/'
FIGURES_PLOT = [FIG_THEO + 'dyna.pdf', FIG_THEO + 'kine.pdf',
                FIG_THEO + 'scales.pdf', FIG_THEO + 'rg.pdf',
                FIG_THEO + 'sphere.pdf']
FIGURES = [FIG_DIR + 'bath.pdf', FIG_DIR + 'diamond.pdf',
           FIG_THEO+ '2ddect.png', FIG_THEO + 'convar.pdf',
           FIG_THEO + 'd22.pdf', FIG_THEO + 'gisas.png',
           FIG_THEO + 'length.png', FIG_THEO + 'multiatom.pdf',
           FIG_THEO + 'reflectgeo.png', FIG_THEO + 'reflrefr.pdf',
           FIG_THEO + 'scat.pdf', FIG_THEO + 'scatlen.png',
           FIG_THEO + 'scatvec.pdf', FIG_THEO + 'singleatom.pdf',
           FIG_THEO + 'syn.png', FIG_THEO + 'undulator.png',
           FIG_THEO + 'dwba.png']
LATEX = [REP + 'main.tex', REP + 'main.bib',
         REP + CHAP + 'introduction.tex', REP + CHAP + 'theory.tex',
         REP + CHAP + 'reflectometry.tex', REP + CHAP + 'smallangle.tex',
         REP + CHAP + 'gisas.tex', REP + CHAP + 'teaching.tex',
         REP + CHAP + 'conclusions.tex', REP + CHAP + THEO + 'scattheory.tex',
         REP + CHAP + THEO + 'probing.tex',
         REP + CHAP + THEO + 'classical.tex',
         REP + CHAP + THEO + 'simulation.tex']

SCRIPTS = ['visualisation/figures.py']

rule all:
    input:
        'reports/main.pdf'

rule latexclean:
    shell:
        """
        rm reports/main.aux
        rm reports/main.bbl
        rm reports/main.blg
        rm reports/main.lof
        rm reports/main.log
        rm reports/main.lol
        rm reports/main.lot
        rm reports/main.pdf
        rm reports/main.toc
        rm reports/rsc-main.bib
        rm reports/chapters/conclusions.aux
        rm reports/chapters/gisas.aux
        rm reports/chapters/introduction.aux
        rm reports/chapters/reflectometry.aux
        rm reports/chapters/smallangle.aux
        rm reports/chapters/teaching.aux
        rm reports/chapters/theory.aux
        rm reports/appendices/license.aux
        """

rule make_thesis:
    input:
        LATEX,
        FIGURES,
        FIGURES_PLOT,
        'config/requirements.out'
    output:
        'reports/main.pdf'
    shell:
        """
        cd reports
        pdflatex main.tex
        bibtex main.aux
        pdflatex main.tex
        pdflatex main.tex
        """

rule make_figues:
    input:
        'visualisation/figures.py',
        'data/theory/Experimental-sphere.txt'
    output:
        FIGURES_PLOT
    shell:
        """
        python visualisation/figures.py
        """

rule make_figures_script:
    input:
        'notebooks/figures.ipynb'
    output:
        'visualisation/figures.py'
    shell:
        """
        jupyter-nbconvert --to script --output-dir=visualisation/ notebooks/figures.ipynb
        """

rule install_packages:
    input:
        'config/requirements.txt'
    output:
        'config/requirements.out'
    shell:
        """
        conda install --yes --file config/requirements.txt > config/requirements.out
        """
