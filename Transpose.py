import pandas as pd
file_path = 'Elect and Other Services Unit Rate.xlsx'
df = pd.read_excel(file_path, usecols='E,H,Q:Y')
df['MiscInformation'] = df['MiscInformation'].str.split("|",expand=True)[3]
Finaldf = pd.DataFrame()
for i in range(2,11):
    name = ''
    name = name + str(df.columns[i])[:4] + '-'
    if len(str(df.columns[i])) > 4:
        name = name + str(df.columns[i])[4:] + '-01'
    else: name = name + '00-00'
    Tempdf = pd.DataFrame()
    Tempdf['REFORECAST_DATE'] = df['REFORECAST_DATE']
    Tempdf['LOCATION_CODE'] = df['MiscInformation']
    Tempdf['RPT_MTH'] = name
    Tempdf['RPT_RATE'] = df[df.columns[i]]
#     print(Tempdf)
    Finaldf = Finaldf.append(Tempdf, ignore_index=True)
#     print(Finaldf)
print(Finaldf)
Finaldf.to_csv('output.csv', sep='|', index=False)
csv1 = pd.read_csv('output.csv')
csv2 = pd.read_csv('output2.csv')
csv1.compare(csv2)
