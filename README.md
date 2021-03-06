# ESI for "Coarse-grained modelling for soft matter scattering"

[Andrew R. McCluskey](https://orcid.org/0000-0003-3381-5911)

[a.r.mccluskey@bath.ac.uk](mailto:a.r.mccluskey@bath.ac.uk)/[andrew.mccluskey@diamond.ac.uk](mailto:andrew.mccluskey@diamond.ac.uk)

Supervisors: [Karen J. Edler](https://orcid.org/0000-0001-5822-0127) (Bath), [Stephen C. Parker](https://orcid.org/0000-0003-3804-0975) (Bath), [Andrew J. Smith](https://orcid.org/0000-0003-3745-7082) (DLS), and [Jonathan L. Rawle](https://orcid.org/0000-0001-8767-4443) (DLS)

This is the electronic supplementary information (ESI) associated with the Ph.D. thesis of Andrew R. McCluskey.
The thesis title is "Coarse-grained modelling for soft matter scattering".
This ESI provides full details of the anlayses performed in the work, as well as access to an automated workflow.
Using this we aim to provide better access to analysis reproducibility.
For more information about reproducible workflows in Python, check out [Tania Allard's talk from Pycon2018](http://bitsandchips.me/Talks/PyCon.html#/title).

## Analysis

This ESI aims to provide a fully reproducible workflow to the data analysis presented within the paper.

Requirements:

- anaconda or miniconda python

Before the work may be re-created it is necessary to obtain the experimental data, 
this is stored in a series of repositories in the Bath Data Archive, however, a zip file of all the data may be obtained from contacting Andrew. 
The supplied Snakemake file, will reproduce all of the analysis, plot the figures, and build the thesis (`reports/main.pdf`) when run.
Be aware that the analyses within this work are non-trivial and take many hours to run so **use caution** before re-running.

If you **still** want to re-run all of the analysis, run the following commands:

```
conda env create -f config/environment.yml

source activate thesis

snakemake clean # this will remove all of the output from previous runs

snakemake
```

## Acknowledgements

ARM is grateful to the University of Bath and Diamond Light Source for co-funding a studentship (Studentship No. STU0149).
