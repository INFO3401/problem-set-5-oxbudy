import pandas as pd
import numpy as np

#4
def correctDateFormat(dataframe, colname):
    melted = pd.melt(dataframe, id_vars=['Country/Region'],
    value_vars=list(dataframe.columns[4:]),
    var_name='Date', value_name=colname)
    #6
    melted['Date'] = pd.to_datetime(melted['Date'], infer_datetime_format=True)
    #print(melted['Date'].dtypes)
    return melted

#14
def aggregateCountry(dataframe, col, country):
    dataframe.groupby([country]).sum()

#def topCorrelations(dataframe, col, num):
#    np.corrcoef()
