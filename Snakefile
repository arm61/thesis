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
         REP + CHAP + 'reflectometry1.tex', REP + CHAP + 'reflectometry2.tex',
         REP + CHAP + 'smallangle.tex', REP + CHAP + 'gisas.tex',
         REP + CHAP + 'teaching.tex', REP + CHAP + 'conclusions.tex',
         REP + CHAP + THEO + 'scattheory.tex',
         REP + CHAP + THEO + 'probing.tex',
         REP + CHAP + THEO + 'classical.tex',
         REP + CHAP + THEO + 'simulation.tex']

SCRIPTS = ['visualisation/theory.py']

rule all:
    input:
        'reports/main.pdf'

rule latexclean:
    shell:
        """
        rm -f reports/main.aux
        rm -f reports/main.bbl
        rm -f reports/main.blg
        rm -f reports/main.fdb_latexmk
        rm -f reports/main.fls
        rm -f reports/main.lof
        rm -f reports/main.log
        rm -f reports/main.lol
        rm -f reports/main.lot
        rm -f reports/main.out
        rm -f reports/main.pdf
        rm -f reports/main.toc
        rm -f reports/rsc-main.bib
        rm -f reports/chapters/conclusions.aux
        rm -f reports/chapters/gisas.aux
        rm -f reports/chapters/introduction.aux
        rm -f reports/chapters/reflectometry1.aux
        rm -f reports/chapters/reflectometry2.aux
        rm -f reports/chapters/smallangle.aux
        rm -f reports/chapters/teaching.aux
        rm -f reports/chapters/theory.aux
        """

rule clean:
    run:
        for i in FIGURES_PLOT:
            shell("rm -f {i}")
        shell("rm -f reports/main.aux")
        shell("rm -f reports/main.bbl")
        shell("rm -f reports/main.blg")
        shell("rm -f reports/main.fdb_latexmk")
        shell("rm -f reports/main.fls")
        shell("rm -f reports/main.lof")
        shell("rm -f reports/main.log")
        shell("rm -f reports/main.lol")
        shell("rm -f reports/main.lot")
        shell("rm -f reports/main.out")
        shell("rm -f reports/main.pdf")
        shell("rm -f reports/main.toc")
        shell("rm -f reports/rsc-main.bib")
        shell("rm -f reports/chapters/conclusions.aux")
        shell("rm -f reports/chapters/gisas.aux")
        shell("rm -f reports/chapters/introduction.aux")
        shell("rm -f reports/chapters/reflectometry1.aux")
        shell("rm -f reports/chapters/reflectometry2.aux")
        shell("rm -f reports/chapters/smallangle.aux")
        shell("rm -f reports/chapters/teaching.aux")
        shell("rm -f reports/chapters/theory.aux")
        shell("rm -f visualisation/theory.py")

rule make_thesis:
    input:
        'reports/MastersDoctoralThesis.cls',
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
        'visualisation/theory.py',
        'data/theory/Experimental-sphere.txt'
    output:
        FIGURES_PLOT
    shell:
        """
        python visualisation/theory.py
        """

rule make_figures_script:
    input:
        'notebooks/theory.ipynb'
    output:
        'visualisation/theory.py'
    shell:
        """
        jupyter-nbconvert --to script --output-dir=visualisation/ notebooks/theory.ipynb
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
