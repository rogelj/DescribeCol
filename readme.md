# DescribeCol

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

