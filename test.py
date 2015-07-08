from pandas import *
import numpy as nm



def test():
	df = pandas.read_csv("../sample_data_set.csv")
	#print df
	df1 = df.dropna(axis = 1)
	y = Series(df['CAID'].unique())
	
	#print y[345]

	leng = len(y)
	#print leng
	
	
	
	for i in range(0,5):
		
		df2 = df1[df1['CAID'] == y[i]]
		
		print df2
		x = df2.index
		print x
		
		data_len = len(df2)
		print data_len
		"""
		first_index = x[0]
		first_name = df1['Name'][x[2]]
		print first_name
		name1_len = len(first_name)
		print name1_len
		"""
	
		for j in range(1, data_len):
				
			
			for x1 in x:
				
				if len(df2.loc[x1, 'Name']) >= len(df2.loc[x[0], 'Name']):
					name = df2.loc[x[0],'Name']
					df2.loc[x1, 'Name'] = name
			
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

