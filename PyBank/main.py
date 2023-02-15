# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv('./Resources/budget_data.csv')

# computing the number of months
number_months = len(df['Date'])

# computing net total amount of "Profit/Losses" over the entire period
total = df['Profit/Losses'].sum()

# computing the average of those changes over the entire period
average = df['Profit/Losses'].mean()

# computingThe greatest increase in profits over the entire period
maximum = df[df['Profit/Losses'] == df['Profit/Losses'].max()]
date_max = maximum['Date'].values[0]
value_max = maximum['Profit/Losses'].values[0]

# computingThe greatest decrease in profits over the entire period
minimum = df[df['Profit/Losses'] == df['Profit/Losses'].min()]
date_min = minimum['Date'].values[0]
value_min = minimum['Profit/Losses'].values[0]

# print the analysis

print('  Financial Analysis' + '\n' + '----------------------------' + '\n')
print('Total Months: ' + str(number_months))  
print('Total: $' + str(total))  
print('Average Change: $' + str(average))
print('Greatest Increase in Profits: ' + str(date_max) + '\t' + '$' + str(value_max))  
print('Greatest Decrease in Profits: ' + str(date_min) + '\t' + '$' + str(value_min))  

# save all this in a .txt file
f= open("./analysis/analysis_results.txt","w+")

f.write('  Financial Analysis' + '\n' + '----------------------------' + '\n')
f.write('Total Months: ' + str(number_months) + '\n')
f.write('Total: $' + str(total) + '\n')
f.write('Average Change: $' + str(average) + '\n')
f.write('Greatest Increase in Profits: ' + str(date_max) + '\t' + '$' + str(value_max) + '\n')
f.write('Greatest Decrease in Profits: ' + str(date_min) + '\t' + '$' + str(value_min) + '\n')

f.close()
