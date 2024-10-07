# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 # total number of months

total_netProfit = 0 # total of all profits and losses

# Add more variables to track other necessary financial data

profit_loss_change = [] # sum of the change in profit and loss each month

profit_loss_average = [] # average of the profit_loss_change

previous_profit_loss = None

dates = [] # stores the dates


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

        # Extract first row to avoid appending to net_change_list
    first_row =next(reader)

    # Track the total and net change
    for row in reader:
        total_months += 1
        profit_loss = int(row[1])
        date = row[0]
        total_netProfit += profit_loss

        dates.append(date)
                   
        if previous_profit_loss is not None:
            diff = profit_loss - previous_profit_loss
            profit_loss_change.append(diff)
        else:
            profit_loss_change.append(None)
        previous_profit_loss = profit_loss

profit_loss_average = sum(diff for diff in profit_loss_change if diff is not None) / (len(profit_loss_change) - 1)
average_change = round(profit_loss_average, 2)
       
greatest_increase = max(diff for diff in profit_loss_change if diff is not None)
greatest_decrease = min(diff for diff in profit_loss_change if diff is not None)

greatest_increase_index = profit_loss_change.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]

greatest_decrease_index = profit_loss_change.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]

# Generate the output summary
    
financial_output = (
f"\nFinancial Analysis\n"
f"------------------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_netProfit}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}\n"
)
   

# Print the output
print(financial_output)


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(financial_output)
