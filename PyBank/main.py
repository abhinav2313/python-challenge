file_1 = 'budget_data_1.csv'
file_2 = 'budget_data_2.csv'
import csv
""" These variables are for first data set """
file_1_data=[]
file_2_data=[]
total_revenue_1 = 0
change_revenue_1 = []
total_change_revenue_1=0
""" These variables are for second data set """
total_revenue_2 = 0
change_revenue_2 = []
total_change_revenue_2=0
""" Reading first file """
with open(file_1,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')
    next(csv_reader,None)
    for row in csv_reader:
        file_1_data.append(row)

"""Reading second file"""
with open(file_2,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    next(csv_reader,None)
    for row in csv_reader:
        file_2_data.append(row)
"""Populating total revenue off first data set"""
for row in file_1_data:
    total_revenue_1 = total_revenue_1 + float(row[1])
    if(file_1_data.index(row) != len(file_1_data) - 1):
        change_revenue_1.append(float(file_1_data[file_1_data.index(row)+1][1]) - float(row[1]))
"""Populating change revenue off first data set"""
for row in change_revenue_1:
    total_change_revenue_1 = total_change_revenue_1 + abs(float(row))

"""Populating total revenue off second data set"""
for row in file_2_data:
    total_revenue_2 = total_revenue_2 + float(row[1])
    if(file_2_data.index(row) != len(file_2_data) - 1):
        change_revenue_2.append(float(file_2_data[file_2_data.index(row)+1][1]) - float(row[1]))

"""Populating change revenue off second data set"""
for row in change_revenue_2:
    total_change_revenue_2 = total_change_revenue_2 + abs(float(row))

"""Printing out first data set report"""
print("--------------------------First Data Set Report-------------------------------")
print("Number of months (1):: "+ str(len(file_1_data)))    
print("Total revenue (1):: "'${:,.2f}'.format(total_revenue_1))
print("Average change in revenue (1):: "+'${:,.2f}'.format(total_change_revenue_1/len(change_revenue_1)))
print("Greatest Increase in Revenue (1):: "+ file_1_data[(change_revenue_1.index(sorted(change_revenue_1)[len(change_revenue_1)-1]))+1][0]+" "+'${:,.2f}'.format(sorted(change_revenue_1)[len(change_revenue_1)-1]))
print("Greatest Decrease in Revenue (1):: "+file_1_data[change_revenue_1.index(sorted(change_revenue_1)[0])+1][0]+" "+'${:,.2f}'.format(sorted(change_revenue_1)[0]))

"""Printing out second data set report"""
print("--------------------------Second Data Set Report-------------------------------")
print("Number of months (2):: "+ str(len(file_2_data)))    
print("Total revenue (2):: "'${:,.2f}'.format(total_revenue_2))
print("Average change in revenue (2):: "+'${:,.2f}'.format(total_change_revenue_2/len(change_revenue_2)))
print("Greatest Increase in Revenue (2):: "+ file_2_data[(change_revenue_2.index(sorted(change_revenue_2)[len(change_revenue_2)-1]))+1][0]+" "+'${:,.2f}'.format(sorted(change_revenue_2)[len(change_revenue_2)-1]))
print("Greatest Decrease in Revenue (2):: "+file_2_data[change_revenue_2.index(sorted(change_revenue_2)[0])+1][0]+" "+'${:,.2f}'.format(sorted(change_revenue_2)[0]))