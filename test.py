from pandas import *
import numpy as nm
import re

"""
def temp_func(temp):
	for i,j in zip(range(0,len(temp)),range(len(1,temp[i]))):
		if temp[i][j] == temp
		
"""	

def test():
	df = pandas.read_csv("../../sample_data_set.csv", error_bad_lines=False)
	#print len(df)
	#df = df.dropna(axis = 0)
	y = Series(df['CAID'].unique())
	
	#print y[345]
	total = 0
	leng = len(y)
	#print leng
	
	countx = 0
	df2 = DataFrame
	df3 = DataFrame()
	df6 = DataFrame()
	
	for i in range(0,leng):
		
		df2 = df[df['CAID'] == y[i]]
		df3 = df3.append(df2, ignore_index=True)
		x = df2.index
		#print x
		#data_len = len(df2)
		#print data_len
		
		#df3.to_csv("output1.csv")
	
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
			result.append(re.split("\\W+|\\s+", df2.loc[x1, 'Name']))
		result.append([''])
		#print result
		#print len(result)
		sum = 0
		k = 0
		df4 = DataFrame()
		df5 = DataFrame()
		
		while k < len(result)-1:
			#By default each Merchant name occurs 1 time
			count = 1 
			
			#print "CAID: " + str(df2['CAID'][x[k]]) + "," + "result: " + " ".join(result[k])
			
			d = { 'CAID': Series(df2['CAID'][x[k]]),
				   'Name': Series(" ".join(result[k])),
				   'Pattern': result[k][0],
				   }
			j = k+1	   
			if j < (len(result)-1):
				
				while result[k][0] == result[j][0]:
					count += 1
					j +=1
		
			k += count
			
			
			
			d['count'] = count
			df4 = DataFrame(d)
			
			df5 = df5.append(df4)
			sum += count
			#print "count: "+ str(count)
			
		
		df6 = df6.append(df5, ignore_index=True)
		
		if count == 1:
			countx +=1
		total += sum
		print "total: " +str(total)
	#print df6	
	df6.to_csv("output_count1.csv")	
	#print "count: "+str(countx)
	
	

if __name__ == '__main__':
	import timeit
	print(timeit.timeit("test()", setup="from __main__ import test", number=1))



"""
1.Make separate functions for all the loopings
2.check a method for pattern matching.(data matching techniques)

"""

