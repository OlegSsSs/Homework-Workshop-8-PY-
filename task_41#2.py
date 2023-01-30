# Уровень 2:

# - Количество действий произовльное
# 12 + 15 - 4

n = '22 + 300 - 14 + 10 - 8 + 2 - 4'
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
# print(calc(a, b, c))

for i in range(3, len(m) - 1, 2):                   # 3 - переменные в result, последняя 2 добавляет шаг для соосности выражения
    result = calc(result, int(m[i + 1]), m[i])      # выводим предыдущую функцию с новыми аргументами в выражении (знак и число)         

# print(m[i])
# print(m[i+1])

print(n, '=', result)


