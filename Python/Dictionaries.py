#q1
dictionaries = {
    'Taishin': {
        'firstname' : 'Taishin',
        'lastname' : 'Maeda',
        'age' : 20,
        'hobby' : 'Sports'
    },
     'Hiro': {
        'firstname' : 'Hiroaki',
        'lastname' : 'Nagai',
        'age' : 21,
        'hobby' : 'dance'
    },
     'Sihun': {
        'firstname' : 'Sihun',
        'lastname' : 'Chei',
        'age' : 22,
        'hobby' : 'boxing'
    },
}

#q2
for name, info in dictionaries.items():
    firstname = info['firstname']
    lastname = info['lastname']
    age = info['age']
    hobby = info['hobby']

    print(f"This is {firstname} {lastname}, "
          f"he/she is {age} years old and likes {hobby}.")
print('\n')

#q4
dictionaries2 = {
    'Taishin': {
        'firstname' : 'Taishin',
        'lastname' : 'Maeda',
        'age' : 20,
        'hobby' : 'Sports'
    },
     'Hiro': {
        'firstname' : 'Hiroaki',
        'lastname' : 'Nagai',
        'age' : 21,
        'hobby' : 'dance'
    },
     'Sihun': {
        'firstname' : 'Sihun',
        'lastname' : 'Chei',
        'age' : 22,
        'hobby' : 'boxing'
    },
    'Simon' : {
        'firstname' : 'Simon'
    }  
}
for name2, info2 in dictionaries2.items():
    firstname = info2['firstname']
    lastname = info2.get('lastname', '')
    hobby = info2.get('hobby', '')
    try:
        age = info2['age']
        print(f"This is {firstname} {lastname}, "
          f"he/she is {age} years old and likes {hobby}.")
    except KeyError:
        print(f"This is {firstname} {lastname}, "
              f"and we do not have information about their age or hobby.")
print('\n')

#q5


#q6
from collections import defaultdict
import random
inventory = defaultdict(dict)

inventory['Game 1'] = {'stock': random.randint(0, 10), 'price': 50}
inventory['Game 2'] = {'stock': random.randint(0, 10), 'price': 100}
inventory['Game 3'] = {'stock': random.randint(0, 10), 'price': 38}

for game, details in inventory.items():
    stock = details['stock']
    price = details['price']
    print(f"Game: {game}, Stock: {stock}, Price: ${price}")

inventory['Game 1']['stock'] = random.randint(0, 10)
inventory['Game 2']['stock'] = random.randint(0, 10)
inventory['Game 3']['stock'] = random.randint(0, 10)


print("\nUpdated Inventory:")
for game, details in inventory.items():
    stock = details['stock']
    price = details['price']
    print(f"Game: {game}, Stock: {stock}, Price: ${price}")
print('\n')

#q7
order = {
    'Game 1': 5,
    'Game 2': 1,
    'Game 7': 6,
}

#q8
print("Initial Inventory:")
for game, details in inventory.items():
    stock = details['stock']
    price = details['price']
    print(f"Game: {game}, Stock: {stock}, Price: ${price}")

total_cost = 0
for game, quantity in order.items():
    if game in inventory and quantity <= inventory[game]['stock']:
        price = inventory[game]['price']
        total_cost += price * quantity
        inventory[game]['stock'] -= quantity

print("\nUpdated Inventory:")
for game, details in inventory.items():
    stock = details['stock']
    price = details['price']
    print(f"Game: {game}, Stock: {stock}, Price: ${price}")

print("\nTotal Cost:", total_cost)