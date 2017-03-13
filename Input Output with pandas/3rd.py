#got quandl.com
#get the dataset
import pandas as pd


# df = pd.read_csv("ZILL-Z77006_3B.csv")

# print(df.head())

# #setting the index
# df.set_index('Date',inplace=True)
# df.to_csv('newcsv2.csv')

# #specifying index
# df = pd.read_csv("newcsv2.csv",index_col=0)
# print(df.head())

# #change column names
# df.columns = ['Austin_HPI']
# print(df.head())

# df.to_csv("newcsv3.csv")

# #save without headers
# df.to_csv("newcsv4.csv", header=False)
# df = pd.read_csv('newcsv4.csv',names=['Date','Austin_HPI'], index_col=0)
# print(df.head())

# #save as html table
# df.to_html("example.html")


df = pd.read_csv('newcsv4.csv',names=['Date','Austin_HPI'])
print(df.head())

#renaming a column
df.rename(columns={'Austin_HPI':'77005_HPI'},inplace=True)
print(df.head())