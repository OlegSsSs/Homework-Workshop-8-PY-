# Уровень 4:

# - Действия разделяются скобками
# (12 - 4) * 2

m = '(12 - 4) * 2'

m = m.replace(')', ' ) ')
m = m.replace('(', ' ( ')
lst = m.split()

def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

a = int(lst[1])
c = lst[2]
b = int(lst[3])

print(lst)

for i in range(1, len(lst) - 1, 2):

    if lst[i] == '*' or lst[i] == '/':
        result = calc(calc(a, b, c), int(lst[i + 1]), lst[i])
        print(m, '=', result)
