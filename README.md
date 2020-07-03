This is a repository for National Resource for Network Biology (NRNB) [Google Season of Docs project](https://developers.google.com/season-of-docs/docs/participants) named

# Replacing GUI control tutorials to Jupyter Notebook and R Markdown

<!--
[![CircleCI](https://circleci.com/gh/nrnb/gsod2019_kozo_nishida/tree/master.svg?style=svg)](https://circleci.com/gh/nrnb/gsod2019_kozo_nishida/tree/master)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nrnb/gsod2019_kozo_nishida/master?urlpath=rstudio) (for R)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nrnb/gsod2019_kozo_nishida/master?urlpath=lab/tree) (for Python)
-->
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nrnb/gsod2019_kozo_nishida/master)

## How to use the Binder environment
1. Launch a Binder instance by clicking the above Binder badge.
2. Launch Linux desktop by clicking the `New ▼` button -> `desktop`. ![](https://github.com/nrnb/gsod2019_kozo_nishida/raw/master/images/binder_start_xfce4.jpg)
3. Right click the Linux Desktop and click `Open Terminal Here`, and run the following command. ![](https://github.com/nrnb/gsod2019_kozo_nishida/raw/master/images/right_click_start_terminal.png) 
  ```
  bash ~/cytoscape-unix-3.8.0/cytoscape.sh
  ```
  This command launches Cytoscape Desktop. ![](https://github.com/nrnb/gsod2019_kozo_nishida/raw/master/images/binder_starting_cytoscape_inXFCE4.jpg)
4. Launch Python or R Jupyter Notebook by clicking the `New ▼` button -> `Python 3` or `R`. ![](https://github.com/nrnb/gsod2019_kozo_nishida/raw/master/images/binder_start_pythonR.jpg) and run the code cells. Feel free to modify any of the scripts and run commands directly, but note that your changes will *not* be saved. *Binder only provides a temporary space to try out R and Python automation with Cytoscape.*

## The work we've done
We have written notebook documents that automates the Cytoscape tutorial workflows in http://tutorials.cytoscape.org/ with R and Python.
You can check the our project progress and the links to the commits with the links below.
Our basic commit rule is _**Commit every tutorial slide**_.

### Getting Started

- ["Basic Data Visualization"](https://cytoscape.org/cytoscape-tutorials/protocols/basic-data-visualization)
  - [x] with [Python](./ipynb/Python/basic-data-visualization.ipynb) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/19)
  - [x] with [R](https://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/basic-data-visualization.html) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/11)
- ["Differentially Expressed Genes"](https://cytoscape.org/cytoscape-tutorials/protocols/differentially-expressed-genes)
  - [ ] with Python
  - [x] with [R](https://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/differentially-expressed-genes) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/7)

### Protocols

#### Cytoscape Apps

- [stringApp](https://cytoscape.github.io/cytoscape-tutorials/protocols/stringApp)
  - [ ] with Python
  - [x] with [R](https://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/stringApp.html) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/8)
- [WikiPathways App](https://cytoscape.github.io/cytoscape-tutorials/protocols/wikipathways-app)
  - [ ] with Python
  - [x] with [R](https://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/wikipathways-app.html) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/10)

#### Data Visualization

- [Visualizing Data](https://cytoscape.github.io/cytoscape-tutorials/protocols/mapping-data)
  - [ ] with Python
  - [x] with [R](https://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/mapping-data.html) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/12)
- [Network Layout](https://cytoscape.github.io/cytoscape-tutorials/protocols/network-layout)
  - [ ] with Python
  - [x] with [R](https://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/network-layout.html) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/13)
- [Custom Graphics and Labels](https://cytoscape.github.io/cytoscape-tutorials/protocols/custom-enhanced-graphics-style)
  - [ ] with Python
  - [x] with [R](http://cytoscape.org/cytoscape-automation/for-scripters/R/notebooks/Custom-Graphics.nb.html) (Already written by the mentor)

#### Importing Networks and Tables

- [Loading Networks](https://cytoscape.github.io/cytoscape-tutorials/protocols/loading-networks)
  - [ ] with Python
  - [x] with [R](https://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/loading-networks.html) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/15)
- [Importing Data From Tables](https://cytoscape.github.io/cytoscape-tutorials/protocols/importing-data-from-tables)
  - [x] with [Python](./ipynb/Python/Importing_data.ipynb) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/24)
  - [x] with [R](http://cytoscape.org/cytoscape-automation/for-scripters/R/notebooks/Importing-data.nb.html) , (Already written by the mentor)
- [Importing Network From Table](https://cytoscape.org/cytoscape-tutorials/protocols/importing-network-from-table)
  - [ ] with Python
  - [x] with [R](http://rpubs.com/kozo2/565297) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/17)
- [Identifier Mapping](https://cytoscape.org/cytoscape-tutorials/protocols/identifier-mapping)
  - [ ] with Python
  - [x] with [R](http://cytoscape.org/cytoscape-automation/for-scripters/R/notebooks/Identifier-mapping.nb.html) , (Already written by the mentor)

#### Network Analysis

- [Differentially Expressed Genes Network Analysis](https://cytoscape.org/cytoscape-tutorials/protocols/differentially-expressed-genes)
  - [ ] with Python
  - [ ] with R
- [Affinity Purification-Mass Spectrometry Network Analysis](https://cytoscape.org/cytoscape-tutorials/protocols/AP-MS-network-analysis)
  - [ ] with Python
  - [x] with [R](http://cytoscape.org/cytoscape-automation/for-scripters/R/notebooks/AP-MS-network-analysis.nb.html) , (Already written by the mentor)
- [Variant Data Analysis](https://cytoscape.org/cytoscape-tutorials/protocols/variant-data-analysis)
  - [ ] with Python
  - [x] with [R](http://cytoscape.org/cytoscape-automation/for-scripters/R/notebooks/Cancer-networks-and-data.nb.html) , (Already written by the mentor)
- [EnrichmentMap Pipeline](https://cytoscape.github.io/cytoscape-tutorials/protocols/enrichmentmap-pipeline)
  - [ ] with Python
  - [x] with [R](https://baderlab.github.io/Cytoscape_workflows/EnrichmentMapPipeline/index.html) , (Already written by Ruth Isserlin)
- [Functional Enrichment](https://cytoscape.github.io/cytoscape-tutorials/protocols/functional-enrichment)
  - [ ] with Python
  - [ ] with R [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/6)
- [Filtering by Selection](https://cytoscape.github.io/cytoscape-tutorials/protocols/filtering-by-selection)
  - [ ] with Python
  - [ ] with R

### Exporting and Publishing

- [Saving Results](https://cytoscape.github.io/cytoscape-tutorials/protocols/saving-results)
  - [x] with [Python](https://github.com/nrnb/gsod2019_kozo_nishida/blob/master/ipynb/Python/saving_results.ipynb) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/23)
  - [x] with [R](http://nrnb.org/gsod2019_kozo_nishida/html_documents/Rmd/saving-results.html) , [link to the commits](https://github.com/nrnb/gsod2019_kozo_nishida/issues/9)

## There is still work to be done...

- We prioritize the creation of notebooks using RCy3. Python notebooks with py2cytoscape are still almost untouched.
- Python notebooks doesn't require natural language writing ability (Because the text is the same as that of RCy3), but we may need to add the missing functions in py2cytoscape.

### Issue list (What is missing in CyREST, py2cytoscape, and Cytoscape Apps (stringApp etc.)

- [ ] CyREST does not yet support the merge network function
- [ ] py2cytoscape does not yet have RCy3's `selectNodes` equivalent https://github.com/cytoscape/py2cytoscape/issues/97
- [ ] [stringApp](http://apps.cytoscape.org/apps/stringapp) `retrieve enrichment` command does not yet support `Apps -> STRING Enrichment -> Retrieve functional enrichment` equivalent
- [ ] [clusterMaker2](http://apps.cytoscape.org/apps/clustermaker2) doesn't have a document about Commands https://github.com/RBVI/clusterMaker2/issues/11
- [ ] [CyNDEx-2](http://apps.cytoscape.org/apps/cyndex2) app has not implemented CyCommands.
- [ ] [PSICQUIC Web Service Client](https://apps.cytoscape.org/apps/psicquicwebserviceclient) app has not implemented CyCommands.
- [ ] CyCommand or CyREST do not have a function to get the currently applied **Style**.

## Technical writer and mentors
### Writer
- https://github.com/kozo2
### Mentors
- https://github.com/AlexanderPico
- https://github.com/khanspers

# About my achievements during Season of Docs

https://github.com/nrnb/gsod2019_kozo_nishida/wiki/My-achievements-during-Season-of-Docs-(Q-and-A-style)
