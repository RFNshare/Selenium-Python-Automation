# For Loop
obj = [1, 2, 3, 4, 5, 6, 6]
j = 0

for i in obj:
    j += i
print(j)

for k in range(1, 6):
    print(k)

print("************************")

for k in range(1, 6, 2):
    print(k)

print("************************")

for k in range(10):
    print(k)

# While Loop

n = 5
while n > 0:
    print(n)
    n -= 1
    if n == 1:
        break
    continue


