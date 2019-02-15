REP = 'reports/'
CHAP = 'chapters/'
THEO = 'theory/'
REFL1 = 'reflectometry1/'
REFL2 = 'reflectometry2/'
APP = 'appendices/'
FIG_DIR = REP + 'figures/'
FIG_THEO = FIG_DIR + 'theory/'
FIG_REFL1 = FIG_DIR + 'reflectometry1/'
FIG_REFL2 = FIG_DIR + 'reflectometry2/'
FIGURES_PLOT = [FIG_THEO + 'dyna.pdf', FIG_THEO + 'kine.pdf',
                FIG_THEO + 'scales.pdf', FIG_THEO + 'rg.pdf',
                FIG_THEO + 'sphere.pdf', FIG_THEO + 'grad.pdf',
                FIG_THEO + 'diff_evo.pdf', FIG_THEO + 'part_swarm.pdf',
                FIG_THEO + 'mcmc.pdf']
FIGURES = [FIG_DIR + 'bath.pdf', FIG_DIR + 'diamond.pdf',
           FIG_THEO+ '2ddect.png', FIG_THEO + 'convar.pdf',
           FIG_THEO + 'd22.pdf', FIG_THEO + 'gisas.png',
           FIG_THEO + 'length.png', FIG_THEO + 'multiatom.pdf',
           FIG_THEO + 'reflectgeo.png', FIG_THEO + 'reflrefr.pdf',
           FIG_THEO + 'scat.pdf', FIG_THEO + 'scatlen.png',
           FIG_THEO + 'scatvec.pdf', FIG_THEO + 'singleatom.pdf',
           FIG_THEO + 'syn.png', FIG_THEO + 'undulator.png',
           FIG_THEO + 'dwba.png', FIG_REFL1 + 'head_groups.png',
           FIG_REFL1 + 'gixd.png',
           FIG_REFL1 + 'dppc_xray_sp_15_pdf.pdf',
           FIG_REFL1 + 'dppc_xray_sp_20_pdf.pdf',
           FIG_REFL1 + 'dppc_xray_sp_25_pdf.pdf',
           FIG_REFL1 + 'dppc_xray_sp_30_pdf.pdf',
           FIG_REFL1 + 'dppc_xray_ref_sld.pdf',
           FIG_REFL1 + 'dppc_xray_dt_phi.pdf',
           FIG_REFL1 + 'dmpc_xray_sp_20_pdf.pdf',
           FIG_REFL1 + 'dmpc_xray_sp_25_pdf.pdf',
           FIG_REFL1 + 'dmpc_xray_sp_30_pdf.pdf',
           FIG_REFL1 + 'dmpc_xray_sp_40_pdf.pdf',
           FIG_REFL1 + 'dmpc_xray_ref_sld.pdf',
           FIG_REFL1 + 'dmpc_xray_dt_phi.pdf',
           FIG_REFL1 + 'dlpc_xray_sp_20_pdf.pdf',
           FIG_REFL1 + 'dlpc_xray_sp_25_pdf.pdf',
           FIG_REFL1 + 'dlpc_xray_sp_30_pdf.pdf',
           FIG_REFL1 + 'dlpc_xray_sp_35_pdf.pdf',
           FIG_REFL1 + 'dlpc_xray_ref_sld.pdf',
           FIG_REFL1 + 'dlpc_xray_dt_phi.pdf',
           FIG_REFL1 + 'dmpg_xray_sp_15_pdf.pdf',
           FIG_REFL1 + 'dmpg_xray_sp_20_pdf.pdf',
           FIG_REFL1 + 'dmpg_xray_sp_25_pdf.pdf',
           FIG_REFL1 + 'dmpg_xray_sp_30_pdf.pdf',
           FIG_REFL1 + 'dmpg_xray_ref_sld.pdf',
           FIG_REFL1 + 'dmpg_xray_dt_phi.pdf',
           FIG_REFL1 + 'dppc_neutron_15_pdf.pdf',
           FIG_REFL1 + 'dppc_neutron_15_ref_sld.pdf',
           FIG_REFL1 + 'dppc_neutron_20_pdf.pdf',
           FIG_REFL1 + 'dppc_neutron_20_ref_sld.pdf',
           FIG_REFL1 + 'dmpc_neutron_20_pdf.pdf',
           FIG_REFL1 + 'dmpc_neutron_20_ref_sld.pdf',
           FIG_REFL1 + 'dmpc_neutron_25_pdf.pdf',
           FIG_REFL1 + 'dmpc_neutron_25_ref_sld.pdf',
           FIG_REFL2 + 'apm.pdf',
           FIG_REFL2 + 'dspc_20_pdf.pdf',
           FIG_REFL2 + 'dspc_20_ref_sld.pdf',
           FIG_REFL2 + 'dspc_30_pdf.pdf',
           FIG_REFL2 + 'dspc_30_ref_sld.pdf',
           FIG_REFL2 + 'dspc_40_pdf.pdf',
           FIG_REFL2 + 'dspc_40_ref_sld.pdf',
           FIG_REFL2 + 'dspc_50_pdf.pdf',
           FIG_REFL2 + 'dspc_50_ref_sld.pdf',
           FIG_REFL2 + 'dspc_martini_20_ref_sld.pdf',
           FIG_REFL2 + 'dspc_martini_30_ref_sld.pdf',
           FIG_REFL2 + 'dspc_martini_40_ref_sld.pdf',
           FIG_REFL2 + 'dspc_martini_50_ref_sld.pdf',
           FIG_REFL2 + 'dspc_berger_20_ref_sld.pdf',
           FIG_REFL2 + 'dspc_berger_30_ref_sld.pdf',
           FIG_REFL2 + 'dspc_berger_40_ref_sld.pdf',
           FIG_REFL2 + 'dspc_berger_50_ref_sld.pdf',
           FIG_REFL2 + 'dspc_slipids_20_ref_sld.pdf',
           FIG_REFL2 + 'dspc_slipids_30_ref_sld.pdf',
           FIG_REFL2 + 'dspc_slipids_40_ref_sld.pdf',
           FIG_REFL2 + 'dspc_slipids_50_ref_sld.pdf']
