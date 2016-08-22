'''
DescribeCol is a function that facilitates data quality testing. It is a basic function that takes information form a pandas dataframe and based on the type of the data it provides information such as:

- data description
- data visualisation
- data examples

USAGE:

describecol(df, n)

df - pandas DataFrame
n - index for the column to be described
'''
import matplotlib.pyplot as plt
import pandas as pd

def describecol(df,n=0):
    colnames = list(df.columns)
    print('The name of the column is {0}\n\n'.format(colnames[n]))

    print('DESCRIPTION\n')
    print (df[colnames[n]].describe())

    print('\n\n')

    print(df[colnames[n:n+1]].head())

    if (df[colnames[n]].dtype.name == 'object') or \
    (df[colnames[n]].dtype.name == 'category'):
        group1 = df.groupby(colnames[n]).size().sort_values(ascending=False)
        print('\n\n TOP ENTRIES\n')
        print(group1.head(20))

        if len(group1)<16:
            df[colnames[n]].value_counts().plot(kind='bar', figsize=(10,6),
                                                title=colnames[n], fontsize=12)
            plt.show()
    elif (df[colnames[n]].dtype.name == 'float64') or \
    (df[colnames[n]].dtype.name == 'int64'):
        fig1, ax1 = plt.subplots(1,1)
        df[colnames[n]].plot.hist(title=colnames[n], figsize=(10,6),
                                  fontsize=12, ax=ax1)
        plt.show()

        fig2, ax2 =plt.subplots(1,1);
        df[colnames[n]].plot.box(title=colnames[n], figsize=(10,6), fontsize=12,
                                ax=ax2)
        plt.show()
    else:
        print(df[colnames[n]].dtype)

if __name__ == "__main__":
    d = {'one' : [1., 2., 3., 4., 5.],
    'two' : ['red', 'green', 'green', 'red', 'red']}
    df = pd.DataFrame(d)

    cols = list(df.columns)

    for n in range(0,len(df.columns)):
        describecol(df,n)
