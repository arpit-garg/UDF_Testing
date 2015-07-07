from pandas import *
import numpy as nm



def test():
	df = pandas.read_csv("sample_data_set/Sheet1.csv")
	#print df
	df1 = df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], axis = 1)
	y = Series(df['CAID'].unique())
	
	#print y[345]

	leng = len(y)
	#print leng
	
	
	
	for i in range(0,3):
		
		df2 = df1[df1['CAID'] == y[i]]
		
		print df2
		x = df2.index
		print x
		
		data_len = len(df2)
		print data_len
		first_name = df1['Merchant Name'][i]
		print first_name
		#name1_len = len(df1['name'][i])
		#print name1_len
"""		
		for j in range(1, data_len):
			
			if len(df1['name']) > name1_len:
				
				df1['name'][j] = first_name
				print df1
"""

if __name__ == "__main__":
	test()