#CHAPTERS = [REP + CHAP + 'introduction.tex', REP + CHAP + 'theory.tex',
#            REP + CHAP + 'reflectometry1.tex', REP + CHAP + 'reflectometry2.tex',
#            REP + CHAP + 'smallangle.tex', REP + CHAP + 'gisas.tex',
#            REP + CHAP + 'teaching.tex', REP + CHAP + 'summary.tex']
CHAPTERS = [REP + CHAP + 'theory.tex', REP + CHAP + 'reflectometry1.tex',
            REP + CHAP + 'reflectometry2.tex']
LATEX = [REP + CHAP + THEO + 'scattheory.tex',
         REP + CHAP + THEO + 'probing.tex',
         REP + CHAP + THEO + 'classical.tex',
         REP + CHAP + THEO + 'simulation.tex',
         REP + CHAP + REFL1 + 'abstract.tex',
         REP + CHAP + REFL1 + 'context.tex',
         REP + CHAP + REFL1 + 'intro.tex',
         REP + CHAP + REFL1 + 'methods.tex',
         REP + CHAP + REFL1 + 'analysis.tex',
         REP + CHAP + REFL1 + 'discussion.tex',
         REP + CHAP + REFL1 + 'conclusions.tex',
         REP + CHAP + REFL2 + 'abstract.tex',
         REP + CHAP + REFL2 + 'context.tex',
         REP + CHAP + REFL2 + 'intro.tex',
         REP + CHAP + REFL2 + 'methods.tex',
         REP + CHAP + REFL2 + 'analysis.tex',
         REP + CHAP + REFL2 + 'discussion.tex',
         REP + CHAP + REFL2 + 'conclusions.tex',
         REP + 'appendices/papers.tex']
CODE_BLOCKS = [REP + 'code_blocks/' + 'reflectometry.py',
               REP + 'code_blocks/' + 'lennardjones.py',
               REP + 'code_blocks/' + 'diff_evo.py',
               REP + 'code_blocks/' + 'selection.py',
               REP + 'code_blocks/' + 'mutation.py',
               REP + 'code_blocks/' + 'part_swarm.py',
               REP + 'code_blocks/' + 'recombination.py',
               REP + 'code_blocks/' + 'grad.py',
               REP + 'code_blocks/' + 'mol_vol.py']

SCRIPTS = ['visualisation/theory.py', 'visualisation/XRR_plotting.py',
           'tools/chemically_consistent.py']

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

rule thesis:
    input:
        'reports/MastersDoctoralThesis.cls',
        LATEX,
        REP + 'main.tex',
        REP + 'main.bib',
        CHAPTERS,
        FIGURES,
        FIGURES_PLOT,
        CODE_BLOCKS
    output:
        'reports/main.pdf'
    run:
        shell("black -l 70 reports/code_blocks/*.py")
        shell("pdflatex -output-directory=reports/ reports/main.tex")
        for i in CHAPTERS:
            j = i[:-3] + 'aux'
            shell("bibtex {}".format(j))
        shell("pdflatex -output-directory=reports/ reports/main.tex")
        shell("pdflatex -output-directory=reports/ reports/main.tex")

rule theory_figues:
    input:
        'visualisation/theory.py',
        'data/theory/Experimental-sphere.txt',
        CODE_BLOCKS
    output:
        FIGURES_PLOT
    shell:
        """
        cd visualisation && python theory.py
        """

