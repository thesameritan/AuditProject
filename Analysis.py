import json
import numpy as np
import pandas as pd
from datetime import datetime

from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy import stats

jsonPatientObjects = []

# data analysis for global COLLECTIONS
accuracyOfDeliriumDayTimeGlobal = []
accuracyOfDeliriumNightTimeGlobal = []
accuracyOfDeliriumNightTimeNursingGlobal = []
accuracyOfDeliriumDayTimeNursingGlobal = []
percentOfDaysDeliriumTreatedGlobal = []
patientAgesGlobal = []
lengthOfStayGlobal = []
lengthOfDeliriumGlobal = []
lengthOfStayIfDeliriumGlobal = []
deliriumPmhxGlobal = []
hoursOfRassGlobal = []
numberOfDeliriumNursingDayGlobal = []
numberOfDeliriumNursingNightGlobal = []
lengthOfRassInDeliriumGlobal = []


def average_value(values):
    temp = 0
    for i in values:
        temp += i
    return temp / len(values)


def toInt(list):
    newList = []
    for i in list:
        newList.append(int(i))
        return newList


with open('C:\\Users\\thesa\Desktop\\auditProject\\Audit\\PatientDataWithoutShortCases.json', 'r') as file:
    for line in file:

        jsonPatientObjects.append(json.loads(line))  # each patient
        patient = json.loads(line)

        # admission date/discharge date
        date_format = '%d/%m %H:%M'

        admission_date = datetime.strptime(patient['Date Admitted'], date_format)
        discharge_date = datetime.strptime(patient['Date Discharged'], date_format)
        lengthOfStay = discharge_date - admission_date

        lengthOfDelirium = len(patient['Days CAM ICU +ve'])

        if patient['Days Nursing Notes delirium +ve nighttime'][0] != '0':
            numberOfDeliriumNursingNightGlobal.append('1')

        if patient['Days Nursing Notes delirium +ve daytime'][0] != '0':
            numberOfDeliriumNursingDayGlobal.append('1')

        if patient['Days on meds'][0] != '0':
            percentOfDaysDeliriumTreated = \
                set(patient['Days CAM ICU +ve']) & set(patient['Days on meds'])

        if patient['Days CAM ICU +ve'][0] != 0:
            accuracyOfDeliriumDayTimeCAMICU = len(set(patient['Days CAM ICU +ve']) &
                                                  set(patient['Days Nursing Notes delirium +ve daytime'])) \
                                              / len(set(patient['Days CAM ICU +ve']))

            accuracyOfDeliriumNightTimeCAMICU = len(set(patient['Days CAM ICU +ve']) &
                                                    set(patient['Days Nursing Notes delirium +ve nighttime'])) \
                                                / len(set(patient['Days CAM ICU +ve']))

            accuracyOfDeliriumDayTimeNursing = len(set(patient['Days CAM ICU +ve']) &
                                                   set(patient['Days Nursing Notes delirium +ve daytime'])) \
                                               / len(set(patient['Days Nursing Notes delirium +ve daytime']))

            accuracyOfDeliriumNightTimeNursing = len(set(patient['Days CAM ICU +ve']) &
                                                     set(patient['Days Nursing Notes delirium +ve nighttime'])) \
                                                 / len(set(patient['Days Nursing Notes delirium +ve nighttime']))

            percentOfDaysDeliriumTreated = \
                len(set(patient['Days CAM ICU +ve']) & set(patient['Days on meds'])) / len(
                    set(patient['Days CAM ICU +ve']))

        hoursOfRass = int(patient['Hours of RAAS <= -3']) \
                      / (int(lengthOfStay.total_seconds() / 60 / 60))

        # add to global for analysis
        accuracyOfDeliriumNightTimeGlobal.append(accuracyOfDeliriumNightTimeCAMICU)
        accuracyOfDeliriumDayTimeGlobal.append(accuracyOfDeliriumDayTimeCAMICU)
        lengthOfStayGlobal.append(lengthOfStay.days)
        patientAgesGlobal.append(patient['Age'])
        hoursOfRassGlobal.append(hoursOfRass)

        if patient['Days CAM ICU +ve'][0] != '0':
            lengthOfRassInDeliriumGlobal.append(hoursOfRass)
            deliriumPmhxGlobal.append(patient['Patient Comorbidities'])
            lengthOfDeliriumGlobal.append(lengthOfDelirium)
            percentOfDaysDeliriumTreatedGlobal.append(percentOfDaysDeliriumTreated)
            lengthOfStayIfDeliriumGlobal.append(lengthOfStay.days)

        if patient['Days Nursing Notes delirium +ve nighttime'][0] != '0' or \
                patient['Days Nursing Notes delirium +ve daytime'][0] != 0:
            accuracyOfDeliriumDayTimeNursingGlobal.append(accuracyOfDeliriumDayTimeNursing)
            accuracyOfDeliriumNightTimeNursingGlobal.append(accuracyOfDeliriumNightTimeNursing)

    print('====================================================================')
    print('SAMPLE SIZE = ' + str(len(patientAgesGlobal)))
    print('====================================================================')
    print('Incidence of delirium via nursing notes at day: ' + str(len(numberOfDeliriumNursingDayGlobal)))
    print('Incidence of delirium via nursing notes at night: ' + str(len(numberOfDeliriumNursingNightGlobal)))
    print('Incidence of delirium via CAM-ICU: ' + str(len(lengthOfDeliriumGlobal)))
    print('Incidence of +ve CAM-ICU in critical care RHH: ' + str(len(lengthOfDeliriumGlobal) / len(patientAgesGlobal)))
    print('====================================================================')
    print('====================================================================')
    print('Average percent of RASS <= 3 in total patient stay: ' + str(average_value(hoursOfRassGlobal)))
    print('Average percent of RASS <= 3 in total patient stay in delirious patients: ' + str(
        average_value(lengthOfRassInDeliriumGlobal)))
    print('====================================================================')
    print('====================================================================')
    print('Accuracy of Delirium CAM-ICU against nursing notes at night time: ' + str(
        average_value(accuracyOfDeliriumNightTimeGlobal)))
    print('Accuracy of Delirium CAM-ICU against nursing notes at day time: ' + str(
        average_value(accuracyOfDeliriumDayTimeGlobal)))
    print('Accuracy of Nursing Notes at nighttime against CAM-ICU: ' + str(
        average_value(accuracyOfDeliriumNightTimeNursingGlobal)
    ))
    print('Accuracy of Nursing Notes at daytime against CAM-ICU: ' + str(average_value(
        accuracyOfDeliriumDayTimeNursingGlobal
    )))
    print('====================================================================')
    print('====================================================================')
    print('Percent of delirium days treated: ' + str(average_value(percentOfDaysDeliriumTreatedGlobal)))
    print('Average length of stay in whole cohort: ' + str(average_value(lengthOfStayGlobal)))
    print('Average length of stay if recorded CAM-ICU +ve at least once: ' + str(
        average_value(lengthOfStayIfDeliriumGlobal)))
    print(
        'Average length of delirium if patient has recorded CAM-ICU +ve: ' + str(average_value(lengthOfDeliriumGlobal)))
    print('====================================================================')
    print('====================================================================')
    i = 0
    print('Common Medical Histories in Delirium Cohort')
    for s in deliriumPmhxGlobal:
        print(str(i) + ': ' + str(s))
        i += 1
    print('====================================================================')
    print('====================================================================')

