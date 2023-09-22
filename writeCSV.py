import csv
import re

import pandas

file = pandas.read_csv('C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\completeSheet.csv', index_col='Patient MRN')

ndd = file['Days Nursing Notes delirium +ve daytime']
ndn = file['Days Nursing Notes delirium +ve nighttime']

globalAoSD = 0
globalDD = 0
globalHD = 0

nursingDeliriumList = {}
newList = []

pattern = re.compile(r'(\d+\s=\s(\w*, \w*)+)')
# 8 = D, A 9 = FC, A, AoS 10 = D, A
for s in ndd:
    newString = s.partition('//')[2]

    if len(newString) > 1:
        newList.append(pattern.split(newString))

for list in newList:
    for i in list:
        if i == '':
            list.remove(i)

for list in newList:
    for string in list:
        if not string[0].isdigit():
            list.remove(string)

for list in newList:
    for string in list:
        if string == ' ':
            list.remove(string)

print('final:' + str(newList))

globalAoS = []
globalFC = []
globalA = []
globalAg = []
globalH = []
globalUI = []
globalD = []
globalDe = []

for list in newList:
    days = 0

    AoS = 0
    FC = 0
    A = 0
    Ag = 0
    H = 0
    UI = 0
    D = 0
    De = 0

    for s in list:
        days += 1
        if 'AoS' in s:
            AoS += 1
        if 'FC' in s:
            FC += 1
        if re.search("(A[^go]) |( A$)", s):
            A += 1
        if 'Ag' in s:
            Ag += 1
        if 'H' in s:
            H += 1
        if 'UI' in s:
            UI += 1
        if 'De' in s:
            De += 1
        if re.search("(D[^e] |( D$))", s):
            D += 1

        globalAoS.append(AoS/days)
        globalFC.append(FC/days)
        globalA.append(A/days)
        globalAg.append(Ag/days)
        globalH.append(H/days)
        globalUI.append(De/days)
        globalD.append(D/days)


def average_value(values):
    if len(values) != 0:
        temp = 0
        for i in values:
            temp += i
        return temp / len(values)
    return 0

print('Average days AoS' + str(average_value(globalAoS)))
print('Avg FC' + str(average_value(globalFC)))
print('Avg D' + str(average_value(globalD)))
print('Avg H' + str(average_value(globalH)))
print('Avg De' + str(average_value(globalDe)))
print('Avg A ' + str(average_value(globalA)))
print('Avg Ag ' + str(average_value(globalAg)))
print('Avg UI ' + str(average_value(globalUI)))

print('====================================================================')
print('====================================================================')
print('====================================================================')
print('====================================================================')
print('====================================================================')


pattern = re.compile(r'(\d+\s=\s(\w*, \w*)+)')
# 8 = D, A 9 = FC, A, AoS 10 = D, A
for s in ndn:
    newString = s.partition('//')[2]

    if len(newString) > 1:
        newList.append(pattern.split(newString))

for list in newList:
    for i in list:
        if i == '':
            list.remove(i)

for list in newList:
    for string in list:
        if not string[0].isdigit():
            list.remove(string)

for list in newList:
    for string in list:
        if string == ' ':
            list.remove(string)


globalAoS = []
globalFC = []
globalA = []
globalAg = []
globalH = []
globalUI = []
globalD = []
globalDe = []


for list in newList:
    days = 0

    AoS = 0
    FC = 0
    A = 0
    Ag = 0
    H = 0
    UI = 0
    D = 0
    De = 0

    for s in list:
        days += 1
        if 'AoS' in s:
            AoS += 1
        if 'FC' in s:
            FC += 1
        if re.search("(A[^go]) |( A$)", s):
            A += 1
        if 'Ag' in s:
            Ag += 1
        if 'H' in s:
            H += 1
        if 'UI' in s:
            UI += 1
        if 'De' in s:
            De += 1
        if re.search("(D[^e] |( D$))", s):
            D += 1


        globalAoS.append(AoS/days)
        globalFC.append(FC/days)
        globalA.append(A/days)
        globalAg.append(Ag/days)
        globalH.append(H/days)
        globalUI.append(De/days)
        globalD.append(D/days)


def average_value(values):
    if len(values) != 0:
        temp = 0
        for i in values:
            temp += i
        return temp / len(values)
    return 0

print('Average days AoS' + str(average_value(globalAoS)))
print('Avg FC' + str(average_value(globalFC)))
print('Avg D' + str(average_value(globalD)))
print('Avg H' + str(average_value(globalH)))
print('Avg De' + str(average_value(globalDe)))
print('Avg A ' + str(average_value(globalA)))
print('Avg Ag ' + str(average_value(globalAg)))
print('Avg UI ' + str(average_value(globalUI)))

f = open('C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\nursingDelirium.csv', 'w')
writer = csv.writer(f)
