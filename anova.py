#import library
def main():
	#prompt user for input
	table = prompt.get-table()
	#analyse and solve input
	fratio = anova.anova.analyse(table)
	#return hypothesis
	print(anova.hypothesis.find(fratio))