rule dppc_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_15.dat',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_20.dat',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_25.dat',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_30.dat'
    output:
        'output/reflectometry1/dppc_xray/dppc_xray_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dppc 15 15 20 25 30 0
        """

rule dmpc_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_20.dat',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_25.dat',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_30.dat',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_40.dat'
    output:
        'output/reflectometry1/dmpc_xray/dmpc_xray_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dmpc 13 20 25 30 40 0
        """

rule dlpc_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_20.dat',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_25.dat',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_30.dat',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_35.dat'
    output:
        'output/reflectometry1/dlpc_xray/dlpc_xray_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dlpc 11 20 25 30 35 0
        """

rule dmpg_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_15.dat',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_20.dat',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_25.dat',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_30.dat'
    output:
        'output/reflectometry1/dmpg_xray/dmpg_xray_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dmpg 13 15 20 25 30 0
        """

rule dppc_xray_plotting:
    input:
        'visualisation/XRR_plotting.py',
        'output/reflectometry1/dppc_xray/dppc_xray_chain.txt'
    output:
        FIG_REFL1 + 'dppc_xray_sp_15_pdf.pdf',
        FIG_REFL1 + 'dppc_xray_sp_20_pdf.pdf',
        FIG_REFL1 + 'dppc_xray_sp_25_pdf.pdf',
        FIG_REFL1 + 'dppc_xray_sp_30_pdf.pdf',
        FIG_REFL1 + 'dppc_xray_ref_sld.pdf',
        FIG_REFL1 + 'dppc_xray_dt_phi.pdf',
        'output/reflectometry1/dppc_xray/dppc_xray-d_h.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_t.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_h.tex'
    shell:
        """
        cd visualisation && python XRR_plotting.py dppc 15 15 20 25 30 0
        """
rule dmpc_xray_plotting:
    input:
        'visualisation/XRR_plotting.py',
        'output/reflectometry1/dmpc_xray/dmpc_xray_chain.txt'
    output:
        FIG_REFL1 + 'dmpc_xray_sp_20_pdf.pdf',
        FIG_REFL1 + 'dmpc_xray_sp_25_pdf.pdf',
        FIG_REFL1 + 'dmpc_xray_sp_30_pdf.pdf',
        FIG_REFL1 + 'dmpc_xray_sp_40_pdf.pdf',
        FIG_REFL1 + 'dmpc_xray_ref_sld.pdf',
        FIG_REFL1 + 'dmpc_xray_dt_phi.pdf',
        'output/reflectometry1/dmpc_xray/dmpc_xray-d_h.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_t.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_h.tex'
    shell:
        """
        cd visualisation && python XRR_plotting.py dmpc 13 20 25 30 40 0
        """

rule dlpc_xray_plotting:
    input:
        'visualisation/XRR_plotting.py',
        'output/reflectometry1/dlpc_xray/dlpc_xray_chain.txt'
    output:
        FIG_REFL1 + 'dlpc_xray_sp_20_pdf.pdf',
        FIG_REFL1 + 'dlpc_xray_sp_25_pdf.pdf',
        FIG_REFL1 + 'dlpc_xray_sp_30_pdf.pdf',
        FIG_REFL1 + 'dlpc_xray_sp_35_pdf.pdf',
        FIG_REFL1 + 'dlpc_xray_ref_sld.pdf',
        FIG_REFL1 + 'dlpc_xray_dt_phi.pdf',
        'output/reflectometry1/dlpc_xray/dlpc_xray-d_h.tex',
        'output/reflectometry1/dlpc_xray/dlpc_xray-V_t.tex',
        'output/reflectometry1/dlpc_xray/dlpc_xray-V_h.tex'
    shell:
        """
        cd visualisation && python XRR_plotting.py dlpc 11 20 25 30 35 0
        """

rule dmpg_xray_plotting:
    input:
        'visualisation/XRR_plotting.py',
        'output/reflectometry1/dmpg_xray/dmpg_xray_chain.txt'
    output:
        FIG_REFL1 + 'dmpg_xray_sp_15_pdf.pdf',
        FIG_REFL1 + 'dmpg_xray_sp_20_pdf.pdf',
        FIG_REFL1 + 'dmpg_xray_sp_25_pdf.pdf',
        FIG_REFL1 + 'dmpg_xray_sp_30_pdf.pdf',
        FIG_REFL1 + 'dmpg_xray_ref_sld.pdf',
        FIG_REFL1 + 'dmpg_xray_dt_phi.pdf',
        'output/reflectometry1/dmpg_xray/dmpg_xray-d_h.tex',
        'output/reflectometry1/dmpg_xray/dmpg_xray-V_t.tex',
        'output/reflectometry1/dmpg_xray/dmpg_xray-V_h.tex'
    shell:
        """
        cd visualisation && python XRR_plotting.py dmpg 13 15 20 25 30 0
        """

