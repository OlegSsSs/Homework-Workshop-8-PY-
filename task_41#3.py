# Уровень 3:

# - Действия имеют приоритет
# 12 - 4 * 2

n = '22 * 300 + 50 - 10 * 10'
m = n.split()
m2 = []
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

# print(calc(a, b, c))

# def calc_row(result):
for i in range(1, len(m) - 1, 2):                               # 3 - переменные в result, последняя 2 добавляет шаг для соосности выражения
    if m[i] == '*' or m[i] == '/':
        result_1 = calc(int(m[i - 1]), int(m[i + 1]), m[i])     # выводим предыдущую функцию с новыми аргументами в выражении (знак и число)         
        m2.append(result_1)
    else:
        m2.append(m[i])
        m2.append(int(m[i + 1]))
m2.pop(-2)
# print(m2)

a = int(m2[0])
c = m2[1]
b = int(m2[2])

result = calc(a, b, c)

for i in range(3, len(m2) - 1, 2):                    
    result = calc(result, int(m2[i + 1]), m2[i])               

print(n, '=', result)

# print(result_1)

# print(m2[i+1], m2[i])



