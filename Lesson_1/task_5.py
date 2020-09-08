proceeds = int(input("Enter proceeds your company: "))
costs = int(input("Enter costs your company: "))
profit = proceeds - costs
if proceeds > costs:
    print(f"Great! Your company have a profit: {profit} and profitability: {profit / proceeds * 100:.0f}%")
    employes = int(input("Enter number of employes: "))
    print(f"Profit per employe of the company: {profit / employes:.1f}")
else:
    print("Bad news, you have loss")