rule dppc_neutron_15_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dppc_neutron/dppc_neutron_h_sp_15.dat',
        'data/reflectometry1/dppc_neutron/dppc_neutron_hd_sp_15.dat',
        'output/reflectometry1/dppc_xray/dppc_xray-d_h.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_t.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_h.tex'
    output:
        'output/reflectometry1/dppc_neutron/dppc_neutron_15_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dppc 15 15 h hd 30 1
        """

rule dppc_neutron_20_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dppc_neutron/dppc_neutron_h_sp_20.dat',
        'data/reflectometry1/dppc_neutron/dppc_neutron_hd_sp_20.dat',
        'output/reflectometry1/dppc_xray/dppc_xray-d_h.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_t.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_h.tex'
    output:
        'output/reflectometry1/dppc_neutron/dppc_neutron_20_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dppc 15 20 h hd 30 1
        """

rule dmpc_neutron_20_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_h_sp_20.dat',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_hd_sp_20.dat',
        'output/reflectometry1/dmpc_xray/dmpc_xray-d_h.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_t.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_h.tex'
    output:
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_20_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dmpc 13 20 h hd 30 1
        """

rule dmpc_neutron_25_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_h_sp_25.dat',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_hd_sp_25.dat',
        'output/reflectometry1/dmpc_xray/dmpc_xray-d_h.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_t.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_h.tex'
    output:
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_25_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dmpc 13 25 h hd 30 1
        """

rule dspc_neutron_20_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry2/dspc_20/d13acmw20.dat',
        'data/reflectometry2/dspc_20/d13d2o20.dat',
        'data/reflectometry2/dspc_20/d70acmw20.dat',
        'data/reflectometry2/dspc_20/d70d2o20.dat',
        'data/reflectometry2/dspc_20/d83acmw20.dat',
        'data/reflectometry2/dspc_20/d83d2o20.dat',
        'data/reflectometry2/dspc_20/hd2o20.dat'
    output:
        'output/reflectometry2/dspc_20/dspc_20_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dspc 17 20 47.9 2 3 1
        """

rule dspc_neutron_30_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry2/dspc_30/d13acmw30.dat',
        'data/reflectometry2/dspc_30/d13d2o30.dat',
        'data/reflectometry2/dspc_30/d70acmw30.dat',
        'data/reflectometry2/dspc_30/d70d2o30.dat',
        'data/reflectometry2/dspc_30/d83acmw30.dat',
        'data/reflectometry2/dspc_30/d83d2o30.dat',
        'data/reflectometry2/dspc_30/hd2o30.dat'
    output:
        'output/reflectometry2/dspc_30/dspc_30_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dspc 17 30 46.4 2 3 1
        """

rule dspc_neutron_40_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry2/dspc_40/d13acmw40.dat',
        'data/reflectometry2/dspc_40/d13d2o40.dat',
        'data/reflectometry2/dspc_40/d70acmw40.dat',
        'data/reflectometry2/dspc_40/d70d2o40.dat',
        'data/reflectometry2/dspc_40/d83acmw40.dat',
        'data/reflectometry2/dspc_40/d83d2o40.dat',
        'data/reflectometry2/dspc_40/hd2o40.dat'
    output:
        'output/reflectometry2/dspc_40/dspc_40_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dspc 17 40 45.0 2 3 1
        """

rule dspc_neutron_50_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'tools/chemically_consistent.py',
        'data/reflectometry2/dspc_50/d13acmw50.dat',
        'data/reflectometry2/dspc_50/d13d2o50.dat',
        'data/reflectometry2/dspc_50/d70acmw50.dat',
        'data/reflectometry2/dspc_50/d70d2o50.dat',
        'data/reflectometry2/dspc_50/d83acmw50.dat',
        'data/reflectometry2/dspc_50/d83d2o50.dat',
        'data/reflectometry2/dspc_50/hd2o50.dat'
    output:
        'output/reflectometry2/dspc_50/dspc_50_chain.txt'
    shell:
        """
        cd tools && python chemically_consistent.py dspc 17 50 44.6 2 3 1
        """

rule dspc_neutron_20_plotting:
    input:
        'visualisation/NR_plotting2.py',
        'output/reflectometry2/dspc_20/dspc_20_chain.txt'
    output:
        FIG_REFL2 + 'dspc_20_pdf.pdf',
        FIG_REFL2 + 'dspc_20_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting2.py dspc 17 20 47.9
        """

rule dspc_neutron_30_plotting:
    input:
        'visualisation/NR_plotting2.py',
        'output/reflectometry2/dspc_30/dspc_30_chain.txt'
    output:
        FIG_REFL2 + 'dspc_30_pdf.pdf',
        FIG_REFL2 + 'dspc_30_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting2.py dspc 17 30 46.4
        """

rule dspc_neutron_40_plotting:
    input:
        'visualisation/NR_plotting2.py',
        'output/reflectometry2/dspc_40/dspc_40_chain.txt'
    output:
        FIG_REFL2 + 'dspc_40_pdf.pdf',
        FIG_REFL2 + 'dspc_40_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting2.py dspc 17 40 45.0
        """

