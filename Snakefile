REP = 'reports/'
CHAP = 'chapters/'
INTRO = 'introduction/'
THEO = 'theory/'
REFL1 = 'reflectometry1/'
REFL2 = 'reflectometry2/'
SAS = 'smallangle/'
TEACH = 'teaching/'
APP = 'appendices/'
FIG_DIR = REP + 'figures/'
FIG_THEO = FIG_DIR + 'theory/'
FIG_REFL1 = FIG_DIR + REFL1
FIG_REFL2 = FIG_DIR + REFL2
FIG_SAS = FIG_DIR + SAS
FIG_TEACH = FIG_DIR + TEACH
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
           FIG_REFL2 + 'dspc_slipids_50_ref_sld.pdf',
           FIG_REFL2 + 'martini_order.pdf',
           FIG_REFL2 + 'water_20.pdf',
           FIG_REFL2 + 'water_30.pdf',
           FIG_REFL2 + 'water_40.pdf',
           FIG_REFL2 + 'water_50.pdf',
           FIG_REFL2 + 'dspc_slipids_30_ref_sld_short.pdf',
           FIG_SAS + 'scaling.pdf',
           FIG_SAS + 'speedup.pdf',
           FIG_SAS + 'fake.pdf',
           FIG_SAS + 'fake_assess1.pdf',
           FIG_SAS + 'fake_assess2.pdf',
           FIG_SAS + 'fake_assess3.pdf',
           FIG_SAS + 'fake_assess4.pdf',
           FIG_SAS + 'fake_assess5.pdf',
           FIG_SAS + 'fake_assess6.pdf',
           FIG_SAS + 'fake_assess7.pdf',
           FIG_SAS + 'fake_assess8.pdf',
           FIG_SAS + 'fake_assess9.pdf',
           FIG_SAS + 'fake_assess10.pdf',
           #FIG_SAS + 'real_assess1.pdf',
           #FIG_SAS + 'real_assess2.pdf',
           #FIG_SAS + 'real_assess3.pdf',
           #FIG_SAS + 'real_assess4.pdf',
           #FIG_SAS + 'real_assess5.pdf',
           #FIG_SAS + 'real_assess6.pdf',
           #FIG_SAS + 'real_assess7.pdf',
           #FIG_SAS + 'real_assess8.pdf',
           #FIG_SAS + 'real_assess9.pdf',
           #FIG_SAS + 'real_assess10.pdf',
           FIG_SAS + 'exp_data.pdf',
           FIG_TEACH + 'chem_data_py.pdf']
CHAPTERS = [REP + CHAP + 'introduction.tex', REP + CHAP + 'theory.tex',
            REP + CHAP + 'reflectometry1.tex',
            REP + CHAP + 'reflectometry2.tex', REP + CHAP + 'smallangle.tex',
            REP + CHAP + 'teaching.tex', REP + CHAP + 'summary.tex']
LATEX = [REP + CHAP + INTRO + 'soft_matter.tex',
         REP + CHAP + INTRO + 'scattering.tex',
         REP + CHAP + INTRO + 'coarsegraining.tex',
         REP + CHAP + INTRO + 'optimisation.tex',
         REP + CHAP + INTRO + 'education.tex',
         REP + CHAP + THEO + 'scattheory.tex',
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
         REP + CHAP + TEACH + 'abstract.tex',
         REP + CHAP + TEACH + 'context.tex',
         REP + CHAP + TEACH + 'intro.tex',
         REP + CHAP + TEACH + 'pylj.tex',
         REP + CHAP + TEACH + 'sim_and_scat.tex',
         REP + CHAP + TEACH + 'conclusions.tex',
         REP + CHAP + SAS + 'abstract.tex',
         REP + CHAP + SAS + 'context.tex',
         REP + CHAP + SAS + 'intro.tex',
         REP + CHAP + SAS + 'methods.tex',
         REP + CHAP + SAS + 'discussion.tex',
         REP + 'appendices/papers.tex']
CODE_BLOCKS = [REP + 'code_blocks/' + 'reflectometry.py',
               REP + 'code_blocks/' + 'lennardjones.py',
               REP + 'code_blocks/' + 'diff_evo.py',
               REP + 'code_blocks/' + 'selection.py',
               REP + 'code_blocks/' + 'mutation.py',
               REP + 'code_blocks/' + 'part_swarm.py',
               REP + 'code_blocks/' + 'recombination.py',
               REP + 'code_blocks/' + 'grad.py',
               REP + 'code_blocks/' + 'pyljmd.py',
               REP + 'code_blocks/' + 'pyljlj.py',
               REP + 'code_blocks/' + 'mol_vol.py']

SCRIPTS = ['scripts/theory.py', 'scripts/XRR_plotting.py',
           'scripts/chemically_consistent.py']

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

rule clean_all:
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
        shell("rm -f scripts/theory.py")

