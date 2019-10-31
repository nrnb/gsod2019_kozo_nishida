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
doc = handout.Handout('html_documents/py/stringApp')

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
# Cytoscape StringApp

In these exercises, we will use the [stringApp](http://apps.cytoscape.org/apps/stringApp) for [Cytoscape](http://cytoscape.org/) to retrieve molecular networks from the [STRING](https://string-db.org/) and [STITCH](http://stitch-db.org/) databases. The exercises will teach you how to:

- retrieve networks for proteins or small-molecule compounds of interest
- retrieve networks for a disease or an arbitrary topics in PubMed
- layout and visually style the resulting networks
- import external data and map them onto a network
- perform enrichment analyses and visualize the results
- merge and compare networks
- select proteins by attributes
- identify functional modules through network clustering

The original version of this tutorial was developed by Lars Juhl Jensen of the Novo Nordisk Center for Protein Research at the University of Copenhagen. We thank professor Jensen for his gracious willingness to allow us to repackage the content for delivery as a Cytoscape tutorial.

"""