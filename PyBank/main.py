import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

def financial_analysis(data):
        
    total_months = 0
    net_total = 0 
    prev_profit_loss = 0 
    changes = []
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}
    average_change = 0.0

    for row in data:    
        date = row[0]
        profit_loss = int(row[1])

        total_months = total_months + 1
        net_total = net_total + profit_loss

        change = profit_loss - prev_profit_loss
        changes.append(change)
        prev_profit_loss = profit_loss

        if change > greatest_increase["amount"]:
            greatest_increase["date"] = date
            greatest_increase["amount"] = change

        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = change

        average_change = sum(changes) / len(changes)

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


    output_file = os.path.join("analysis", "financial_analysis.csv")

    with open (output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        writer.writerow(["Total Months", total_months])
        writer.writerow(["Total", net_total])
        writer.writerow(["Average Change", average_change])
        writer.writerow(["Greatest Increase in Profits", f"{greatest_increase['date']} (${greatest_increase['amount']})"])
        writer.writerow(["Greatest Decrease in Profits", f"{greatest_decrease['date']} (${greatest_decrease['amount']})"])

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    financial_analysis(csvreader)