rule thesis:
    input:
        'reports/MastersDoctoralThesis.cls',
        LATEX,
        REP + 'main.tex',
        REP + 'main.bib',
        CHAPTERS,
        FIGURES,
        FIGURES_PLOT,
        CODE_BLOCKS,
        'output/reflectometry2/dspc_20/dspc_martini_20_dt.txt',
        'output/reflectometry2/dspc_30/dspc_martini_30_dt.txt',
        'output/reflectometry2/dspc_40/dspc_martini_40_dt.txt',
        'output/reflectometry2/dspc_50/dspc_martini_50_dt.txt',
        'output/reflectometry2/dspc_20/dspc_berger_20_dt.txt',
        'output/reflectometry2/dspc_30/dspc_berger_30_dt.txt',
        'output/reflectometry2/dspc_40/dspc_berger_40_dt.txt',
        'output/reflectometry2/dspc_50/dspc_berger_50_dt.txt',
        'output/reflectometry2/dspc_20/dspc_slipids_20_dt.txt',
        'output/reflectometry2/dspc_30/dspc_slipids_30_dt.txt',
        'output/reflectometry2/dspc_40/dspc_slipids_40_dt.txt',
        'output/reflectometry2/dspc_50/dspc_slipids_50_dt.txt',
        'output/reflectometry2/dspc_20/dspc_martini_20_wph.txt',
        'output/reflectometry2/dspc_30/dspc_martini_30_wph.txt',
        'output/reflectometry2/dspc_40/dspc_martini_40_wph.txt',
        'output/reflectometry2/dspc_50/dspc_martini_50_wph.txt',
        'output/reflectometry2/dspc_20/dspc_berger_20_wph.txt',
        'output/reflectometry2/dspc_30/dspc_berger_30_wph.txt',
        'output/reflectometry2/dspc_40/dspc_berger_40_wph.txt',
        'output/reflectometry2/dspc_50/dspc_berger_50_wph.txt',
        'output/reflectometry2/dspc_20/dspc_slipids_20_wph.txt',
        'output/reflectometry2/dspc_30/dspc_slipids_30_wph.txt',
        'output/reflectometry2/dspc_40/dspc_slipids_40_wph.txt',
        'output/reflectometry2/dspc_50/dspc_slipids_50_wph.txt',
        'output/reflectometry2/dspc_30/slipids_mean_N_30.txt',
        'output/reflectometry2/dspc_20/slipids_mean_N_20.txt',
        'output/reflectometry2/dspc_40/slipids_mean_N_40.txt',
        'output/reflectometry2/dspc_50/slipids_mean_N_50.txt'
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
        'scripts/theory.py',
        'data/theory/Experimental-sphere.txt',
        CODE_BLOCKS
    output:
        FIGURES_PLOT
    shell:
        """
        cd scripts && python theory.py
        """

rule fake_fig:
    input:
        'scripts/make_fake.py',
    output:
        'reports/figures/smallangle/fake.pdf'
    shell:
        """
        cd scripts && python make_fake.py
        """

rule exp_fig:
    input:
        'scripts/plot_exp.py',
        'data/smallangle/sans2d.txt'
    output:
        'reports/figures/smallangle/exp_data.pdf'
    shell:
        """
        cd scripts && python plot_exp.py
        """

rule fakeassess_fig:
    input:
        'scripts/assess_fake.py',
        'data/smallangle/best_fake/best1.fit',
        'data/smallangle/best_fake/best1.xyz',
        'data/smallangle/best_fake/best2.fit',
        'data/smallangle/best_fake/best2.xyz',
        'data/smallangle/best_fake/best3.fit',
        'data/smallangle/best_fake/best3.xyz',
        'data/smallangle/best_fake/best4.fit',
        'data/smallangle/best_fake/best4.xyz',
        'data/smallangle/best_fake/best5.fit',
        'data/smallangle/best_fake/best5.xyz',
        'data/smallangle/best_fake/best6.fit',
        'data/smallangle/best_fake/best6.xyz',
        'data/smallangle/best_fake/best7.fit',
        'data/smallangle/best_fake/best7.xyz',
        'data/smallangle/best_fake/best8.fit',
        'data/smallangle/best_fake/best8.xyz',
        'data/smallangle/best_fake/best9.fit',
        'data/smallangle/best_fake/best9.xyz',
        'data/smallangle/best_fake/best10.fit',
        'data/smallangle/best_fake/best10.xyz'
    output:
        'reports/figures/smallangle/fake_assess1.pdf',
        'reports/figures/smallangle/fake_assess2.pdf',
        'reports/figures/smallangle/fake_assess3.pdf',
        'reports/figures/smallangle/fake_assess4.pdf',
        'reports/figures/smallangle/fake_assess5.pdf',
        'reports/figures/smallangle/fake_assess6.pdf',
        'reports/figures/smallangle/fake_assess7.pdf',
        'reports/figures/smallangle/fake_assess8.pdf',
        'reports/figures/smallangle/fake_assess9.pdf',
        'reports/figures/smallangle/fake_assess10.pdf'
    shell:
        """
        cd scripts && python assess_fake.py 1
        python assess_fake.py 2
        python assess_fake.py 3
        python assess_fake.py 4
        python assess_fake.py 5
        python assess_fake.py 6
        python assess_fake.py 7
        python assess_fake.py 8
        python assess_fake.py 9
        python assess_fake.py 10
        """

rule realassess_fig:
    input:
        'scripts/assess_real.py',
        'data/smallangle/best_real/best1.fit',
        'data/smallangle/best_real/best1.xyz',
        'data/smallangle/best_real/best2.fit',
        'data/smallangle/best_real/best2.xyz',
        'data/smallangle/best_real/best3.fit',
        'data/smallangle/best_real/best3.xyz',
        'data/smallangle/best_real/best4.fit',
        'data/smallangle/best_real/best4.xyz',
        'data/smallangle/best_real/best5.fit',
        'data/smallangle/best_real/best5.xyz',
        'data/smallangle/best_real/best6.fit',
        'data/smallangle/best_real/best6.xyz',
        'data/smallangle/best_real/best7.fit',
        'data/smallangle/best_real/best7.xyz',
        'data/smallangle/best_real/best8.fit',
        'data/smallangle/best_real/best8.xyz',
        'data/smallangle/best_real/best9.fit',
        'data/smallangle/best_real/best9.xyz',
        'data/smallangle/best_real/best10.fit',
        'data/smallangle/best_real/best10.xyz'
    output:
        'reports/figures/smallangle/real_assess1.pdf',
        'reports/figures/smallangle/real_assess2.pdf',
        'reports/figures/smallangle/real_assess3.pdf',
        'reports/figures/smallangle/real_assess4.pdf',
        'reports/figures/smallangle/real_assess5.pdf',
        'reports/figures/smallangle/real_assess6.pdf',
        'reports/figures/smallangle/real_assess7.pdf',
        'reports/figures/smallangle/real_assess8.pdf',
        'reports/figures/smallangle/real_assess9.pdf',
        'reports/figures/smallangle/real_assess10.pdf'
    shell:
        """
        cd scripts && python assess_real.py 1
        python assess_real.py 2
        python assess_real.py 3
        python assess_real.py 4
        python assess_real.py 5
        python assess_real.py 6
        python assess_real.py 7
        python assess_real.py 8
        python assess_real.py 9
        python assess_real.py 10
        """

rule scaling_fig:
    input:
        'scripts/scaling.py',
    output:
        'reports/figures/smallangle/scaling.pdf',
        'reports/figures/smallangle/speedup.pdf'
    shell:
        """
        cd scripts && python scaling.py
        """

