# Cleaning data delete space

import numpy as np
import pandas as pd

df = pd.read_excel("After1.xlsx")

l = np.array(df)
j = l.tolist()
Ldate = []
Ljob = []
LcomN = []
Lloc = []
for i in range(599):
    if i % 6 == 0:
        Ldate.append(j[i])
    if (i - 1)%6 == 0:
        Ljob.append(j[i])
    if (i-3)%6 == 0:
        LcomN.append(j[i])
    if (i-4)%6 == 0:
        Lloc.append(j[i])
#zhengze
#strinfo=re.compile()
#strinfo=re.compile(' ')
#b = strinfo.sub(' ',Ldate)
Cdate = []
for index,value in enumerate(Ldate):
    for i in value:
        afters = i.strip()
        Cdate.append(afters)

Cjob = []
for index,value in enumerate(Ljob):
    for i in value:
        afterj = i.strip()
        Cjob.append(afterj)

CcomN = []
for index,value in enumerate(LcomN):
    for i in value:
        afterc = i.strip()
        CcomN.append(afterc)

Cloc = []
for index,value in enumerate(Lloc):
    for i in value:
        afterlc = i.strip()
        Cloc.append(afterlc)


#print(Ldate)
# new df
test = pd.DataFrame({'Date':Cdate,'Job':Cjob,'Company':CcomN,'Location':Cloc})
test.to_excel('list1.xlsx')

#df1 = pd.DataFrame(Cdate,Cjob,CcomN,Cloc,columns=['Date','Job','CompanyName','Location'])
#df1.to_excel('list1.xlsx')

