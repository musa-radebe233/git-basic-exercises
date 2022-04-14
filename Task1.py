#task 1.1
num = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        num.append(i)
print(sum(num))
