#!/usr/bin/env python

import os
import numpy as np
import pandas as pd

os.getcwd()

# Request for the filename
# Current version of this script works only with TSV type files
mainFilename = input('Input your file name (diabetes.tab.txt or housing.data.txt): ')
print()

# To create proper dataframe, transforming it with numpy
# Then changing it with pandas
filenameData = np.genfromtxt(mainFilename, dtype='str')

filenameData = pd.DataFrame(filenameData)

# Obtains first row to identify header is string or numeric
headers = filenameData.iloc[0]

try:
    pd.to_numeric(headers)
except:
    filenameData = pd.DataFrame(filenameData.values[1:], columns=headers)

# Changes strings to numbers (self identifies for float or integer)
filenameData = filenameData.apply(pd.to_numeric)

# Obtains the mean and standard deviation of the columns
listMean = filenameData.mean()
listStd = filenameData.std()

print(filenameData)

# Prints out the results
print('Mean for each column:')
for idx in filenameData.columns:
    print(idx,':',listMean[idx])

print()
print('Standard deviation for each column:')
for idx in filenameData.columns:
    print(idx,':',listStd[idx])
