
rates = [
    "r d 0.01",
    "d e 0.98"
]

amount = 1000
path = ["r", "d", "e"]


exchange = {}
for line in rates:
    a, b, rate = line.split()
    exchange[(a, b)] = float(rate)


print(f"Начальная сумма: {amount} {path[0]}")
current = amount


for i in range(len(path) - 1):
    from_cur = path[i]
    to_cur = path[i + 1]

    if (from_cur, to_cur) in exchange:
        rate = exchange[(from_cur, to_cur)]
        current *= rate
        print(f"Конвертация: {from_cur} -> {to_cur}, курс = {rate}, сумма = {current:.2f}")
    else:
        print(f"Ошибка: нет курса {from_cur} -> {to_cur}")
        break

print(f"Итоговая сумма: {current:.2f} {path[-1]}")