rule dppc_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_15.dat',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_20.dat',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_25.dat',
        'data/reflectometry1/dppc_xray/dppc_xray_sp_30.dat'
    output:
        'output/reflectometry1/dppc_xray/dppc_xray_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dppc 15 15 20 25 30 0
        """

rule dmpc_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_20.dat',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_25.dat',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_30.dat',
        'data/reflectometry1/dmpc_xray/dmpc_xray_sp_40.dat'
    output:
        'output/reflectometry1/dmpc_xray/dmpc_xray_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dmpc 13 20 25 30 40 0
        """

rule dlpc_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_20.dat',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_25.dat',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_30.dat',
        'data/reflectometry1/dlpc_xray/dlpc_xray_sp_35.dat'
    output:
        'output/reflectometry1/dlpc_xray/dlpc_xray_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dlpc 11 20 25 30 35 0
        """

rule dmpg_xray_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_15.dat',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_20.dat',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_25.dat',
        'data/reflectometry1/dmpg_xray/dmpg_xray_sp_30.dat'
    output:
        'output/reflectometry1/dmpg_xray/dmpg_xray_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dmpg 13 15 20 25 30 0
        """

rule dppc_xray_plotting:
    input:
        'scripts/XRR_plotting.py',
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
        cd scripts && python XRR_plotting.py dppc 15 15 20 25 30 0
        """
rule dmpc_xray_plotting:
    input:
        'scripts/XRR_plotting.py',
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
        cd scripts && python XRR_plotting.py dmpc 13 20 25 30 40 0
        """

rule dlpc_xray_plotting:
    input:
        'scripts/XRR_plotting.py',
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
        cd scripts && python XRR_plotting.py dlpc 11 20 25 30 35 0
        """

rule dmpg_xray_plotting:
    input:
        'scripts/XRR_plotting.py',
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
        cd scripts && python XRR_plotting.py dmpg 13 15 20 25 30 0
        """

rule dppc_neutron_15_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dppc_neutron/dppc_neutron_h_sp_15.dat',
        'data/reflectometry1/dppc_neutron/dppc_neutron_hd_sp_15.dat',
        'output/reflectometry1/dppc_xray/dppc_xray-d_h.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_t.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_h.tex'
    output:
        'output/reflectometry1/dppc_neutron/dppc_neutron_15_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dppc 15 15 h hd 30 1
        """

rule dppc_neutron_20_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dppc_neutron/dppc_neutron_h_sp_20.dat',
        'data/reflectometry1/dppc_neutron/dppc_neutron_hd_sp_20.dat',
        'output/reflectometry1/dppc_xray/dppc_xray-d_h.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_t.tex',
        'output/reflectometry1/dppc_xray/dppc_xray-V_h.tex'
    output:
        'output/reflectometry1/dppc_neutron/dppc_neutron_20_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dppc 15 20 h hd 30 1
        """

rule dmpc_neutron_20_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_h_sp_20.dat',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_hd_sp_20.dat',
        'output/reflectometry1/dmpc_xray/dmpc_xray-d_h.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_t.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_h.tex'
    output:
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_20_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dmpc 13 20 h hd 30 1
        """

rule dmpc_neutron_25_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_h_sp_25.dat',
        'data/reflectometry1/dmpc_neutron/dmpc_neutron_hd_sp_25.dat',
        'output/reflectometry1/dmpc_xray/dmpc_xray-d_h.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_t.tex',
        'output/reflectometry1/dmpc_xray/dmpc_xray-V_h.tex'
    output:
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_25_chain.txt'
    shell:
        """
        cd scripts && python chemically_consistent.py dmpc 13 25 h hd 30 1
        """

rule dspc_neutron_20_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
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
        cd scripts && python chemically_consistent.py dspc 17 20 47.9 2 3 1
        """

rule dspc_neutron_30_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
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
        cd scripts && python chemically_consistent.py dspc 17 30 46.4 2 3 1
        """

rule dspc_neutron_40_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
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
        cd scripts && python chemically_consistent.py dspc 17 40 45.0 2 3 1
        """

rule dspc_neutron_50_analysis:
    input:
        'reports/code_blocks/mol_vol.py',
        'reports/code_blocks/ref_help.py',
        'scripts/chemically_consistent.py',
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
        cd scripts && python chemically_consistent.py dspc 17 50 44.6 2 3 1
        """

rule dspc_neutron_20_plotting:
    input:
        'scripts/NR_plotting2.py',
        'output/reflectometry2/dspc_20/dspc_20_chain.txt'
    output:
        FIG_REFL2 + 'dspc_20_pdf.pdf',
        FIG_REFL2 + 'dspc_20_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting2.py dspc 17 20 47.9
        """

rule dspc_neutron_30_plotting:
    input:
        'scripts/NR_plotting2.py',
        'output/reflectometry2/dspc_30/dspc_30_chain.txt'
    output:
        FIG_REFL2 + 'dspc_30_pdf.pdf',
        FIG_REFL2 + 'dspc_30_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting2.py dspc 17 30 46.4
        """

rule dspc_neutron_40_plotting:
    input:
        'scripts/NR_plotting2.py',
        'output/reflectometry2/dspc_40/dspc_40_chain.txt'
    output:
        FIG_REFL2 + 'dspc_40_pdf.pdf',
        FIG_REFL2 + 'dspc_40_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting2.py dspc 17 40 45.0
        """

rule dspc_neutron_50_plotting:
    input:
        'scripts/NR_plotting2.py',
        'output/reflectometry2/dspc_50/dspc_50_chain.txt'
    output:
        FIG_REFL2 + 'dspc_50_pdf.pdf',
        FIG_REFL2 + 'dspc_50_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting2.py dspc 17 50 44.6
        """

rule dppc_neutron_15_plotting:
    input:
        'scripts/NR_plotting.py',
        'output/reflectometry1/dppc_neutron/dppc_neutron_15_chain.txt'
    output:
        FIG_REFL1 + 'dppc_neutron_15_pdf.pdf',
        FIG_REFL1 + 'dppc_neutron_15_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting.py dppc 15 15 h hd 30 1
        """