rule dspc_neutron_50_plotting:
    input:
        'visualisation/NR_plotting.py2',
        'output/reflectometry2/dspc_50/dspc_50_chain.txt'
    output:
        FIG_REFL2 + 'dspc_50_pdf.pdf',
        FIG_REFL2 + 'dspc_50_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting2.py dspc 17 50 44.6
        """

rule dppc_neutron_15_plotting:
    input:
        'visualisation/NR_plotting.py',
        'output/reflectometry1/dppc_neutron/dppc_neutron_15_chain.txt'
    output:
        FIG_REFL1 + 'dppc_neutron_15_pdf.pdf',
        FIG_REFL1 + 'dppc_neutron_15_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting.py dppc 15 15 h hd 30 1
        """

rule dppc_neutron_20_plotting:
    input:
        'visualisation/NR_plotting.py',
        'output/reflectometry1/dppc_neutron/dppc_neutron_20_chain.txt'
    output:
        FIG_REFL1 + 'dppc_neutron_20_pdf.pdf',
        FIG_REFL1 + 'dppc_neutron_20_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting.py dppc 15 20 h hd 30 1
        """

rule dmpc_neutron_20_plotting:
    input:
        'visualisation/NR_plotting.py',
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_20_chain.txt'
    output:
        FIG_REFL1 + 'dmpc_neutron_20_pdf.pdf',
        FIG_REFL1 + 'dmpc_neutron_20_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting.py dmpc 13 20 h hd 30 1
        """

rule dmpc_neutron_25_plotting:
    input:
        'visualisation/NR_plotting.py',
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_25_chain.txt'
    output:
        FIG_REFL1 + 'dmpc_neutron_25_pdf.pdf',
        FIG_REFL1 + 'dmpc_neutron_25_ref_sld.pdf'
    shell:
        """
        cd visualisation && python NR_plotting.py dmpc 13 25 h hd 30 1
        """

rule martini_dspc_20_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_20/martini_frame1.pdb',
        'data/reflectometry2/dspc_20/martini_frame2.pdb',
        'data/reflectometry2/dspc_20/martini_frame3.pdb',
        'data/reflectometry2/dspc_20/martini_frame4.pdb',
        'data/reflectometry2/dspc_20/martini_frame5.pdb',
        'data/reflectometry2/dspc_20/martini_frame6.pdb',
        'data/reflectometry2/dspc_20/martini_frame7.pdb',
        'data/reflectometry2/dspc_20/martini_frame8.pdb',
        'data/reflectometry2/dspc_20/martini_frame9.pdb',
        'data/reflectometry2/dspc_20/martini_frame10.pdb',
        'data/reflectometry2/dspc_20/d13acmw20.dat',
        'data/reflectometry2/dspc_20/d13d2o20.dat',
        'data/reflectometry2/dspc_20/d70acmw20.dat',
        'data/reflectometry2/dspc_20/d70d2o20.dat',
        'data/reflectometry2/dspc_20/d83acmw20.dat',
        'data/reflectometry2/dspc_20/d83d2o20.dat',
        'data/reflectometry2/dspc_20/hd2o20.dat'
    output:
        FIG_REFL2 + 'dspc_martini_20_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py martini 20 4 0.8
        """

rule martini_dspc_30_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_30/martini_frame1.pdb',
        'data/reflectometry2/dspc_30/martini_frame2.pdb',
        'data/reflectometry2/dspc_30/martini_frame3.pdb',
        'data/reflectometry2/dspc_30/martini_frame4.pdb',
        'data/reflectometry2/dspc_30/martini_frame5.pdb',
        'data/reflectometry2/dspc_30/martini_frame6.pdb',
        'data/reflectometry2/dspc_30/martini_frame7.pdb',
        'data/reflectometry2/dspc_30/martini_frame8.pdb',
        'data/reflectometry2/dspc_30/martini_frame9.pdb',
        'data/reflectometry2/dspc_30/martini_frame10.pdb',
        'data/reflectometry2/dspc_30/d13acmw30.dat',
        'data/reflectometry2/dspc_30/d13d2o30.dat',
        'data/reflectometry2/dspc_30/d70acmw30.dat',
        'data/reflectometry2/dspc_30/d70d2o30.dat',
        'data/reflectometry2/dspc_30/d83acmw30.dat',
        'data/reflectometry2/dspc_30/d83d2o30.dat',
        'data/reflectometry2/dspc_30/hd2o30.dat'
    output:
        FIG_REFL2 + 'dspc_martini_30_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py martini 30 4 0.8
        """

