"""
# Installation

```
conda install -c conda-forge py2cytoscape
pip install -U handout
```

## Prerequisites
In addition to the RCy3 package, you will need the latest version of Cytoscape, which can be downloaded from http://www.cytoscape.org/download.php. Simply follow the installation instructions on screen.

## Getting started
First, launch Cytoscape and keep it running whenever using py2cytoscape. Confirm that you have everything installed and running:
"""

import handout
doc = handout.Handout('html_documents/py/differentially-expressed-genes')

import io
from contextlib import redirect_stdout

from py2cytoscape import cyrest
HOST = "localhost"
cytoscape=cyrest.cyclient(host=HOST)
f = io.StringIO()
with redirect_stdout(f):
    cytoscape.status()
    cytoscape.version()
s = f.getvalue()
doc.add_text(s)
doc.show()

"""
# Differentially Expressed Genes Network Analysis

This protocol describes a network analysis workflow in Cytoscape for a set of differentially expressed genes. Points covered:

- Retrieving relevant networks from public databases
- Network functional enrichment analysis
- Integration and visualization of experimental data
- Exporting network visualizations
"""