import json
company_profit = {}
count = 0
summary = 0
with open('text_7.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        title, ownership, income, cost = line.split()
        profit = float(income) - float(cost)
        company_profit[title] = profit
        if profit > 0:
            count += 1
            summary += profit
average = {'average_profit': summary/count}
result = [company_profit, average]
with open('text_77.json', 'w') as result_file:
    json.dump(result, result_file, ensure_ascii=False, indent=4)