rule martini_dspc_40_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_40/martini_frame1.pdb',
        'data/reflectometry2/dspc_40/martini_frame2.pdb',
        'data/reflectometry2/dspc_40/martini_frame3.pdb',
        'data/reflectometry2/dspc_40/martini_frame4.pdb',
        'data/reflectometry2/dspc_40/martini_frame5.pdb',
        'data/reflectometry2/dspc_40/martini_frame6.pdb',
        'data/reflectometry2/dspc_40/martini_frame7.pdb',
        'data/reflectometry2/dspc_40/martini_frame8.pdb',
        'data/reflectometry2/dspc_40/martini_frame9.pdb',
        'data/reflectometry2/dspc_40/martini_frame10.pdb',
        'data/reflectometry2/dspc_40/d13acmw40.dat',
        'data/reflectometry2/dspc_40/d13d2o40.dat',
        'data/reflectometry2/dspc_40/d70acmw40.dat',
        'data/reflectometry2/dspc_40/d70d2o40.dat',
        'data/reflectometry2/dspc_40/d83acmw40.dat',
        'data/reflectometry2/dspc_40/d83d2o40.dat',
        'data/reflectometry2/dspc_40/hd2o40.dat'
    output:
        FIG_REFL2 + 'dspc_martini_40_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py martini 40 4 0.8
        """

rule martini_dspc_50_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_50/martini_frame1.pdb',
        'data/reflectometry2/dspc_50/martini_frame2.pdb',
        'data/reflectometry2/dspc_50/martini_frame3.pdb',
        'data/reflectometry2/dspc_50/martini_frame4.pdb',
        'data/reflectometry2/dspc_50/martini_frame5.pdb',
        'data/reflectometry2/dspc_50/martini_frame6.pdb',
        'data/reflectometry2/dspc_50/martini_frame7.pdb',
        'data/reflectometry2/dspc_50/martini_frame8.pdb',
        'data/reflectometry2/dspc_50/martini_frame9.pdb',
        'data/reflectometry2/dspc_50/martini_frame10.pdb',
        'data/reflectometry2/dspc_50/d13acmw50.dat',
        'data/reflectometry2/dspc_50/d13d2o50.dat',
        'data/reflectometry2/dspc_50/d70acmw50.dat',
        'data/reflectometry2/dspc_50/d70d2o50.dat',
        'data/reflectometry2/dspc_50/d83acmw50.dat',
        'data/reflectometry2/dspc_50/d83d2o50.dat',
        'data/reflectometry2/dspc_50/hd2o50.dat'
    output:
        FIG_REFL2 + 'dspc_martini_50_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py martini 50 4 0.8
        """

rule berger_dspc_20_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_20/berger_frame1.pdb',
        'data/reflectometry2/dspc_20/berger_frame2.pdb',
        'data/reflectometry2/dspc_20/berger_frame3.pdb',
        'data/reflectometry2/dspc_20/berger_frame4.pdb',
        'data/reflectometry2/dspc_20/berger_frame5.pdb',
        'data/reflectometry2/dspc_20/berger_frame6.pdb',
        'data/reflectometry2/dspc_20/berger_frame7.pdb',
        'data/reflectometry2/dspc_20/berger_frame8.pdb',
        'data/reflectometry2/dspc_20/berger_frame9.pdb',
        'data/reflectometry2/dspc_20/berger_frame10.pdb',
        'data/reflectometry2/dspc_20/d13acmw20.dat',
        'data/reflectometry2/dspc_20/d13d2o20.dat',
        'data/reflectometry2/dspc_20/d70acmw20.dat',
        'data/reflectometry2/dspc_20/d70d2o20.dat',
        'data/reflectometry2/dspc_20/d83acmw20.dat',
        'data/reflectometry2/dspc_20/d83d2o20.dat',
        'data/reflectometry2/dspc_20/hd2o20.dat'
    output:
        FIG_REFL2 + 'dspc_berger_20_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py berger 20 1 0
        """

rule berger_dspc_30_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_30/berger_frame1.pdb',
        'data/reflectometry2/dspc_30/berger_frame2.pdb',
        'data/reflectometry2/dspc_30/berger_frame3.pdb',
        'data/reflectometry2/dspc_30/berger_frame4.pdb',
        'data/reflectometry2/dspc_30/berger_frame5.pdb',
        'data/reflectometry2/dspc_30/berger_frame6.pdb',
        'data/reflectometry2/dspc_30/berger_frame7.pdb',
        'data/reflectometry2/dspc_30/berger_frame8.pdb',
        'data/reflectometry2/dspc_30/berger_frame9.pdb',
        'data/reflectometry2/dspc_30/berger_frame10.pdb',
        'data/reflectometry2/dspc_30/d13acmw30.dat',
        'data/reflectometry2/dspc_30/d13d2o30.dat',
        'data/reflectometry2/dspc_30/d70acmw30.dat',
        'data/reflectometry2/dspc_30/d70d2o30.dat',
        'data/reflectometry2/dspc_30/d83acmw30.dat',
        'data/reflectometry2/dspc_30/d83d2o30.dat',
        'data/reflectometry2/dspc_30/hd2o30.dat'
    output:
        FIG_REFL2 + 'dspc_berger_30_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py berger 30 1 0
        """

