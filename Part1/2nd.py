import pandas as pd

import numpy as np

#information as dataframe

web_stats = {'Day':[1,2,3,4,5,6],
			'Visitors':[43,53,34,45,64,34],
			'Bounce_Rate':[65,72,62,64,54,66]}

#convert this dictionary to dataframe 

df = pd.DataFrame(web_stats)

#print(df)
#print(df.head())
#print(df.tail())
#print(df.tail(2))

#set index and print
#print(df.set_index('Day'))
#print(df.head())

# save the index instead of just printing it
#df = df.set_index('Day')

#view a column
#print(df['Visitors'])
#print(df.Visitors)

#view list of columns
#print(df[['Bounce_Rate','Visitors']])

#convert to list
#print(df.Visitors.tolist())

#list of list
#print(df[['Bounce_Rate','Visitors']].tolist())
print(np.array(df[['Bounce_Rate','Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))

print(df2)

