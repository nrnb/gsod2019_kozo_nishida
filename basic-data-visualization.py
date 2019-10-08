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
doc = handout.Handout('html_documents/py/basic-data-visualization')

import io
from contextlib import redirect_stdout

from py2cytoscape import cyrest
cytoscape=cyrest.cyclient()
f = io.StringIO()
with redirect_stdout(f):
    cytoscape.status()
s = f.getvalue()
doc.add_text(s)
doc.show()

"""
# Basic Data Visualization

**Cytoscape is an open source software platform for integrating, visualizing, and analyzing measurement data in the context of networks.**

This tutorial presents a scenario of how expression and network data can be combined to tell a biological story and includes these concepts:

 - Visualizing networks using expression data.
 - Filtering networks based on expression data.
 - Assessing expression data in the context of a biological network.

## Loading Network
You can download the [demo network session file](https://nrnb.org/data/BasicDataVizDemo.cys) to your current working directory by running...
"""

print('foo1')

"""
Now open the demo network using...
"""

print('foo2')

"""
Now you should see a network like this.
"""

print('foo3')

"""
## Visualizing Expression Data on Networks

Probably the most common use of expression data in Cytoscape is to set the **visual properties** of the nodes (color, shape, border) in a network according to expression data. This creates a powerful visualization, portraying functional relation and experimental response at the same time. Here, we will show an example of doing this.

The data used in this example is from yeast, and represents an experiment of perturbations of the genes **Gal1**, **Gal4**, and **Gal80**, which are all yeast transcription factors.

For this tutorial, the experimental data was part of the Cytoscape session file you loaded earlier, and is visible in the Node Table:

![](https://cytoscape.org/cytoscape-tutorials/protocols/basic-data-visualization/Galbrowse3.png)
"""

print('foo4')

"""
- You can select nodes in the network by 
"""

print('foo5')

"""
- Selecting one or more nodes in the network will update the Node Table to show only the corresponding row(s).

`FILL PNG LINK HERE`

We can now use the data to manipulate the visual properties of the network by mapping specific data columns to visual style properties:

- The **gal80Rexp** expression values will be mapped to node color; nodes with low expression will be colored blue, nodes with high expression will be colored red.
- Significance for expression values will be mapped to Node Border Width, so nodes with significant changes will appear with a thicker border.

### Set Node Fill Color

- Click on the **Style** tab in the Control Panel. And you can set node fill color by
"""

print('foo6')

"""
- This produces an initial gradient ranging from blue to red for expression values. Notice that the nodes in the network change color.

`FILL PNG LINK HERE`

### Set Default Node Color

Some nodes in the network don't have any data, and for those nodes, the default color applies. In our case, the default color is blue, which falls within the spectrum of our blue-red gradient. This is not ideal for data visualization, so a useful trick is to choose a color outside the gradient spectrum to distinguish nodes with no defined expression value.

- Still in the **Style** tab, And you can set default node color to dark gray by
"""

print('foo7')

"""
`FILL PNG LINK HERE`

### Set Node Border Width

You can set the Border Width by
"""

# Invisible below:
value = 13  # handout: exclude

"""
This defines the node border width over the range of `gal80Rsig` column p-values like

`FILL PNG LINK HERE`

### Creating a Legend

## Layouts
An important aspect of network visualization is the layout, meaning the positioning of nodes and edges. Our network had a preset layout in the original file you imported, but this can be changed.

- Let's change the layout to **Degree Sorted Circle Layout** by 
"""

"""
Cytoscape supports many different layout algorithms, described in detail in the [Cytoscape manual](http://manual.cytoscape.org/en/stable/Navigation_and_Layout.html?highlight=layout#automatic-layout-algorithms).

## Select Nodes

Cytoscape allows you to easily filter and select nodes and edges based on data attributes. Next, we will select a subset of nodes with high expression in the gal80 knockout:

### Expand Selection and Create New Network

## Saving Results
"""