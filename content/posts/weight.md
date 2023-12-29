+++
title = 'Weight / Pressure Log'
date = 2023-12-18T10:40:19-06:00
draft = false
summary = 'A system for tracking weight and pressure' 
+++

## Weight

{{% weightmd %}}

{{< chart >}}
type: 'bar',
data: {
  labels: ['Tomato', 'Blueberry', 'Banana', 'Lime', 'Orange'],
  datasets: [{
    label: '# of votes',
    data: [12, 19, 3, 5, 3],
  }]
}
{{< /chart >}}

## BP

{{% bpmd %}}


## The Code

On this project I attemp to use the [_Unix Philosophy_](https://en.wikipedia.org/wiki/Unix_philosophy) and also only the [Python Standard Library](https://docs.python.org/3/library/index.html).  So at time of writing there are two separate modules for capturing weight (weight.py), and blood pressure / heart rate readings (bp.py).  Those record the data in simple .csv files.  A separate script (make_table.py) generates markdown tables for each of the .csv files.  Last, a script to copy the markdown tables to the appropriate Hugo directory where they are included in creation of the final page. [link here](http://www.davidgpohl.com/fake).



```python
{{% weightpy %}}
```

 