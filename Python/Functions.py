#q1
mylist = [True, False,False, True,True, False]
newlist = [x for x in mylist if x == True]
print(newlist)

#q2
def funclist(mylist):
    return [x for x in mylist if x == True]
new = funclist(mylist)
print(new)
    
#q3
def triple(original):
    return [x*3 for x in original]

original = [5,89,23,4.6,55,27]
tripled = triple(original)
print(tripled)

#q4
triple1 = lambda original: [x*3 for x in original]
tripled1 = triple1(original)
print(tripled1)

#q5
def findcity(locations):
    return [x for x in locations if x[2] > 1600]

locations = [('San Francisco', 'USA', 1776), ('Tokyo', 'Japan', 1603), ('Helsinki', 'Finland', 1550), ('Sao Paolo', 'Brazil', 1554), ('Ho Chi Minh', 'Vietnam', 1698), ('Mumbai', 'India', 1294)]
city = findcity(locations)
print(city)

#q6
