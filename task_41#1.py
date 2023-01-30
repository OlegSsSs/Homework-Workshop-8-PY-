# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15

# 1. Определить где операторы?
# 2. Где числовые значения?

# Уровень 1:

# - 1 действие
# - 2 аргумента

n = '12 + 15'
m = n.split()
print(m)


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

a = int(m[0])
c = m[1]
b = int(m[2])

result = calc(a, b, c)

print(n, '=', result)  

