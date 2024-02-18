#q1
for x in range(0, 20):
    if x%2 != 0:
        print(x, end=" ")

#q2
for num in range(2, 201):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print('\n')

#q3
b = ["cat","dog","ham","bad","moon","sun"]
a = []
for x in b:
    if 'a' in x:
        a.append(x)
print(a)

#q4
count = 0
for x in b:
    for y in x:
        if y == 'o':
            count += 1
print(count)

#q5
x = input("Enter a word or a number: ")

if x.isdigit():
    print("The input is a number")
else:
    print("The input is a string.")

#q6
check = 1
while check > 0:
    x = input("Enter a word or a number (press q to exit): ")
    if x.isdigit():
        print("The input is a number")
    elif x == 'q':
        check -= 1
    else:
        print("The input is a string.")

#q7

