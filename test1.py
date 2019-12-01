f1 = open('test.txt', 'w+')

n = int(input())

for i in range(n+1):
    if i % 4 == 0:
        continue
    elif i % 4 == 1:
        data = '%d ' %i
        f1.write(data*(i%4))
        f1.write('\n')
    elif i % 4 == 2:
        data = '%d ' % i
        f1.write(data *(i%4))
        f1.write('\n')
    elif i % 4 == 3:
        data = '%d ' % i
        f1.write(data *(i%4))
        f1.write('\n')

f1.seek(0, 0)
data = f1.read()
print(data)