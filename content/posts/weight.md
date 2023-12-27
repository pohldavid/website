+++
title = 'Weight / Pressure Log'
date = 2023-12-18T10:40:19-06:00
draft = false
summary = 'A system for tracking weight and pressure' 
+++

## Weight

{{% weightmd %}}

## BP

{{% bpmd %}}


## The Code

On this project I attemp to use the _Unix Philosophy_ and also only the python standard library.  So at time of writing there are two separate modules for capturing weight (weight.py), and blood   pressure / heart rate readings (bp.py).  Those record the data in sumple .csv files.  A separate script (make_table.py) generates markdown tables for each of the csv files.  Last, a script to copy the markdown tables to the appropriate Hugo directory where they are included in creation of the final page.  [link here](http://www.davidgpohl.com/fake).


```python
{{% weightpy %}}
```

 