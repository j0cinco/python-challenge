import os
import csv

# csv file path
budget_data_load = "Resources\budget_data.csv"

#set the output of the text file
budget_analysis_output = os.path.join("analysis", "budget_analysis.txt")

#Variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


#open csv file
with open(budget_data_load) as financial_data:
    reader = csv.reader(financial_data)
    PL = next(reader)

    #Loop to count total months
    for row in reader:

        #Count the total of months
        total_months += 1

        #Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row[1])

        #Calculate the average change in revenue between months over the entire period
        revenue_change = float(row[1])- previous_revenue
        previous_revenue = float(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_change = [month_change] + [row[0]]
        revenue_average = (revenue_change)/(total_months)


        #The greatest increase in revenue over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row[0]

        #The greatest decrease in revenue over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row[0]
    

#write changes to csv
with open(budget_analysis_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % revenue_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

    print("Financial Analysis\n")
    print("---------------------\n")
    print("Total Months: %d\n" % total_months)
    print("Total Revenue: $%d\n" % total_revenue)
    print("Average Revenue Change $%d\n" % revenue_average)
    print("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

