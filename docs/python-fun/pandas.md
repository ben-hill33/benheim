# [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)

If you thought this is where you were gonna get dumplings and kung-fu, you were mistaken! Your kung fu is weak! First you must master DATAFRAMES!!!

What's a dataframe..?

A dataframe is a word mash-up of for data (analysis) framework. Pandas specifically is a software library written for Python for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series. The name is derived from "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals. - thanks [wikipedia!](https://en.wikipedia.org/wiki/Pandas_(software)#:~:text=In%20computer%20programming%2C%20pandas%20is,the%20three%2Dclause%20BSD%20license.)

There are several ways to create a Pandas dataframe.
- In most cases, you'll use the [DataFrame constructor](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) and provide the data, labels, and other info
- You can pass the data as a 2D list, tuple, dictionary, NumPy array, or Pandas Series instance.
- Just like NumPy has a standard identifier as np, Pandas does too. 
  - import pandas as **pd**
- Dictionary
  - If you create a dictionary using pandas, the keys are the DataFrames column labels, and the values are the data values in the corresponding DataFrame columns.
    - The values can be contained in a tuple, list, 1D NumPy array, Pandas Series object
- NumPy
  - You can pass a 2D numpy array to the dataframe constructor the same way you do a list
  - Sometimes you might want to extract data from a dataframe without its labels.
    - to do that, you can use either `.to_numpy()` or `.values`
    - `.to_numpy()` comes with two optional parameters
      - **dtype**: to specify the data type of the resulting array. It's set to `None` by default
      - **copy**: set to `False` if you want to use the original data from the dataframe. Set to `True` if you want to make a copy of the data


### Resources
- [Getting Started](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html)
- [Real Python - Pandas](https://realpython.com/learning-paths/pandas-data-science/)
- [Master Pandas](https://towardsdatascience.com/be-a-more-efficient-data-scientist-today-master-pandas-with-this-guide-ea362d27386)

[Table of Contents](../index.md)
