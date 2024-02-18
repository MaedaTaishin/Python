name = "tAishin maEda"
name.capitalize()
print(name.capitalize())
print(len(name))

splitname = name.split()
print(splitname)

firstname = splitname[0]
lastname = splitname[1]
print(firstname)
print(lastname)


b = "Hello, World!"
print(b[2:5])

names = ["Doe, John", "Smith, Jane", "Lee, David"]

# Iterate over the names list and split each name into two parts
for i in range(len(names)):
    parts = names[i].split(", ")
    
    # Re-arrange the parts into the desired format and assign it back to the original list
    names[i] = parts[1] + " " + parts[0]

print(names)

print("Enter a word")
word = input()
print(word == word[::-1])

string = "Supercalifragilisticexpialidocious"
st = print(string.lower())
print(string[0:5])
print(string[9:20])