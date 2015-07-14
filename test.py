from pandas import *
import numpy as nm
import re



def test():
	df = pandas.read_csv("../sample_data_set.csv")
	#print len(df)
	df1 = df.dropna(axis = 1)
	y = Series(df['CAID'].unique())
	
	#print y[345]
	total = 0
	leng = len(y)
	#print leng
	
	df2 = DataFrame
	df3 = DataFrame()
	for i in range(0,3):
		
		df2 = df1[df1['CAID'] == y[i]]
		df3 = df3.append(df2, ignore_index=False)
		x = df2.index
		#print x
		
		data_len = len(df2)
		#print data_len
		
		#df3.to_csv("output.csv")
		#print len(df3)
		
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
			
		
		
		j = 0
		sum = 0
		
		k = 0
		while k < len(result)-1:
			count = 1 #By default each Merchant name occurs 1 time
			print "CAID: " + str(df2['CAID'][x[k]]) + "," + "result: " + str(result[k])
			#print len(result[k])
			
			if result[k][0] == result[k+1][0]:
				count += 1
				for j in range(k+1, len(result)-1):
					if result[j][0] == result[j+1][0]:
						count += 1
					else:
						break
				k += count
			else:
				count = 1
				k += 1
			
			sum += count
			print "count: "+ str(count)
		total += sum
		print total
			
	


if __name__ == "__main__":
	test()



"""
1.Make separate functions for all the loopings
2.append to a dataframe
3.check a method for pattern matching.(data matching techniques)

"""

