import pandas
import os


dossier  = os.getcwd()

path = os.path.join(dossier, 'env', 'sons','notes.csv')
# print(dossier)

df = pandas.read_csv(path)

print(df)