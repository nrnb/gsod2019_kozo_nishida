# Basic Data Visualization

**Cytoscape is an open source software platform for integrating, visualizing, and analyzing measurement data in the context of networks.**

This tutorial presents a scenario of how expression and network data can be combined to tell a biological story and includes these concepts:

- Visualizing networks using expression data.
- Filtering networks based on expression data.
- Assessing expression data in the context of a biological network.

## Prerequisites
FILLME. How can we combine the prerequisites instruction of RCy3 and py4cytoscape here? Should it be separeted to the other pages?

## Getting started
First, launch Cytoscape and keep it running whenever using RCy3 or py4cytoscape. Confirm that you have everything installed and running:

````{tabbed} r
```{code-block} r
cytoscapePing()
cytoscapeVersionInfo()
```
````

````{tabbed} python
```{code-block} python
cytoscape_ping()
cytoscape_version_info()
```
````

## Loading Network

You can download the [demo network session file](https://nrnb.org/data/BasicDataVizDemo.cys) to your current working directory by running...

````{tabbed} r
```{code-block} r
download.file("https://nrnb.org/data/BasicDataVizDemo.cys", "./BasicDataVizDemo.cys", 'curl')
```
````

````{tabbed} python
```{code-block} python
# Below is the IPython magic command, not the Python code, but this is the easiest.
# !curl -O https://nrnb.org/data/BasicDataVizDemo.cys
```
````

Now open the demo network using...

````{tabbed} r
```{code-block} r
openSession(file.location = "./BasicDataVizDemo.cys")
```
````

````{tabbed} python
```{code-block} python
open_session(file_location="BasicDataVizDemo.cys")
```
````

Now you should see a network like this.

![](../images/BasicDataVizDemo.png)

## Visualizing Expression Data on Networks

Probably the most common use of expression data in Cytoscape is to set the **visual properties** of the nodes (color, shape, border) in a network according to expression data.
This creates a powerful visualization, portraying functional relation and experimental response at the same time.
Here, we will show an example of doing this.

The data used in this example is from yeast, and represents an experiment of perturbations of the genes **Gal1**, **Gal4**, and **Gal80**, which are all yeast transcription factors.

For this tutorial, the experimental data was part of the Cytoscape session file you loaded earlier, and is visible in the Node Table:

![](../images/Galbrowse3.png)

- You can select nodes in the network by 

````{tabbed} r
```{code-block} r
selectNodes(c("YDL194W", "YLR345W"), by.col = "name")
```
````

````{tabbed} python
```{code-block} python
select_nodes(['YDL194W', 'YLR345W'], by_col='name')
```
````

- Selecting one or more nodes in the network will update the Node Table to show only the corresponding row(s).

![](../images/SelectNodes.png)

We can now use the data to manipulate the visual properties of the network by mapping specific data columns to visual style properties:

- The **gal80Rexp** expression values will be mapped to node color; nodes with low expression will be colored blue, nodes with high expression will be colored red.
- Significance for expression values will be mapped to Node Border Width, so nodes with significant changes will appear with a thicker border.

### Set Node Fill Color

Let's specify the node fill color as a gradient ranging from blue to red for expression values using a continuous mapping for the 'gal80Rexp' column:

````{tabbed} r
```{code-block} r
gal80Rexp.score.table <- getTableColumns('node','gal80Rexp')
gal80Rexp.min <- min(gal80Rexp.score.table, na.rm = T)
gal80Rexp.max <- max(gal80Rexp.score.table, na.rm = T)
gal80Rexp.center <- gal80Rexp.min + (gal80Rexp.max - gal80Rexp.min)/2
setNodeColorMapping('gal80Rexp', c(gal80Rexp.min, gal80Rexp.center, gal80Rexp.max), c('#0000FF', '#FFFFFF', '#FF0000'))
```
````

````{tabbed} python
```{code-block} python
gal80Rexp_score_table = get_table_columns(table='node', columns='gal80Rexp')
gal80Rexp_min = gal80Rexp_score_table.min().values[0]
gal80Rexp_max = gal80Rexp_score_table.max().values[0]
gal80Rexp_center = gal80Rexp_min + (gal80Rexp_max - gal80Rexp_min)/2
set_node_color_mapping('gal80Rexp', [gal80Rexp_min, gal80Rexp_center, gal80Rexp_max], ['#0000FF', '#FFFFFF', '#FF0000'])
```
````

- This produces an initial gradient ranging from blue to red for expression values. Notice that the nodes in the network change color.

![](../images/SetNodeFillColor.png)

### Set Default Node Color

Some nodes in the network don't have any data, and for those nodes, the default color applies.
In our case, the default color is blue, which falls within the spectrum of our blue-red gradient.
This is not ideal for data visualization, so a useful trick is to choose a color outside the gradient spectrum to distinguish nodes with no defined expression value.

We can set default node color to dark gray color:

````{tabbed} r
```{code-block} r
setNodeColorDefault('#666666')
```
````

````{tabbed} python
```{code-block} python
set_node_color_default('#666666')
```
````

![](../images/SetDefaultNodeColor.png)

### Set Node Border Width

To visualize the significance of measurements, let's add a contiuous mapping for 'gal80Rsig' p-values to Node Border Width:

````{tabbed} r
```{code-block} r
gal80Rsig.score.table <- getTableColumns('node','gal80Rsig')
gal80Rsig.min <- min(gal80Rsig.score.table, na.rm = T)
gal80Rsig.max <- max(gal80Rsig.score.table, na.rm = T)
setNodeBorderWidthMapping('gal80Rsig', c(gal80Rsig.min, gal80Rsig.max), c(10,30))
```
````

````{tabbed} python
```{code-block} python
gal80Rsig_score_table = get_table_columns(table='node', columns='gal80Rsig')
gal80Rsig_min = gal80Rsig_score_table.min().values[0]
gal80Rsig_max = gal80Rsig_score_table.max().values[0]
set_node_border_width_mapping('gal80Rsig', table_column_values=[gal80Rsig_min, gal80Rsig_max], widths=[10, 30])
```
````

This creates the following mapping for `gal80Rsig`:
![](../images/SetNodeBorderWidth.png)

## Layouts
An important aspect of network visualization is the layout, meaning the positioning of nodes and edges.
Our network had a preset layout in the original file you imported, but this can be changed.

- Let's change the layout to **Degree Sorted Circle Layout**:

````{tabbed} r
```{code-block} r
layoutNetwork("degree-circle")
```
````

````{tabbed} python
```{code-block} python
layout_network('degree-circle')
```
````

![](../images/degree-circle.png)

In this layout, nodes are sorted by degree (connectedness), with the highest degree node at the 6 o'clock position, and remaining nodes are sorted counter clock-wise based on decreasing degree.

For this network, a degree-sorted circle layout may not be the most effective.
Instead, let's try a force-directed layout instead, which may work better with this network.

````{tabbed} r
```{code-block} r
layoutNetwork("force-directed")
```
````

````{tabbed} python
```{code-block} python
layout_network('force-directed')
```
````

![](../images/force-directed.png)

Cytoscape supports many different layout algorithms, described in detail in the [Cytoscape manual](http://manual.cytoscape.org/en/stable/Navigation_and_Layout.html?highlight=layout#automatic-layout-algorithms).

## Select Nodes

Cytoscape allows you to easily filter and select nodes and edges based on data attributes.
Next, we will select a subset of nodes with high expression in the gal80 knockout:

Let's select a subset of nodes with high expression in the gal80 knockout: 

````{tabbed} r
```{code-block} r
createColumnFilter('myFilter', 'gal80Rexp', 2.00, "GREATER_THAN")
```
````

````{tabbed} python
```{code-block} python
create_column_filter('myFilter', 'gal80Rexp', 2.00, "GREATER_THAN")
```
````

You should now see only a few nodes in the network selected (highlighted yellow).

![](../images/column-filter.png)

### Expand Selection and Create New Network

We have now selected only the few top expressing nodes.
To see the context of these nodes in the larger network, we can expand the selection of nodes to include the nodes connecting to the selected nodes, i.e. the first neighbors.
Once we have that larger selection, we can create a new network.

Select the first neighbors of selected nodes:

````{tabbed} r
```{code-block} r
selectFirstNeighbors()
```
````

````{tabbed} python
```{code-block} python
select_first_neighbors()
```
````

![](../images/first-neighbors.png)

Digging into the biology of this network, it turns out that GAL4 is repressed by GAL80.
Both nodes (GAL4 and GAL11) show fairly small changes in expression, and neither change is statistically significant: they are pale blue with thin borders.
These slight changes in expression suggest that the critical change affecting the red nodes might be somewhere else in the network, and not either of these nodes.
GAL4 interacts with GAL80, which shows a significant level of repression: it is medium blue with a thicker border.

Note that while GAL80 shows evidence of significant repression, most nodes interacting with GAL4 show significant levels of induction: they are rendered as red rectangles.
GAL11 is a general transcription co-factor with many interactions.

Putting all of this together, we see that the ***transcriptional activation activity of Gal4 is repressed by Gal80***.
So, repression of Gal80 increases the transcriptional activation activity of Gal4.
Even though the expression of Gal4 itself did not change much, ***the Gal4 transcripts were much more likely to be active transcription factors when Gal80 was repressed***.
This explains why there is so much up-regulation in the vicinity of Gal4.

## Summary

In summary, we have:

- Explored a yeast interactome from a transcription factor knockout experiment
- Created a visual style using expression value as node color and with border width mapped to significance
- Selected high expressing genes and their neighbors and created a new network

Finally, we can now export this network as a publication-quality image....

## Saving Results

Cytoscape provides a number of ways to save results and visualizations:

- As a session:

````{tabbed} r
```{code-block} r
saveSession('./basic-data-visualization.cys')
```
````

````{tabbed} python
```{code-block} python
save_session('basic-data-visualization.cys')
```
````

- As an image:

````{tabbed} r
```{code-block} r
exportImage('./basic-data-visualization', 'PDF')
exportImage('./basic-data-visualization', 'PNG')
exportImage('./basic-data-visualization', 'JPEG')
exportImage('./basic-data-visualization', 'SVG')
exportImage('./basic-data-visualization', 'PS')
```
````

````{tabbed} python
```{code-block} python
export_image('basic-data-visualization', type='PDF')
export_image('basic-data-visualization', type='PNG')
export_image('basic-data-visualization', type='JPEG')
export_image('basic-data-visualization', type='SVG')
export_image('basic-data-visualization', type='PS')
```
````

- To a public repository:

````{tabbed} r
```{code-block} r
exportNetworkToNDEx("user", "pass", TRUE)
```
````

````{tabbed} python
```{code-block} python
export_network_to_ndex('userid', 'password', True)
```
````

- As a graph format file (Formats: "CX JSON", "Cytoscape.js JSON", "GraphML", "XGMML", "SIF",...):

````{tabbed} r
```{code-block} r
exportNetwork('./basic-data-visualization', 'CX')
exportNetwork('./basic-data-visualization', 'cyjs')
exportNetwork('./basic-data-visualization', 'graphML')
exportNetwork('./basic-data-visualization', 'xGMML')
exportNetwork('./basic-data-visualization', 'SIF')
```
````

````{tabbed} python
```{code-block} python
export_network('basic-data-visualization', 'CX')
export_network('basic-data-visualization', 'cyjs')
export_network('basic-data-visualization', 'graphML')
export_network('basic-data-visualization', 'xGMML')
export_network('basic-data-visualization', 'SIF')
```
````
