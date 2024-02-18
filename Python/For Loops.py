#q1
list1 = [1, 2, 3, 4, 5]
for x in list1:
    print(x)

#q2
list2 = [345,67,85436,23,1,89,98734]
for x in list2:
    product = x * len(str(x))
    print(product)

#q3
list3 = [345,-5,-345,67,85436,5,-123,24,0,89,-456,98734]
for x in list3:
    if x >= 0:
        print(x)

#q4
original =  [1,8.9,"cat",[1,2,3,4],8j,(1,2)]
new = []
for x in original:
    datatype = type(x)
    turple = (x, datatype)
    new.append(turple)
print(new)

#q5
Column1 = [6.7,4.5,9.7,3.2,4.0,34]
Column2 = [65.7,97.6,3.5,3.0,45.6,23.4]
Column3 = []
for x, y in zip(Column1, Column2):
    Columnx = y/x
    turple = (x, Columnx, y)
    Column3.append(turple)
print(Column3)

#q6
n = int(input("Enter a number: "))
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end="")
    print("\r")

#q7
