#q1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list1)
#q2
print(list(range(1, 13, 1)))
#q3
print(list1[3])

#q4
list2 = ["one", 1, 1.2]
print(list1 + list2)

#list1.append([1, 2, 3])
#print(list1)
exlist = list1
exlist.extend([1, 2, 3])
print(exlist)

#q5
print(set(exlist))

#q6
x = list1.pop(2)
print(x)
print(list1)
list1.insert(14, x)
print(list1)

#q7
print(list1[-1:])

#q8
a = [1, 2, ["one", "two", "three"], 4, 5]
print(a[2][1][2:3])

#q9
list3 = [1,2,3,4,56,3,2,6,432,6,7,4,26,76,6,6,6,6,6,6,6]
print(list3.count(6))
percentage = (6/len(list3))*100
print(percentage)