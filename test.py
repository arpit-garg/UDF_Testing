from pandas import *
import numpy as nm



def test():
	df = pandas.read_csv("../sample_data_set/Sheet1.csv")
	#print df
	df1 = df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], axis = 1)
	y = Series(df['CAID'].unique())
	
	#print y[345]

	leng = len(y)
	#print leng
	
	
	
	for i in range(0,1):
		
		df2 = df1[df1['CAID'] == y[i]]
		
		print df2
		x = df2.index
		print x
		
		data_len = len(df2)
		print data_len
		#first_name = df1['Merchant Name'][i]
		#print first_name
		#name1_len = len(df1['name'][i])
		#print name1_len
		#print len(df2['Merchant Name'][0])
		
		for j in range(1, data_len):
			for x1 in x:
				
				if len(df2['Merchant Name'][x1]) == len(df2['Merchant Name'][0]):
				
					df2['Merchant Name'][x1] = df2['Merchant Name'][0]
					
		print df2


if __name__ == "__main__":
	test()



"""
1.Make separate functions for all the loopings
2.check for if conditions within dataframes.
3.return count, caid and merchant_name for every matched pattern 
  and then store it in a bigger array
4.check a method for pattern matching.
"""

