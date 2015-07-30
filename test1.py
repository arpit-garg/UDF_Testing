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
	df = pandas.read_csv("sample_data_set.csv", error_bad_lines=False)
	#print len(df)
	#df = df.dropna(axis = 0)
	unique_ids = Series(df['CAID'].unique())
	
	#print y[345]
	total_unique_ids = len(unique_ids)
	#print leng
	
	df2 = DataFrame
	df3 = DataFrame()
	df6 = DataFrame()
	
	for i in range(0,total_unique_ids):
		
		df2 = df[df['CAID'] == unique_ids[i]]
		df3 = df3.append(df2, ignore_index=True)
		x = df2.index
		#print x
		#data_len = len(df2)
		#print data_len
		
		#df3.to_csv("output1.csv")

	
		result = []
		for x1 in x:
				
			#result = Series(re.split("\\W+|\\s+|\\d+", df2.loc[x1, 'Name']))
			#result = re.split("\\W+|\\s+|\\d+", df2.loc[x1, 'Name'])
			result.append(re.split("\\W+|\\s+", df2.loc[x1, 'Name']))
		result.append([''])
		#print result
		#print len(result)
		k = 0
		df4 = DataFrame()
		df5 = DataFrame()
		
		while k < len(result)-1:
			#By default each Merchant name occurs 1 time
			count_match = 1
			token=1
			temp = []
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
						else:
							break
					temp.append(result[j])

			except 	IndexError,e:
				print 'exception: ' + e
				continue
			
			#print temp
			stopwords = ['the']
			flag=0
			if temp is not None:
				tokens=[]
				#temp.append([''])
				for i in range(len(temp)-1):
					m, index,token =  (temp_func(temp[i], temp[i+1]))
					if m>1:
						tokens.append(token)
						pattern1=max(tokens)
						count_match+=1			
						flag=1	
					else:
						if token[0].lower() not in stopwords:
							count_match+=1
							pattern1=token
							flag=1
						else:
							pattern=temp[i]			
			k+=count_match			
			#print "count: "+ str(count_match)
			#print "pattern: "+ str(pattern)
			
			if flag==1:
				d['Pattern'] = str(pattern1)	
			else:
				d['Pattern'] = str(pattern)
			d['count'] = count_match
			
			df4 = DataFrame(d)
			df5 = df5.append(df4)
		
		df6 = df6.append(df5, ignore_index=True)
		
		
	#print df6	
	df6.to_csv("output_update.csv")	

	

if __name__ == '__main__':
	import timeit
	print(timeit.timeit("test()", setup="from __main__ import test", number=1))

