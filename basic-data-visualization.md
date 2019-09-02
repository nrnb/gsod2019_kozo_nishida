
# Basic Data Visualization

**Cytoscape is an open source software platform for integrating, visualizing, and analyzing measurement data in the context of networks.**

This tutorial presents a scenario of how expression and network data can be combined to tell a biological story and includes these concepts:
- Visualizing networks using expression data.
- Filtering networks based on expression data.
- Assessing expression data in the context of a biological network.

# Loading Network

- To get started,
  - install py2cytoscape with running

      ```shell
      conda install -c conda-forge py2cytoscape
      ```
  - install and launch the latest version of [Cytoscape](http://www.cytoscape.org/).
- Download the [demo network session file](http://nrnb.org/data/BasicDataVizDemo.cys).
- Open the demo network using


```python
from py2cytoscape import cyrest
cytoscape=cyrest.cyclient()
cytoscape.session.open(session_file="/Users/knishida/Documents/GitHub/gsod2019_kozo_nishida/BasicDataVizDemo.cys")
```

- To see node labels


```python
# NOT YET IMPLEMENTED
```

The network will open with the default style, similar to
![](https://cytoscape.org/cytoscape-tutorials/protocols/basic-data-visualization/BasicDataVizDemoLoaded.png)

# Visualizing Expression Data on Networks

Probably the most common use of expression data in Cytoscape is to set the visual properties of the nodes (color, shape, border) in a network according to expression data. This creates a powerful visualization, portraying functional relation and experimental response at the same time. Here, we will show an example of doing this.

The data used in this example is from yeast, and represents an experiment of perturbations of the genes **Gal1**, **Gal4**, and **Gal80**, which are all yeast transcription factors.

For this tutorial, the experimental data was part of the Cytoscape session file you loaded earlier, and is visible in the Node Table:


```python
cytoscape.table.getTable(columns=['COMMON', 'gal1RGexp', 'gal4RGexp', 'gal80Rexp', 'gal1RGsig', 'gal4RGsig', 'gal80Rsig'], table='node')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>COMMON</th>
      <th>gal1RGexp</th>
      <th>gal4RGexp</th>
      <th>gal80Rexp</th>
      <th>gal1RGsig</th>
      <th>gal4RGsig</th>
      <th>gal80Rsig</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>YKR026C</td>
      <td>GCN3</td>
      <td>-0.154</td>
      <td>-0.501</td>
      <td>0.292</td>
      <td>0.000912</td>
      <td>3.569200e-06</td>
      <td>0.011229</td>
    </tr>
    <tr>
      <td>YGL122C</td>
      <td>NAB2</td>
      <td>0.174</td>
      <td>0.020</td>
      <td>0.187</td>
      <td>0.000873</td>
      <td>6.170700e-01</td>
      <td>0.005997</td>
    </tr>
    <tr>
      <td>YMR146C</td>
      <td>TIF34</td>
      <td>-0.050</td>
      <td>-0.143</td>
      <td>-0.151</td>
      <td>0.308440</td>
      <td>8.517300e-03</td>
      <td>0.072007</td>
    </tr>
    <tr>
      <td>YDR429C</td>
      <td>TIF35</td>
      <td>0.078</td>
      <td>-0.209</td>
      <td>0.354</td>
      <td>0.072655</td>
      <td>1.172400e-03</td>
      <td>0.000017</td>
    </tr>
    <tr>
      <td>YFL017C</td>
      <td>GNA1</td>
      <td>0.131</td>
      <td>0.122</td>
      <td>0.124</td>
      <td>0.001785</td>
      <td>5.530200e-03</td>
      <td>0.050323</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>YBR045C</td>
      <td>GIP1</td>
      <td>0.786</td>
      <td>1.022</td>
      <td>0.940</td>
      <td>0.000006</td>
      <td>1.294500e-05</td>
      <td>0.016389</td>
    </tr>
    <tr>
      <td>YER054C</td>
      <td>GIP2</td>
      <td>0.057</td>
      <td>0.206</td>
      <td>0.247</td>
      <td>0.169580</td>
      <td>6.203200e-04</td>
      <td>0.004360</td>
    </tr>
    <tr>
      <td>YPR145W</td>
      <td>ASN1</td>
      <td>-0.195</td>
      <td>-0.614</td>
      <td>-0.232</td>
      <td>0.000032</td>
      <td>1.152500e-07</td>
      <td>0.001187</td>
    </tr>
    <tr>
      <td>YDR277C</td>
      <td>MTH1</td>
      <td>0.243</td>
      <td>0.192</td>
      <td>0.448</td>
      <td>0.000022</td>
      <td>2.804400e-02</td>
      <td>0.000573</td>
    </tr>
    <tr>
      <td>YDL194W</td>
      <td>SNF3</td>
      <td>0.139</td>
      <td>0.333</td>
      <td>0.449</td>
      <td>0.018043</td>
      <td>3.396100e-02</td>
      <td>0.011348</td>
    </tr>
  </tbody>
</table>
<p>249 rows × 7 columns</p>
</div>



You can select nodes in the current network based on node names provided by a file.



```python
!cat node_names.txt
```

    YIL143C
    YNL036W



```python
cytoscape.node.select_from_file(afile="./node_names.txt")
```


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-5-3b06a5138042> in <module>
    ----> 1 cytoscape.node.select_from_file(afile="./node_names.txt")
    

    ~/miniconda3/lib/python3.7/site-packages/py2cytoscape/cyrest/node.py in select_from_file(self, afile, verbose)
        222         :param verbose: print more
        223         """
    --> 224         network=check_network(self,network,verbose=verbose)
        225         PARAMS=set_param(["file"],[afile])
        226         response=api(url=self.__url+"/select from file", PARAMS=PARAMS, method="POST", verbose=verbose)


    UnboundLocalError: local variable 'network' referenced before assignment


- Selecting one or more nodes in the network will update the Node Table to show only the corresponding row(s).

We can now use the data to manipulate the visual properties of the network by mapping specific data columns to visual style properties:

- The **gal80Rexp** expression values will be mapped to node color; nodes with low expression will be colored blue, nodes with high expression will be colored red.
- Significance for expression values will be mapped to Node Border Width, so nodes with significant changes will appear with a thicker border.


```python

```
