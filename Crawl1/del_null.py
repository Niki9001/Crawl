import docx
import pandas as pd

from docx import Document
path = 'list.xlsx'
df = pd.read_excel(io='./list.xlsx')
#df.reindex(columns = list('ABCD'))
# delete null row

for i in range(1801):
    if (i - 6)% 18 == 0:
        df = df.drop([i])
k = df.dropna(axis=0,how='any')
j = df.iloc[2]

print(k)
write = pd.ExcelWriter('After1.xlsx')
data = k
data.to_excel(write)
write.save()
