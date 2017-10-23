file_path = 'election_data_2.csv'
import csv
import collections
"""Declaring variables to hold the voting data"""
raw_data = []
vote_dict = dict()
vote_dict = collections.defaultdict(list)
winner_dict=dict()
winners = []
"""Opening raw data file """
with open(file_path,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')
    next(csv_reader,None)
    for row in csv_reader:
        raw_data.append(row)

for row in raw_data:
       vote_dict[row[2]].append(row[0])


"""Printing out the results"""
print("Election Results")    
print("----------------------")
print("Total votes: "+"{:,}".format((len(raw_data))))
print("----------------------")
for key,value in vote_dict.items():
    print("No of votes for: "+str(key)+"("+str(len(value)*100/len(raw_data))+"%)"+" --> "+"{:,}".format(len(value)))
    winner_dict[key] = len(value)
for key, value in sorted(winner_dict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
    winners.append(key)
print("-----------------------")
print("Winner: "+str(winners[-1]))