# DATAFRAMES INIT
df = pd.read_csv('C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\analysisNoArraysWithoutShortCases.csv')
df.replace(('Yes', 'No'), (1, 0), inplace=True)
dfOnlyCAMICUPositive = pd.read_csv('C:\\Users\\thesa\\Desktop\\auditProject\\Audit\\analysisNoArrays.csv')
dfOnlyCAMICUPositive = dfOnlyCAMICUPositive.drop(dfOnlyCAMICUPositive
                                                 [dfOnlyCAMICUPositive['Has CAM-ICU +ve'] == 0].index)

# mentalIllVsCamICU = df['Mental Illness?'].corr(df['Has CAM-ICU +ve'])
mentalIllVsCamICU = stats.pointbiserialr(df['Mental Illness?'].tolist(), df['Has CAM-ICU +ve'].tolist())
painVsCAMIcu = pearsonr(df['Has CAM-ICU +ve'].tolist(), df['Days pain dealt with'].tolist())
ageVsCamICU = pearsonr(dfOnlyCAMICUPositive['Age'].tolist(), dfOnlyCAMICUPositive['Days CAM ICU +ve'].tolist())
camICUvsAge = stats.pointbiserialr(df['Has CAM-ICU +ve'].tolist(), (df['Age'].tolist()))
RASSVsCAMMICU = stats.pointbiserialr(df['Has CAM-ICU +ve'].tolist(), hoursOfRassGlobal)

nursingDeliriumDayTimeVsMentalIllness = pearsonr(df['Days Nursing Notes delirium +ve daytime'].tolist(), df['Mental Illness?'].tolist())
nursingDeliriumNightTimeVsMentalIllness = pearsonr(df['Days Nursing Notes delirium +ve nighttime'].tolist(), df['Mental Illness?'].tolist())
nddVsAge = pearsonr(df['Days Nursing Notes delirium +ve daytime'].tolist(), df['Age'].tolist())
ndnVsAge = df['Days Nursing Notes delirium +ve nighttime'].corr(df['Age'])



corr, p_value = pearsonr(df['Days CAM ICU +ve'], df['Mental Illness?'])
corr2, p_value2 = spearmanr(df['Days CAM ICU +ve'], df['Mental Illness?'])
x = stats.pointbiserialr(np.array(df['Has CAM-ICU +ve']), np.array(df['Age']))

print('Correlation between increasing age and +ve CAM ICU: ' + str(camICUvsAge))
print('Correlation between mental illness and +ve CAM ICU: ' + str(mentalIllVsCamICU))
print('Corr between mental illness and NDD: ' + str(nursingDeliriumDayTimeVsMentalIllness))
print('Corr between mental illness and NDN: ' + str(nursingDeliriumNightTimeVsMentalIllness))
print('====================================================================')
print('====================================================================')
print('Correlation between pain not dealt with and +ve CAM ICU: ' + str(painVsCAMIcu))
print('====================================================================')
print('====================================================================')
print('Correlation between increasing age and length of delirium: ' + str(ageVsCamICU))
print('Corr between inc age and NDD: ' + str(nddVsAge))
print('Corr between inc age and NDN: ' + str(ndnVsAge))
print('Corr between RASS and +ve CAM ICU ' + str(RASSVsCAMMICU))

