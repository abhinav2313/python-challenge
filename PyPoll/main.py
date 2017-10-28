file_path = 'election_data_2.csv'
file_results = 'election_results.txt'
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

file=open(file_results,'w')
"""Printing out the results"""
file.write("Printing out the results\n")
print("Election Results")   
file.write("Election Results\n")   
print("----------------------")
file.write("----------------------\n")
print("Total votes: "+"{:,}".format((len(raw_data))))
file.write("Total votes: "+"{:,}".format((len(raw_data)))+"\n")
print("----------------------")
file.write("----------------------\n")
for key,value in vote_dict.items():
    file.write("No of votes for: "+str(key)+"("+str(len(value)*100/len(raw_data))+"%)"+" --> "+"{:,}".format(len(value))+"\n")
    winner_dict[key] = len(value)
for key, value in sorted(winner_dict.iteritems(), key=lambda (k,v): (v,k)):
    print("%s: %s" % (key, value))
    file.write("%s: %s" % (key, value)+"\n")
    winners.append(key)
print("-----------------------")
file.write("-----------------------\n")
print("Winner: "+str(winners[-1]))
file.write("Winner: "+str(winners[-1])+"\n")
file.close()