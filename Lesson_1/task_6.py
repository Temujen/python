base = float(input("Введите результат первого дня: "))
plan = float(input("Введите целевую дистанцию: "))
current = base
day = 1
while current <= plan:
    print(f"{day}-й день: {current:.2f}")
    day += 1
    current *= 1.1
print(f"{day}-й день: {current:.2f}")
print(f"На {day}-й день спортсмен достиг результата - не менее {plan:.0f} км.")
