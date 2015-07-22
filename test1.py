from __future__ import division
from pandas import *
import numpy as nm
import re


def temp_func(temp1, temp2):
	index1,index2=[],[]
	token=[]
	#print temp1,temp2
	for i in temp1:
		if i in temp2:
			index1.append(temp1.index(i))
			index2.append(temp2.index(i))
			token.append(i)
			#print temp1.index(i)
	#m = len(set(temp1)&set(temp2))/len(set(temp1)|set(temp2))
	m = len(set(temp1)&set(temp2))
	index = list(set(index1)&set(index2))
	#return (m,index1,index2)
	#print 'index: '+str(index)
	return (m,index,token)


def test():
	df = pandas.read_csv("../sample_data_set/Sheet1.csv", error_bad_lines=False)
	#print len(df)
	#df = df.dropna(axis = 0)
	y = Series(df['CAID'].unique())
	
	#print y[345]
	#total = 0
	leng = len(y)
	#print leng
	
	#countx = 0
	df2 = DataFrame
	df3 = DataFrame()
	df6 = DataFrame()
	
	for i in range(0,leng):
		
		df2 = df[df['CAID'] == y[i]]
		#df3 = df3.append(df2, ignore_index=True)
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
		#sum = 0
		k = 0
		df4 = DataFrame()
		df5 = DataFrame()
		
		while k < len(result)-1:
			#By default each Merchant name occurs 1 time
			count = 1
			count_match=1
			token=1
			temp = []
			pattern=[]
			pattern=result[k]

			#print "CAID: " + str(df2['CAID'][x[k]]) + "," + "result: " + " ".join(result[k])
			
			d = { 'CAID': Series(df2['CAID'][x[k]]),
				   'Name': Series(" ".join(result[k])),
				   }
			
			try:
				if result[k][0] == result[k+1][0]:
					for j in range(k, len(result)-1):
						if result[j][0] == result[j+1][0]:
							temp.append(result[j])
							count+=1
						else:
							break
					temp.append(result[j])
					#k += count
				#else:
				#	k += 1
			
			except 	IndexError,e:
				print 'exception: ' + e
				continue
			
			#print temp
			stopwords = ['the']
			
			if temp is not None:
				match1 = []
				match2 = []
				indices1 = []
				indices2 = []
				tokens=[]
				#temp.append([''])
				for i in range(len(temp)-1):
					m, index,token =  (temp_func(temp[i], temp[i+1]))
					if m>1:
						match1.append(m)
						indices1.append(index)
						tokens.append(token)
						pattern=max(tokens)
						count_match+=1				
					else:
						if token[0] not in stopwords:
							count_match+=1
							pattern=token
						else:
							pattern=temp[i]			
			k+=count_match			
			#print "count: "+ str(count_match)
			#print "pattern: "+ str(pattern)
						
			d['Pattern'] = str(pattern)	
			d['count'] = count_match
			df4 = DataFrame(d)
			
			df5 = df5.append(df4)
			#sum += count
			#print "count: "+ str(count)
			
		
		df6 = df6.append(df5, ignore_index=True)
		
		
		#total += sum
		#print "total: " +str(total)
	#print df6	
	df6.to_csv("output_update.csv")	
	#print "count: "+str(countx)
	
	

if __name__ == '__main__':
	import timeit
	print(timeit.timeit("test()", setup="from __main__ import test", number=1))



"""
1.Make separate functions for all the loopings
2.check a method for pattern matching.(data matching techniques)

"""

