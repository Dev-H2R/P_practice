#loops functions project

for i in range(3):
    print("Hello")

#whi;e
i = 1
while i <= 5:
    print(i)
    i = i + 1

num = 1
while num <= 10:
    print(num)
    num += 1

#Range function
range(5)        # 0 to 4
range(1, 5)     # 1 to 4
range(1, 10, 2) # 1,3,5,7,9

for i in range(1, 10, 2):
    print(i)

#break and continue 
# break -> stop loop
for i in range(1, 6):
    if i == 3:
        break
    print(i)

#continue -> Skip current location
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

#p1 print 1 to 10
for i in range(1, 11):
    print(i)

#p2 Table of num
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#prog3
n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

#reverse counting
for i in range(10,0,-1):
    print(i)