rule dppc_neutron_20_plotting:
    input:
        'scripts/NR_plotting.py',
        'output/reflectometry1/dppc_neutron/dppc_neutron_20_chain.txt'
    output:
        FIG_REFL1 + 'dppc_neutron_20_pdf.pdf',
        FIG_REFL1 + 'dppc_neutron_20_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting.py dppc 15 20 h hd 30 1
        """

rule dmpc_neutron_20_plotting:
    input:
        'scripts/NR_plotting.py',
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_20_chain.txt'
    output:
        FIG_REFL1 + 'dmpc_neutron_20_pdf.pdf',
        FIG_REFL1 + 'dmpc_neutron_20_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting.py dmpc 13 20 h hd 30 1
        """

rule dmpc_neutron_25_plotting:
    input:
        'scripts/NR_plotting.py',
        'output/reflectometry1/dmpc_neutron/dmpc_neutron_25_chain.txt'
    output:
        FIG_REFL1 + 'dmpc_neutron_25_pdf.pdf',
        FIG_REFL1 + 'dmpc_neutron_25_ref_sld.pdf'
    shell:
        """
        cd scripts && python NR_plotting.py dmpc 13 25 h hd 30 1
        """

rule martini_dspc_20_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py martini 20 4 0.4
        """

rule martini_dspc_30_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py martini 30 4 0.4
        """

rule martini_dspc_40_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py martini 40 4 0.4
        """

rule martini_dspc_50_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py martini 50 4 0.4
        """

rule berger_dspc_20_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py berger 20 1 0
        """

rule berger_dspc_30_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py berger 30 1 0
        """

rule berger_dspc_40_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py berger 40 1 0
        """

rule berger_dspc_50_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py berger 50 1 0
        """

rule slipids_dspc_20_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py slipids 20 1 0
        """

rule slipids_dspc_30_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py slipids 30 1 0
        """

rule slipids_dspc_30_analysis_short:
    input:
        'scripts/sim_analysis.py',
        'data/reflectometry2/dspc_30/slipids_frame1.pdb',
        'data/reflectometry2/dspc_30/slipids_frame2.pdb',
        'data/reflectometry2/dspc_30/d13acmw30.dat',
        'data/reflectometry2/dspc_30/d13d2o30.dat',
        'data/reflectometry2/dspc_30/d70acmw30.dat',
        'data/reflectometry2/dspc_30/d70d2o30.dat',
        'data/reflectometry2/dspc_30/d83acmw30.dat',
        'data/reflectometry2/dspc_30/d83d2o30.dat',
        'data/reflectometry2/dspc_30/hd2o30.dat'
    output:
        FIG_REFL2 + 'dspc_slipids_30_ref_sld_short.pdf',
    shell:
        """
        cd scripts && python short_sim_analysis.py slipids 30 1 0
        """

rule slipids_dspc_40_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py slipids 40 1 0
        """

rule slipids_dspc_50_analysis:
    input:
        'scripts/sim_analysis.py',
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
        cd scripts && python sim_analysis.py slipids 50 1 0
        """

rule martini_dspc_20_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_20/martini_frame1.pdb',
        'data/reflectometry2/dspc_20/martini_frame2.pdb',
        'data/reflectometry2/dspc_20/martini_frame3.pdb',
        'data/reflectometry2/dspc_20/martini_frame4.pdb',
        'data/reflectometry2/dspc_20/martini_frame5.pdb',
        'data/reflectometry2/dspc_20/martini_frame6.pdb',
        'data/reflectometry2/dspc_20/martini_frame7.pdb',
        'data/reflectometry2/dspc_20/martini_frame8.pdb',
        'data/reflectometry2/dspc_20/martini_frame9.pdb',
        'data/reflectometry2/dspc_20/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_20/dspc_martini_20_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py martini 20
        """

rule martini_dspc_30_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_30/martini_frame1.pdb',
        'data/reflectometry2/dspc_30/martini_frame2.pdb',
        'data/reflectometry2/dspc_30/martini_frame3.pdb',
        'data/reflectometry2/dspc_30/martini_frame4.pdb',
        'data/reflectometry2/dspc_30/martini_frame5.pdb',
        'data/reflectometry2/dspc_30/martini_frame6.pdb',
        'data/reflectometry2/dspc_30/martini_frame7.pdb',
        'data/reflectometry2/dspc_30/martini_frame8.pdb',
        'data/reflectometry2/dspc_30/martini_frame9.pdb',
        'data/reflectometry2/dspc_30/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_30/dspc_martini_30_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py martini 30
        """

rule martini_dspc_40_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_40/martini_frame1.pdb',
        'data/reflectometry2/dspc_40/martini_frame2.pdb',
        'data/reflectometry2/dspc_40/martini_frame3.pdb',
        'data/reflectometry2/dspc_40/martini_frame4.pdb',
        'data/reflectometry2/dspc_40/martini_frame5.pdb',
        'data/reflectometry2/dspc_40/martini_frame6.pdb',
        'data/reflectometry2/dspc_40/martini_frame7.pdb',
        'data/reflectometry2/dspc_40/martini_frame8.pdb',
        'data/reflectometry2/dspc_40/martini_frame9.pdb',
        'data/reflectometry2/dspc_40/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_40/dspc_martini_40_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py martini 40
        """

rule martini_dspc_50_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_50/martini_frame1.pdb',
        'data/reflectometry2/dspc_50/martini_frame2.pdb',
        'data/reflectometry2/dspc_50/martini_frame3.pdb',
        'data/reflectometry2/dspc_50/martini_frame4.pdb',
        'data/reflectometry2/dspc_50/martini_frame5.pdb',
        'data/reflectometry2/dspc_50/martini_frame6.pdb',
        'data/reflectometry2/dspc_50/martini_frame7.pdb',
        'data/reflectometry2/dspc_50/martini_frame8.pdb',
        'data/reflectometry2/dspc_50/martini_frame9.pdb',
        'data/reflectometry2/dspc_50/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_50/dspc_martini_50_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py martini 50
        """

