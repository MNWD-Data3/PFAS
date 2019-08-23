import pandas as pd 
import numpy as np 

from pandas import Series
import matplotlib.pyplot as plt

import pickle 

import seaborn as sns

vars = ['Station Name','Parameter Name','Parameter_Abbreviation','Sample Date','Sample Time','Result Value (10% of RDL for NDs)','Result Text',
'Units','RDL','Detected (Y: Yes; N: No)','Laboratory Sample Number','Method']

data = pd.read_csv('All-Table 1.csv', names = vars, skiprows= 17)

#print(data.head(100))

sns.set(rc={'figure.figsize':(11, 4)})

"""

if data[data.Parameter_Abbreviation == 'PFBS']:#
	con1 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con1,'r')
elif data['Parameter Abbreviation'] == 'PFHpA':#
	con2 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con2,'r')
elif data['Parameter Abbreviation'] == 'PFHxS':#
	con3 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con3,'r')
elif data['Parameter Abbreviation'] == 'PFNA':#
	con4 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con4,'r')
elif data['Parameter Abbreviation'] == 'PFOS':#
	con5 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con5,'r')
elif data['Parameter Abbreviation'] == 'PFOA':#
	con6 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con6,'r')
elif data['Parameter Abbreviation'] == 'GENX':#
	con7 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con7,'r')
elif data['Parameter Abbreviation'] == 'PFDA':#
	con8 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con8,'r')
elif data['Parameter Abbreviation'] == 'PFDoA':#
	con9 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con9,'r')
elif data['Parameter Abbreviation'] == 'PFHxA':#
	con10 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con10,'r')
elif data['Parameter Abbreviation'] == 'PFTA':#
	con11 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con11,'r')
elif data['Parameter Abbreviation'] == 'PFTrDA':#
	con12 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con12,'r')
elif data['Parameter Abbreviation'] == 'PFUnA':#
	con13 = data['Result Value (10% of RDL for NDs)']
	plt.plot(con13,'r')
"""

### https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/

datasep = data.groupby('Parameter_Abbreviation')
print(datasep.first()) #print first entries in all groups formed

#genx,pfbs,pfda,pfdoa,pfhpa,pfhxa,pfhxs,pfna,pfoa,pfos,pfta,pftrda,pfuna
#genx, pfdoa, pfta,pftrda,pfuna
genx = datasep.get_group('GenX')###
con1 = genx['Result Value (10% of RDL for NDs)']
pfbs = datasep.get_group('PFBS')
con2 = pfbs['Result Value (10% of RDL for NDs)']
pfda = datasep.get_group('PFDA')
con3 = pfda['Result Value (10% of RDL for NDs)']
pfdoa = datasep.get_group('PFDoA')
con4 = pfdoa['Result Value (10% of RDL for NDs)']
pfhpa = datasep.get_group('PFHpA')
con5 = pfhpa['Result Value (10% of RDL for NDs)']
pfhxa = datasep.get_group('PFHxA')
con6 = pfhxa['Result Value (10% of RDL for NDs)']
pfhxs = datasep.get_group('PFHxS')
con7 = pfhxs['Result Value (10% of RDL for NDs)']
pfna = datasep.get_group('PFNA')
con8 = pfna['Result Value (10% of RDL for NDs)']
pfoa = datasep.get_group('PFOA')####
con9 = pfoa['Result Value (10% of RDL for NDs)']
pfos = datasep.get_group('PFOS')####
con10 = pfos['Result Value (10% of RDL for NDs)']
pfta = datasep.get_group('PFTA')
con11 = pfta['Result Value (10% of RDL for NDs)']
pftrda = datasep.get_group('PFTrDA')
con12 = pftrda['Result Value (10% of RDL for NDs)']
pfuna = datasep.get_group('PFUnA')
con13 = pfuna['Result Value (10% of RDL for NDs)']

#plt.plot(con1,'b')
plt.plot(con2,'g')
#plt.plot(con4,'c')
plt.plot(con5,'m')
plt.plot(con6,'y')
plt.plot(con7,'k')
plt.plot(con8,'w')
plt.plot(con9,'r')
plt.plot(con10,'g')
#plt.plot(con11,'r')
#plt.plot(con12,'c')
#plt.plot(con13,'m')
plt.savefig('line_plts.png')
plt.show()
