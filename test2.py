x = int(input())

result = 0
for i in range(x+1):
    y = ((-1) ** (i + 1)) * 2 * i
    result += y

print('result: %d'%result)