import pandas
import pandasql


def query_analysis(filename):
	
	df = pandas.read_csv(filename)
	
	#print df 
	
	q1 = """
		select * from df
		order by CAID;
		"""
		
	ordered_result = pandasql.sqldf(q1.lower(), locals())
	#print ordered_result
	
	q2 = """
		select caid, name, count(distinct name)
		from ordered_result
		group by caid, name;
		"""
		
	grouped_result = pandasql.sqldf(q2.lower(), locals())
	#print grouped_result
	
	grouped_result.to_csv("ordered_sample_data_set.csv")









if __name__ == "__main__":
	query_analysis("sample_data_set.csv")
