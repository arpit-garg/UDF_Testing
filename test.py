from pandas import *
import numpy as nm
import re



def test():
	df = pandas.read_csv("../sample_data_set.csv")
	#print df
	df1 = df.dropna(axis = 1)
	y = Series(df['CAID'].unique())
	
	#print y[345]

	leng = len(y)
	#print leng
	
	df2 = DataFrame
	
	for i in range(0,1):
		
		#df2.append(df1[df1['CAID'] == y[i]], ignore_index=True)
		df2 = df1[df1['CAID'] == y[i]]
		
		print df2
		x = df2.index
		print x
		
		data_len = len(df2)
		print data_len
		
	#df2.to_csv("output.csv")
		
		"""
		first_index = x[0]
		first_name = df1['Name'][x[2]]
		print first_name
		name1_len = len(first_name)
		print name1_len
		"""
	
		result = []
		for x1 in x:
				
			#result = Series(re.split("\\W+|\\s+|\\d+", df2.loc[x1, 'Name']))
			#result = re.split("\\W+|\\s+|\\d+", df2.loc[x1, 'Name'])
			result.append(re.split("\\W+|\\s+|\\d+", df2.loc[x1, 'Name']))
			
			count = 1 #By default each Merchant name occurs 1 time
		
		for i in range(0, len(result)-1):
			
			#print result[i]
			#print len(result[i])
			
			#comparing each split within
			for j,k in zip((0, len(result[i])), (0, len(result[i+1]))):	
			
				if result[i][j] == result[i+1][k]:
					print result[i][j] + "==" +result[i+1][k]
				
				
				
			#result_df = DataFrame(result)
		#print result_df
#def patt_matching():
	
	

"""				
				if len(df2.loc[x1, 'Name']) >= len(df2.loc[x[0], 'Name']):
					name = df2.loc[x[0],'Name']
					df2.loc[x1, 'Name'] = name
			
		print df2
"""

if __name__ == "__main__":
	test()



"""
1.Make separate functions for all the loopings
2.check for if conditions within dataframes.
3.return count, caid and merchant_name for every matched pattern 
  and then store it in a bigger array
4.check a method for pattern matching.
"""