rule berger_dspc_40_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_40/berger_frame1.pdb',
        'data/reflectometry2/dspc_40/berger_frame2.pdb',
        'data/reflectometry2/dspc_40/berger_frame3.pdb',
        'data/reflectometry2/dspc_40/berger_frame4.pdb',
        'data/reflectometry2/dspc_40/berger_frame5.pdb',
        'data/reflectometry2/dspc_40/berger_frame6.pdb',
        'data/reflectometry2/dspc_40/berger_frame7.pdb',
        'data/reflectometry2/dspc_40/berger_frame8.pdb',
        'data/reflectometry2/dspc_40/berger_frame9.pdb',
        'data/reflectometry2/dspc_40/berger_frame10.pdb',
        'data/reflectometry2/dspc_40/d13acmw40.dat',
        'data/reflectometry2/dspc_40/d13d2o40.dat',
        'data/reflectometry2/dspc_40/d70acmw40.dat',
        'data/reflectometry2/dspc_40/d70d2o40.dat',
        'data/reflectometry2/dspc_40/d83acmw40.dat',
        'data/reflectometry2/dspc_40/d83d2o40.dat',
        'data/reflectometry2/dspc_40/hd2o40.dat'
    output:
        FIG_REFL2 + 'dspc_berger_40_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py berger 40 1 0
        """

rule berger_dspc_50_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_50/berger_frame1.pdb',
        'data/reflectometry2/dspc_50/berger_frame2.pdb',
        'data/reflectometry2/dspc_50/berger_frame3.pdb',
        'data/reflectometry2/dspc_50/berger_frame4.pdb',
        'data/reflectometry2/dspc_50/berger_frame5.pdb',
        'data/reflectometry2/dspc_50/berger_frame6.pdb',
        'data/reflectometry2/dspc_50/berger_frame7.pdb',
        'data/reflectometry2/dspc_50/berger_frame8.pdb',
        'data/reflectometry2/dspc_50/berger_frame9.pdb',
        'data/reflectometry2/dspc_50/berger_frame10.pdb',
        'data/reflectometry2/dspc_50/d13acmw50.dat',
        'data/reflectometry2/dspc_50/d13d2o50.dat',
        'data/reflectometry2/dspc_50/d70acmw50.dat',
        'data/reflectometry2/dspc_50/d70d2o50.dat',
        'data/reflectometry2/dspc_50/d83acmw50.dat',
        'data/reflectometry2/dspc_50/d83d2o50.dat',
        'data/reflectometry2/dspc_50/hd2o50.dat'
    output:
        FIG_REFL2 + 'dspc_berger_50_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py berger 50 1 0
        """

rule slipids_dspc_20_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_20/slipids_frame1.pdb',
        'data/reflectometry2/dspc_20/slipids_frame2.pdb',
        'data/reflectometry2/dspc_20/slipids_frame3.pdb',
        'data/reflectometry2/dspc_20/slipids_frame4.pdb',
        'data/reflectometry2/dspc_20/slipids_frame5.pdb',
        'data/reflectometry2/dspc_20/slipids_frame6.pdb',
        'data/reflectometry2/dspc_20/slipids_frame7.pdb',
        'data/reflectometry2/dspc_20/slipids_frame8.pdb',
        'data/reflectometry2/dspc_20/slipids_frame9.pdb',
        'data/reflectometry2/dspc_20/slipids_frame10.pdb',
        'data/reflectometry2/dspc_20/d13acmw20.dat',
        'data/reflectometry2/dspc_20/d13d2o20.dat',
        'data/reflectometry2/dspc_20/d70acmw20.dat',
        'data/reflectometry2/dspc_20/d70d2o20.dat',
        'data/reflectometry2/dspc_20/d83acmw20.dat',
        'data/reflectometry2/dspc_20/d83d2o20.dat',
        'data/reflectometry2/dspc_20/hd2o20.dat'
    output:
        FIG_REFL2 + 'dspc_slipids_20_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py slipids 20 1 0
        """

rule slipids_dspc_30_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_30/slipids_frame1.pdb',
        'data/reflectometry2/dspc_30/slipids_frame2.pdb',
        'data/reflectometry2/dspc_30/slipids_frame3.pdb',
        'data/reflectometry2/dspc_30/slipids_frame4.pdb',
        'data/reflectometry2/dspc_30/slipids_frame5.pdb',
        'data/reflectometry2/dspc_30/slipids_frame6.pdb',
        'data/reflectometry2/dspc_30/slipids_frame7.pdb',
        'data/reflectometry2/dspc_30/slipids_frame8.pdb',
        'data/reflectometry2/dspc_30/slipids_frame9.pdb',
        'data/reflectometry2/dspc_30/slipids_frame10.pdb',
        'data/reflectometry2/dspc_30/d13acmw30.dat',
        'data/reflectometry2/dspc_30/d13d2o30.dat',
        'data/reflectometry2/dspc_30/d70acmw30.dat',
        'data/reflectometry2/dspc_30/d70d2o30.dat',
        'data/reflectometry2/dspc_30/d83acmw30.dat',
        'data/reflectometry2/dspc_30/d83d2o30.dat',
        'data/reflectometry2/dspc_30/hd2o30.dat'
    output:
        FIG_REFL2 + 'dspc_slipids_30_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py slipids 30 1 0
        """

