#q1 
l = [x for x in range(1, 8)]
print(l)

#q2
list = [x for x in range(100, 2100, 100)]
print(list)

#q3 #q4
kevin = [4.54,7.89,5.66,2.00]
my_list = [round(x*1.08, 2) for x in kevin]
print(my_list)

#q5
mylist = [1,2,3,4,5,6,7,8,9]
newlist = [x for x in mylist if x%2]
print(newlist)

#q6
mylist1 = [1,2,3,4,5,6,7,-2,-7,4,-9]
newlist1 = [x if x>= 0 else 0 for x in mylist1 ]
print(newlist1)

#q7
mixed = [1,"a",9.99,"b",["c",1],6,23,5.67,9]
ans = [x for x in mixed if type(x) != str]
print(ans)

#q8
ans2 = [x for x in mixed if isinstance(x, (int, float))]
print(ans2)

#q9
cities = ["Cape Town","Tokyo","Oslo"]
temps = [[20.4,    20.4,    19.2,    16.9,    14.4,    12.5,    11.9,    12.4,    13.7,    15.6,    17.9,    19.5,    16.2],[5.2,    5.7,    8.7,    13.9,    18.2,    21.4,    25.0,    26.4,    22.8,    17.5,    12.1,    7.6,    15.4],[-4.3,    -4.0,    -0.2,    4.5,    10.8,    15.2,    16.4,    15.2,    10.8,    6.3,    0.7,    -3.1,    5.7]]

dictionaries = {city: temps[x] for x, city in enumerate(cities)}
print(dictionaries)