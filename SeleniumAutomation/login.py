# import csv
# # print("The csv lib version is",csv.__version__)
#
# def read_csv(filename):
#     with open(filename,'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         data = list(reader)
#         return data
#
# data = read_csv('Testdata.csv')
# username = data[0]['username']
# password = data[0]['password']
# print(password)
from distutils.command.install import install

import pandas as pd
print(pd.__version__)
data = pd.read_excel("Testdata.xlsx",sheet_name=None)
# print(data)
# print(data.keys())
Login = data['Login']
uname = Login.loc[0,'username']
pswrd = Login.loc[0,'password']