rule slipids_dspc_40_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_40/slipids_frame1.pdb',
        'data/reflectometry2/dspc_40/slipids_frame2.pdb',
        'data/reflectometry2/dspc_40/slipids_frame3.pdb',
        'data/reflectometry2/dspc_40/slipids_frame4.pdb',
        'data/reflectometry2/dspc_40/slipids_frame5.pdb',
        'data/reflectometry2/dspc_40/slipids_frame6.pdb',
        'data/reflectometry2/dspc_40/slipids_frame7.pdb',
        'data/reflectometry2/dspc_40/slipids_frame8.pdb',
        'data/reflectometry2/dspc_40/slipids_frame9.pdb',
        'data/reflectometry2/dspc_40/slipids_frame10.pdb',
        'data/reflectometry2/dspc_40/d13acmw40.dat',
        'data/reflectometry2/dspc_40/d13d2o40.dat',
        'data/reflectometry2/dspc_40/d70acmw40.dat',
        'data/reflectometry2/dspc_40/d70d2o40.dat',
        'data/reflectometry2/dspc_40/d83acmw40.dat',
        'data/reflectometry2/dspc_40/d83d2o40.dat',
        'data/reflectometry2/dspc_40/hd2o40.dat'
    output:
        FIG_REFL2 + 'dspc_slipids_40_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py slipids 40 1 0
        """

rule slipids_dspc_50_analysis:
    input:
        'tools/sim_analysis.py',
        'data/reflectometry2/dspc_50/slipids_frame1.pdb',
        'data/reflectometry2/dspc_50/slipids_frame2.pdb',
        'data/reflectometry2/dspc_50/slipids_frame3.pdb',
        'data/reflectometry2/dspc_50/slipids_frame4.pdb',
        'data/reflectometry2/dspc_50/slipids_frame5.pdb',
        'data/reflectometry2/dspc_50/slipids_frame6.pdb',
        'data/reflectometry2/dspc_50/slipids_frame7.pdb',
        'data/reflectometry2/dspc_50/slipids_frame8.pdb',
        'data/reflectometry2/dspc_50/slipids_frame9.pdb',
        'data/reflectometry2/dspc_50/slipids_frame10.pdb',
        'data/reflectometry2/dspc_50/d13acmw50.dat',
        'data/reflectometry2/dspc_50/d13d2o50.dat',
        'data/reflectometry2/dspc_50/d70acmw50.dat',
        'data/reflectometry2/dspc_50/d70d2o50.dat',
        'data/reflectometry2/dspc_50/d83acmw50.dat',
        'data/reflectometry2/dspc_50/d83d2o50.dat',
        'data/reflectometry2/dspc_50/hd2o50.dat'
    output:
        FIG_REFL2 + 'dspc_slipids_50_ref_sld.pdf',
    shell:
        """
        cd tools && python sim_analysis.py slipids 50 1 0
        """

rule pear_plotting:
    input:
        'visualisation/pear_plotting.py',
        'output/reflectometry1/dlpc_xray/dlpc_p_sum_sp20.txt',
        'output/reflectometry1/dlpc_xray/dlpc_p_sum_sp25.txt',
        'output/reflectometry1/dlpc_xray/dlpc_p_sum_sp30.txt',
        'output/reflectometry1/dlpc_xray/dlpc_p_sum_sp35.txt',
        'output/reflectometry1/dmpc_xray/dmpc_p_sum_sp20.txt',
        'output/reflectometry1/dmpc_xray/dmpc_p_sum_sp25.txt',
        'output/reflectometry1/dmpc_xray/dmpc_p_sum_sp30.txt',
        'output/reflectometry1/dmpc_xray/dmpc_p_sum_sp40.txt',
        'output/reflectometry1/dppc_xray/dppc_p_sum_sp15.txt',
        'output/reflectometry1/dppc_xray/dppc_p_sum_sp20.txt',
        'output/reflectometry1/dppc_xray/dppc_p_sum_sp25.txt',
        'output/reflectometry1/dppc_xray/dppc_p_sum_sp30.txt'
    output:
        FIG_REFL1 + 'pear.pdf',
    shell:
        """
        cd visualisation && python pear_plotting.py
        """

rule apm_plotting:
    input:
        'visualisation/apm.py',
        'data/reflectometry2/surf_iso.csv'
    output:
        FIG_REFL2 + 'apm.pdf',
    shell:
        """
        cd visualisation && python apm.py
        """