rule berger_dspc_20_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_20/berger_frame1.pdb',
        'data/reflectometry2/dspc_20/berger_frame2.pdb',
        'data/reflectometry2/dspc_20/berger_frame3.pdb',
        'data/reflectometry2/dspc_20/berger_frame4.pdb',
        'data/reflectometry2/dspc_20/berger_frame5.pdb',
        'data/reflectometry2/dspc_20/berger_frame6.pdb',
        'data/reflectometry2/dspc_20/berger_frame7.pdb',
        'data/reflectometry2/dspc_20/berger_frame8.pdb',
        'data/reflectometry2/dspc_20/berger_frame9.pdb',
        'data/reflectometry2/dspc_20/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_20/dspc_berger_20_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py berger 20
        """

rule berger_dspc_30_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_30/berger_frame1.pdb',
        'data/reflectometry2/dspc_30/berger_frame2.pdb',
        'data/reflectometry2/dspc_30/berger_frame3.pdb',
        'data/reflectometry2/dspc_30/berger_frame4.pdb',
        'data/reflectometry2/dspc_30/berger_frame5.pdb',
        'data/reflectometry2/dspc_30/berger_frame6.pdb',
        'data/reflectometry2/dspc_30/berger_frame7.pdb',
        'data/reflectometry2/dspc_30/berger_frame8.pdb',
        'data/reflectometry2/dspc_30/berger_frame9.pdb',
        'data/reflectometry2/dspc_30/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_30/dspc_berger_30_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py berger 30
        """

rule berger_dspc_40_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_40/berger_frame1.pdb',
        'data/reflectometry2/dspc_40/berger_frame2.pdb',
        'data/reflectometry2/dspc_40/berger_frame3.pdb',
        'data/reflectometry2/dspc_40/berger_frame4.pdb',
        'data/reflectometry2/dspc_40/berger_frame5.pdb',
        'data/reflectometry2/dspc_40/berger_frame6.pdb',
        'data/reflectometry2/dspc_40/berger_frame7.pdb',
        'data/reflectometry2/dspc_40/berger_frame8.pdb',
        'data/reflectometry2/dspc_40/berger_frame9.pdb',
        'data/reflectometry2/dspc_40/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_40/dspc_berger_40_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py berger 40
        """

rule berger_dspc_50_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_50/berger_frame1.pdb',
        'data/reflectometry2/dspc_50/berger_frame2.pdb',
        'data/reflectometry2/dspc_50/berger_frame3.pdb',
        'data/reflectometry2/dspc_50/berger_frame4.pdb',
        'data/reflectometry2/dspc_50/berger_frame5.pdb',
        'data/reflectometry2/dspc_50/berger_frame6.pdb',
        'data/reflectometry2/dspc_50/berger_frame7.pdb',
        'data/reflectometry2/dspc_50/berger_frame8.pdb',
        'data/reflectometry2/dspc_50/berger_frame9.pdb',
        'data/reflectometry2/dspc_50/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_50/dspc_berger_50_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py berger 50
        """

rule slipids_dspc_20_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_20/slipids_frame1.pdb',
        'data/reflectometry2/dspc_20/slipids_frame2.pdb',
        'data/reflectometry2/dspc_20/slipids_frame3.pdb',
        'data/reflectometry2/dspc_20/slipids_frame4.pdb',
        'data/reflectometry2/dspc_20/slipids_frame5.pdb',
        'data/reflectometry2/dspc_20/slipids_frame6.pdb',
        'data/reflectometry2/dspc_20/slipids_frame7.pdb',
        'data/reflectometry2/dspc_20/slipids_frame8.pdb',
        'data/reflectometry2/dspc_20/slipids_frame9.pdb',
        'data/reflectometry2/dspc_20/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_20/dspc_slipids_20_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py slipids 20
        """

rule slipids_dspc_30_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_30/slipids_frame1.pdb',
        'data/reflectometry2/dspc_30/slipids_frame2.pdb',
        'data/reflectometry2/dspc_30/slipids_frame3.pdb',
        'data/reflectometry2/dspc_30/slipids_frame4.pdb',
        'data/reflectometry2/dspc_30/slipids_frame5.pdb',
        'data/reflectometry2/dspc_30/slipids_frame6.pdb',
        'data/reflectometry2/dspc_30/slipids_frame7.pdb',
        'data/reflectometry2/dspc_30/slipids_frame8.pdb',
        'data/reflectometry2/dspc_30/slipids_frame9.pdb',
        'data/reflectometry2/dspc_30/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_30/dspc_slipids_30_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py slipids 30
        """

