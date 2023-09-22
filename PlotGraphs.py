import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# AGE VS CAM ICU SCATTER GRAPH
df = pd.read_csv('C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\analysisNoArraysWithoutShortCases.csv')
dfWholeCohort = pd.read_csv('C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\analysisNoArrays.csv')

dfOnlyGreaterThan12Hours = pd.read_csv('C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\analysisNew.csv')


dfOnlyCamICUPos = df.drop(df[df['Has CAM-ICU +ve'] == 0].index)
plt.scatter(df['Age'], df['Days CAM ICU +ve'])
plt.xlabel("Age")
plt.ylabel("Days CAM ICU +VE")
# noinspection PyTupleAssignmentBalance
a, b = np.polyfit(np.array(df['Age']), np.array(df['Days CAM ICU +ve']), 1)
plt.plot(df['Age'], a * df['Age'] + b)
plt.show()

plt.scatter(df['Age'], df['Days Nursing Notes delirium +ve nighttime'])
plt.xlabel("Age")
plt.ylabel("Days Nursing Notes Nighttitme +VE")
# noinspection PyTupleAssignmentBalance
a, b = np.polyfit(np.array(df['Age']), np.array(df['Days Nursing Notes delirium +ve nighttime']), 1)
plt.plot(df['Age'], a * df['Age'] + b)
plt.show()

plt.scatter(df['Age'], df['Days Nursing Notes delirium +ve daytime'])
plt.xlabel("Age")
plt.ylabel("Days Nursing Notes Nighttitme +VE")
# noinspection PyTupleAssignmentBalance
a, b = np.polyfit(np.array(df['Age']), np.array(df['Days Nursing Notes delirium +ve daytime']), 1)
plt.plot(df['Age'], a * df['Age'] + b)
plt.show()



# PIE CHARTS
# 1) Mental Illness in CAM ICU +ve cohort
dfbinary = df.replace(to_replace=['No', 'Yes'], value=[0, 1])
y = dfbinary['Mental Illness?']
no = 0
yes = 0
for i in y:
    if i == 0:
        no += 1
    else:
        yes += 1
plt.pie([no, yes])
plt.show()

# 2)


