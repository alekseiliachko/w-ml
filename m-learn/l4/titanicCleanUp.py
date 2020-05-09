import numpy as np
import pandas as pd
import re
import csv

translator = {
    'female': 0,
    'male': 1,
    'S': 0,
    'C': 1,
    'Q': 2,
}

sumAges = {}
agesCounter = {}

df = pd.read_csv("titanic_test.csv")
X = np.asarray(df.iloc[:, 1:])

isTest = 1

for line in X:
    age = line[4]
    if not np.isnan(age):
        print(line)
        title = re.search('\, (.*?)\.', line[2 - isTest]).group(1)
        sumAges[title] = (sumAges[title] if title in sumAges else 0) + age
        agesCounter[title] = (
            agesCounter[title] if title in agesCounter else 0) + 1

for key in agesCounter.keys():
    sumAges[key] = sumAges[key] / agesCounter[key]

# Fill missing data, map some of it
for line in X:
    # Age
    age = line[4 - isTest]
    if pd.isnull(age):
        title = re.search('\, (.*?)\.', line[2 - isTest]).group(1)
        line[4 - isTest] = sumAges[title]
    # Port
    port = line[-1]
    if pd.isnull(port):
        line[-1] = 0
    else:
        line[-1] = translator[line[-1]]
    # Sex
    line[3 - isTest] = translator[line[3 - isTest]]

allX = []
for line in X:
    dataWeWant = np.concatenate(
        (line[:(2 - isTest)], line[(3-isTest):(5 - isTest)], [line[5 - isTest] + line[6 - isTest]], line[(8 - isTest):(9 - isTest)], line[(10 - isTest):]))
    allX.append(dataWeWant)

with open('cleanupTest.csv', 'w', newline='') as csvfile:
    fieldnames = ['"pclass"', '"sex"',
                  '"age"', '"family_size"', '"fare"', '"embarked"']
    csvfile.write(",".join(fieldnames) + '\n')
    for line in allX:
        csvfile.write(",".join(str(x) for x in line) + '\n')