rule slipids_dspc_40_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_40/slipids_frame1.pdb',
        'data/reflectometry2/dspc_40/slipids_frame2.pdb',
        'data/reflectometry2/dspc_40/slipids_frame3.pdb',
        'data/reflectometry2/dspc_40/slipids_frame4.pdb',
        'data/reflectometry2/dspc_40/slipids_frame5.pdb',
        'data/reflectometry2/dspc_40/slipids_frame6.pdb',
        'data/reflectometry2/dspc_40/slipids_frame7.pdb',
        'data/reflectometry2/dspc_40/slipids_frame8.pdb',
        'data/reflectometry2/dspc_40/slipids_frame9.pdb',
        'data/reflectometry2/dspc_40/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_40/dspc_slipids_40_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py slipids 40
        """

rule slipids_dspc_50_tail:
    input:
        'scripts/tail_length.py',
        'data/reflectometry2/dspc_50/slipids_frame1.pdb',
        'data/reflectometry2/dspc_50/slipids_frame2.pdb',
        'data/reflectometry2/dspc_50/slipids_frame3.pdb',
        'data/reflectometry2/dspc_50/slipids_frame4.pdb',
        'data/reflectometry2/dspc_50/slipids_frame5.pdb',
        'data/reflectometry2/dspc_50/slipids_frame6.pdb',
        'data/reflectometry2/dspc_50/slipids_frame7.pdb',
        'data/reflectometry2/dspc_50/slipids_frame8.pdb',
        'data/reflectometry2/dspc_50/slipids_frame9.pdb',
        'data/reflectometry2/dspc_50/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_50/dspc_slipids_50_dt.txt'
    shell:
        """
        cd scripts && python tail_length.py slipids 50
        """

rule martini_dspc_20_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_20/martini_frame1.pdb',
        'data/reflectometry2/dspc_20/martini_frame2.pdb',
        'data/reflectometry2/dspc_20/martini_frame3.pdb',
        'data/reflectometry2/dspc_20/martini_frame4.pdb',
        'data/reflectometry2/dspc_20/martini_frame5.pdb',
        'data/reflectometry2/dspc_20/martini_frame6.pdb',
        'data/reflectometry2/dspc_20/martini_frame7.pdb',
        'data/reflectometry2/dspc_20/martini_frame8.pdb',
        'data/reflectometry2/dspc_20/martini_frame9.pdb',
        'data/reflectometry2/dspc_20/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_20/dspc_martini_20_wph.txt'
    shell:
        """
        cd scripts && python waters.py martini 20
        """

rule martini_dspc_30_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_30/martini_frame1.pdb',
        'data/reflectometry2/dspc_30/martini_frame2.pdb',
        'data/reflectometry2/dspc_30/martini_frame3.pdb',
        'data/reflectometry2/dspc_30/martini_frame4.pdb',
        'data/reflectometry2/dspc_30/martini_frame5.pdb',
        'data/reflectometry2/dspc_30/martini_frame6.pdb',
        'data/reflectometry2/dspc_30/martini_frame7.pdb',
        'data/reflectometry2/dspc_30/martini_frame8.pdb',
        'data/reflectometry2/dspc_30/martini_frame9.pdb',
        'data/reflectometry2/dspc_30/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_30/dspc_martini_30_wph.txt'
    shell:
        """
        cd scripts && python waters.py martini 30
        """

rule martini_dspc_40_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_40/martini_frame1.pdb',
        'data/reflectometry2/dspc_40/martini_frame2.pdb',
        'data/reflectometry2/dspc_40/martini_frame3.pdb',
        'data/reflectometry2/dspc_40/martini_frame4.pdb',
        'data/reflectometry2/dspc_40/martini_frame5.pdb',
        'data/reflectometry2/dspc_40/martini_frame6.pdb',
        'data/reflectometry2/dspc_40/martini_frame7.pdb',
        'data/reflectometry2/dspc_40/martini_frame8.pdb',
        'data/reflectometry2/dspc_40/martini_frame9.pdb',
        'data/reflectometry2/dspc_40/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_40/dspc_martini_40_wph.txt'
    shell:
        """
        cd scripts && python waters.py martini 40
        """

rule martini_dspc_50_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_50/martini_frame1.pdb',
        'data/reflectometry2/dspc_50/martini_frame2.pdb',
        'data/reflectometry2/dspc_50/martini_frame3.pdb',
        'data/reflectometry2/dspc_50/martini_frame4.pdb',
        'data/reflectometry2/dspc_50/martini_frame5.pdb',
        'data/reflectometry2/dspc_50/martini_frame6.pdb',
        'data/reflectometry2/dspc_50/martini_frame7.pdb',
        'data/reflectometry2/dspc_50/martini_frame8.pdb',
        'data/reflectometry2/dspc_50/martini_frame9.pdb',
        'data/reflectometry2/dspc_50/martini_frame10.pdb'
    output:
        'output/reflectometry2/dspc_50/dspc_martini_50_wph.txt'
    shell:
        """
        cd scripts && python waters.py martini 50
        """

rule berger_dspc_20_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_20/berger_frame1.pdb',
        'data/reflectometry2/dspc_20/berger_frame2.pdb',
        'data/reflectometry2/dspc_20/berger_frame3.pdb',
        'data/reflectometry2/dspc_20/berger_frame4.pdb',
        'data/reflectometry2/dspc_20/berger_frame5.pdb',
        'data/reflectometry2/dspc_20/berger_frame6.pdb',
        'data/reflectometry2/dspc_20/berger_frame7.pdb',
        'data/reflectometry2/dspc_20/berger_frame8.pdb',
        'data/reflectometry2/dspc_20/berger_frame9.pdb',
        'data/reflectometry2/dspc_20/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_20/dspc_berger_20_wph.txt'
    shell:
        """
        cd scripts && python waters.py berger 20
        """

rule berger_dspc_30_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_30/berger_frame1.pdb',
        'data/reflectometry2/dspc_30/berger_frame2.pdb',
        'data/reflectometry2/dspc_30/berger_frame3.pdb',
        'data/reflectometry2/dspc_30/berger_frame4.pdb',
        'data/reflectometry2/dspc_30/berger_frame5.pdb',
        'data/reflectometry2/dspc_30/berger_frame6.pdb',
        'data/reflectometry2/dspc_30/berger_frame7.pdb',
        'data/reflectometry2/dspc_30/berger_frame8.pdb',
        'data/reflectometry2/dspc_30/berger_frame9.pdb',
        'data/reflectometry2/dspc_30/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_30/dspc_berger_30_wph.txt'
    shell:
        """
        cd scripts && python waters.py berger 30
        """

rule berger_dspc_40_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_40/berger_frame1.pdb',
        'data/reflectometry2/dspc_40/berger_frame2.pdb',
        'data/reflectometry2/dspc_40/berger_frame3.pdb',
        'data/reflectometry2/dspc_40/berger_frame4.pdb',
        'data/reflectometry2/dspc_40/berger_frame5.pdb',
        'data/reflectometry2/dspc_40/berger_frame6.pdb',
        'data/reflectometry2/dspc_40/berger_frame7.pdb',
        'data/reflectometry2/dspc_40/berger_frame8.pdb',
        'data/reflectometry2/dspc_40/berger_frame9.pdb',
        'data/reflectometry2/dspc_40/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_40/dspc_berger_40_wph.txt'
    shell:
        """
        cd scripts && python waters.py berger 40
        """

rule berger_dspc_50_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_50/berger_frame1.pdb',
        'data/reflectometry2/dspc_50/berger_frame2.pdb',
        'data/reflectometry2/dspc_50/berger_frame3.pdb',
        'data/reflectometry2/dspc_50/berger_frame4.pdb',
        'data/reflectometry2/dspc_50/berger_frame5.pdb',
        'data/reflectometry2/dspc_50/berger_frame6.pdb',
        'data/reflectometry2/dspc_50/berger_frame7.pdb',
        'data/reflectometry2/dspc_50/berger_frame8.pdb',
        'data/reflectometry2/dspc_50/berger_frame9.pdb',
        'data/reflectometry2/dspc_50/berger_frame10.pdb'
    output:
        'output/reflectometry2/dspc_50/dspc_berger_50_wph.txt'
    shell:
        """
        cd scripts && python waters.py berger 50
        """

rule slipids_dspc_20_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_20/slipids_frame1.pdb',
        'data/reflectometry2/dspc_20/slipids_frame2.pdb',
        'data/reflectometry2/dspc_20/slipids_frame3.pdb',
        'data/reflectometry2/dspc_20/slipids_frame4.pdb',
        'data/reflectometry2/dspc_20/slipids_frame5.pdb',
        'data/reflectometry2/dspc_20/slipids_frame6.pdb',
        'data/reflectometry2/dspc_20/slipids_frame7.pdb',
        'data/reflectometry2/dspc_20/slipids_frame8.pdb',
        'data/reflectometry2/dspc_20/slipids_frame9.pdb',
        'data/reflectometry2/dspc_20/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_20/dspc_slipids_20_wph.txt'
    shell:
        """
        cd scripts && python waters.py slipids 20
        """

rule slipids_dspc_30_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_30/slipids_frame1.pdb',
        'data/reflectometry2/dspc_30/slipids_frame2.pdb',
        'data/reflectometry2/dspc_30/slipids_frame3.pdb',
        'data/reflectometry2/dspc_30/slipids_frame4.pdb',
        'data/reflectometry2/dspc_30/slipids_frame5.pdb',
        'data/reflectometry2/dspc_30/slipids_frame6.pdb',
        'data/reflectometry2/dspc_30/slipids_frame7.pdb',
        'data/reflectometry2/dspc_30/slipids_frame8.pdb',
        'data/reflectometry2/dspc_30/slipids_frame9.pdb',
        'data/reflectometry2/dspc_30/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_30/dspc_slipids_30_wph.txt'
    shell:
        """
        cd scripts && python waters.py slipids 30
        """

rule slipids_dspc_40_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_40/slipids_frame1.pdb',
        'data/reflectometry2/dspc_40/slipids_frame2.pdb',
        'data/reflectometry2/dspc_40/slipids_frame3.pdb',
        'data/reflectometry2/dspc_40/slipids_frame4.pdb',
        'data/reflectometry2/dspc_40/slipids_frame5.pdb',
        'data/reflectometry2/dspc_40/slipids_frame6.pdb',
        'data/reflectometry2/dspc_40/slipids_frame7.pdb',
        'data/reflectometry2/dspc_40/slipids_frame8.pdb',
        'data/reflectometry2/dspc_40/slipids_frame9.pdb',
        'data/reflectometry2/dspc_40/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_40/dspc_slipids_40_wph.txt'
    shell:
        """
        cd scripts && python waters.py slipids 40
        """

rule slipids_dspc_50_wph:
    input:
        'scripts/waters.py',
        'data/reflectometry2/dspc_50/slipids_frame1.pdb',
        'data/reflectometry2/dspc_50/slipids_frame2.pdb',
        'data/reflectometry2/dspc_50/slipids_frame3.pdb',
        'data/reflectometry2/dspc_50/slipids_frame4.pdb',
        'data/reflectometry2/dspc_50/slipids_frame5.pdb',
        'data/reflectometry2/dspc_50/slipids_frame6.pdb',
        'data/reflectometry2/dspc_50/slipids_frame7.pdb',
        'data/reflectometry2/dspc_50/slipids_frame8.pdb',
        'data/reflectometry2/dspc_50/slipids_frame9.pdb',
        'data/reflectometry2/dspc_50/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_50/dspc_slipids_50_wph.txt'
    shell:
        """
        cd scripts && python waters.py slipids 50
        """

rule slipids_dspc_30_nd:
    input:
        'scripts/intrinsic.py',
        'data/reflectometry2/dspc_30/slipids_frame1.pdb',
        'data/reflectometry2/dspc_30/slipids_frame2.pdb',
        'data/reflectometry2/dspc_30/slipids_frame3.pdb',
        'data/reflectometry2/dspc_30/slipids_frame4.pdb',
        'data/reflectometry2/dspc_30/slipids_frame5.pdb',
        'data/reflectometry2/dspc_30/slipids_frame6.pdb',
        'data/reflectometry2/dspc_30/slipids_frame7.pdb',
        'data/reflectometry2/dspc_30/slipids_frame8.pdb',
        'data/reflectometry2/dspc_30/slipids_frame9.pdb',
        'data/reflectometry2/dspc_30/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_30/waters_slipids_30.txt',
        'output/reflectometry2/dspc_30/heads_slipids_30.txt',
        'output/reflectometry2/dspc_30/tails_slipids_30.txt'
    shell:
        """
        cd scripts && python intrinsic.py slipids 30
        """

rule slipids_dspc_30_nd_plot:
    input:
        'scripts/water_plot.py',
        'output/reflectometry2/dspc_30/waters_slipids_30.txt',
        'output/reflectometry2/dspc_30/heads_slipids_30.txt',
        'output/reflectometry2/dspc_30/tails_slipids_30.txt'
    output:
        'reports/figures/reflectometry2/water_30.pdf'
    shell:
        """
        cd scripts && python water_plot.py 30
        """

rule slipids_dspc_20_nd:
    input:
        'scripts/intrinsic.py',
        'data/reflectometry2/dspc_20/slipids_frame1.pdb',
        'data/reflectometry2/dspc_20/slipids_frame2.pdb',
        'data/reflectometry2/dspc_20/slipids_frame3.pdb',
        'data/reflectometry2/dspc_20/slipids_frame4.pdb',
        'data/reflectometry2/dspc_20/slipids_frame5.pdb',
        'data/reflectometry2/dspc_20/slipids_frame6.pdb',
        'data/reflectometry2/dspc_20/slipids_frame7.pdb',
        'data/reflectometry2/dspc_20/slipids_frame8.pdb',
        'data/reflectometry2/dspc_20/slipids_frame9.pdb',
        'data/reflectometry2/dspc_20/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_20/waters_slipids_20.txt',
        'output/reflectometry2/dspc_20/heads_slipids_20.txt',
        'output/reflectometry2/dspc_20/tails_slipids_20.txt'
    shell:
        """
        cd scripts && python intrinsic.py slipids 20
        """

rule slipids_dspc_20_nd_plot:
    input:
        'scripts/water_plot.py',
        'output/reflectometry2/dspc_20/waters_slipids_20.txt',
        'output/reflectometry2/dspc_20/heads_slipids_20.txt',
        'output/reflectometry2/dspc_20/tails_slipids_20.txt'
    output:
        'reports/figures/reflectometry2/water_20.pdf'
    shell:
        """
        cd scripts && python water_plot.py 20
        """

rule slipids_dspc_40_nd:
    input:
        'scripts/intrinsic.py',
        'data/reflectometry2/dspc_40/slipids_frame1.pdb',
        'data/reflectometry2/dspc_40/slipids_frame2.pdb',
        'data/reflectometry2/dspc_40/slipids_frame3.pdb',
        'data/reflectometry2/dspc_40/slipids_frame4.pdb',
        'data/reflectometry2/dspc_40/slipids_frame5.pdb',
        'data/reflectometry2/dspc_40/slipids_frame6.pdb',
        'data/reflectometry2/dspc_40/slipids_frame7.pdb',
        'data/reflectometry2/dspc_40/slipids_frame8.pdb',
        'data/reflectometry2/dspc_40/slipids_frame9.pdb',
        'data/reflectometry2/dspc_40/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_40/waters_slipids_40.txt',
        'output/reflectometry2/dspc_40/heads_slipids_40.txt',
        'output/reflectometry2/dspc_40/tails_slipids_40.txt'
    shell:
        """
        cd scripts && python intrinsic.py slipids 40
        """

rule slipids_dspc_40_nd_plot:
    input:
        'scripts/water_plot.py',
        'output/reflectometry2/dspc_40/waters_slipids_40.txt',
        'output/reflectometry2/dspc_40/heads_slipids_40.txt',
        'output/reflectometry2/dspc_40/tails_slipids_40.txt'
    output:
        'reports/figures/reflectometry2/water_40.pdf'
    shell:
        """
        cd scripts && python water_plot.py 40
        """

rule slipids_dspc_50_nd:
    input:
        'scripts/intrinsic.py',
        'data/reflectometry2/dspc_50/slipids_frame1.pdb',
        'data/reflectometry2/dspc_50/slipids_frame2.pdb',
        'data/reflectometry2/dspc_50/slipids_frame3.pdb',
        'data/reflectometry2/dspc_50/slipids_frame4.pdb',
        'data/reflectometry2/dspc_50/slipids_frame5.pdb',
        'data/reflectometry2/dspc_50/slipids_frame6.pdb',
        'data/reflectometry2/dspc_50/slipids_frame7.pdb',
        'data/reflectometry2/dspc_50/slipids_frame8.pdb',
        'data/reflectometry2/dspc_50/slipids_frame9.pdb',
        'data/reflectometry2/dspc_50/slipids_frame10.pdb'
    output:
        'output/reflectometry2/dspc_50/waters_slipids_50.txt',
        'output/reflectometry2/dspc_50/heads_slipids_50.txt',
        'output/reflectometry2/dspc_50/tails_slipids_50.txt'
    shell:
        """
        cd scripts && python intrinsic.py slipids 50
        """

rule slipids_dspc_50_nd_plot:
    input:
        'scripts/water_plot.py',
        'output/reflectometry2/dspc_50/waters_slipids_50.txt',
        'output/reflectometry2/dspc_50/heads_slipids_50.txt',
        'output/reflectometry2/dspc_50/tails_slipids_50.txt'
    output:
        'reports/figures/reflectometry2/water_50.pdf'
    shell:
        """
        cd scripts && python water_plot.py 50
        """

rule spread_30:
    input:
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
        'scripts/roughness.py'
    output:
        'output/reflectometry2/dspc_30/slipids_mean_N_30.txt'
    shell:
        """
        cd scripts && python roughness.py 30
        """

rule spread_20:
    input:
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
        'scripts/roughness.py'
    output:
        'output/reflectometry2/dspc_20/slipids_mean_N_20.txt'
    shell:
        """
        cd scripts && python roughness.py 20
        """

rule spread_40:
    input:
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
        'scripts/roughness.py'
    output:
        'output/reflectometry2/dspc_40/slipids_mean_N_40.txt'
    shell:
        """
        cd scripts && python roughness.py 40
        """

rule spread_50:
    input:
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
        'scripts/roughness.py'
    output:
        'output/reflectometry2/dspc_50/slipids_mean_N_50.txt'
    shell:
        """
        cd scripts && python roughness.py 50
        """

rule pear_plotting:
    input:
        'scripts/pear_plotting.py',
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
        cd scripts && python pear_plotting.py
        """

