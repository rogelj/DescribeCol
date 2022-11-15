# DescribeCol

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.x-orange)](https://www.python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Twitter](https://img.shields.io/badge/twitter-quantum__tunnel-blue)](http://twitter.com/quantum_tunnel)
[![BioSite](https://img.shields.io/badge/BioSite-jrogel-blue)](https://bio.site/jrogel)
[![Website](https://img.shields.io/badge/web-jrogel-black)](https://jrogel.com)
[![Website](https://img.shields.io/badge/web-RogueLoop-black)](https://rogueloop.jrogel.com)

DescribeCol is a function that facilitates data quality testing. It is a basic function that takes information form a pandas dataframe and based on the type of the data it provides information such as:

- data description
- data visualisation
- data examples

## USAGE

`describecol(df, n)`

`df` - pandas DataFrame
`n` - index for the column to be described



**Example**:

```python
import pandas as pd
import describecol as dc

d = {'one': [1., 2., 3., 4., 5.],
     'two': ['red', 'green', 'green', 'red', 'red']}
df = pd.DataFrame(d)
cols = list(df.columns)

for n in range(0, len(df.columns)):
    dc.describecol(df, n)
   
```

