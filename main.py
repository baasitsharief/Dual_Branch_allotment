import csv

# In the branch dictionary, 1 is A1, 2 is A2 and so on. And the values corresponding to each branch is the number of seats(not actual, don't worry. They are scaled down according to the number of responses filled in the csv.)
branch = {'1':7,'2':8,'3':13,'4':10,'7':22,'8':5,'A':13,'B':5}
# I've set the initial cutoffs to 10. Change it or don't use this dictionary, it is your choice.
cutoff = {'1':10,'2':10,'3':10,'4':10,'7':10,'8':10,'A':10,'B':10}

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""
    f = open(raw_file, "r+")  # > Open File
    reader = csv.reader(f) # > Start reading the file
    parsed_data = []
    g=1
    csv_data = []
    for row in reader:
    	if(g==1):
    		fields = row
    		g=7
    	else:
    		csv_data.append(row)
    # The following loop adds the data from csv to parsed_data
    for row in csv_data:
        # Figure out what dict() and zip() do. Read the documentation. Links are in the post.
        parsed_data.append(dict(zip(fields, row)))

    f.close()

    return parsed_data

def branch_allot(pref_data):
	for i in range(len(pref_data)):
		pref = '1'
		for j in range(len(pref_data[i])):
			x = pref_data[i][pref]
			m = x[1:]
			if(branch[m]>0):
				pref_data[i]['alloted'] = x
				cutoff[m] = pref_data[i]['CG Year 1']
				branch[m] -= 1
				break
			else:
				pref = ord(pref)-48
				pref += 49
				pref = chr(pref)

def alloted_results(pref_data):
	fields = ["ID","CG Year 1","1","2","3","4","5","6","7","8","9","alloted"]
	f = open("result.csv", "w")
	writer = csv.DictWriter(f, delimiter=",", fieldnames = fields)
	writer.writeheader()
	for row in pref_data:
		writer.writerow(row)

def main():
	pref_data = parse("file.csv", ",")
	branch_allot(pref_data)
	print(cutoff)
	alloted_results(pref_data)

if __name__ == '__main__':
	main()