rule martini_order:
    input:
        'scripts/martini_order.py',
        'data/reflectometry2/dspc_30/martini_frame1.pdb',
        'data/reflectometry2/dspc_30/martini_frame2.pdb',
        'data/reflectometry2/dspc_30/martini_frame3.pdb',
        'data/reflectometry2/dspc_30/martini_frame4.pdb',
        'data/reflectometry2/dspc_30/martini_frame5.pdb',
        'data/reflectometry2/dspc_30/martini_frame6.pdb',
        'data/reflectometry2/dspc_30/martini_frame7.pdb',
        'data/reflectometry2/dspc_30/martini_frame8.pdb',
        'data/reflectometry2/dspc_30/martini_frame9.pdb',
        'data/reflectometry2/dspc_30/martini_frame10.pdb'
    output:
        FIG_REFL2 + 'martini_order.pdf',
    shell:
        """
        cd scripts && python martini_order.py
        """

rule apm_plotting:
    input:
        'scripts/apm.py',
        'data/reflectometry2/surf_iso.csv'
    output:
        FIG_REFL2 + 'apm.pdf',
    shell:
        """
        cd scripts && python apm.py
        """

rule growth_plot:
    input:
        'scripts/growth.py'
    output:
        FIG_TEACH + 'chem_data_py.pdf'
    shell:
        """
        cd scripts && python growth.py
        """
