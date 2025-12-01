

if __name__ == "__main__":
    log = []

def evaluate(expr):
    expr = expr.strip()

    log.append(f"Вычисление выражения: {expr}")

    if expr.isdigit():
        result = int(expr)
        log.append(f"Результат: {result}")
        return result

    if "(" in expr:
        start = None
        end = None
        for i, ch in enumerate(expr):
            if ch == "(":
                start = i
            elif ch == ")":
                end = i
                break

        inside = expr[start + 1 : end]

        inner_value = evaluate(inside)

        new_expr = expr[:start] + str(inner_value) + expr[end + 1:]
        return evaluate(new_expr)

    for op in "+-*/":
        if op in expr:
            left, right = expr.split(op)
            left = evaluate(left)
            right = evaluate(right)

            if op == "+":
                result = left + right
            elif op == "-":
                result = left - right
            elif op == "*":
                result = left * right
            else:  # '/'
                result = left / right

            log.append(f"Вычисление: {left} {op} {right} = {result}")
            return result
expression = "(2 + (3 * (4 - 1)))"
result = evaluate(expression)

print("Результат выражения:", result)
print("\nЖурнал рекурсий:")
for entry in log:
    print(entry)
