import random

# random decimal fromm 0.0 to <1.0
print("The Random modules : random.random value is(0.0 - <1.0) : ",random.random())
# random decimal between a and b
print("Random decimal between a and b(1, 10) : ", random.uniform(1, 10))
# random integer between a and b
print("Random integer between a and b(1, 10) : ", random.randint(1, 10))
# random integer containing k random bits
print("Random integer containing k random bits(0, 20, 2) : ", random.randrange(0, 20, 2))

# pick 1 item
fruits = ["apple", "banana", "mango", "grapes", "guava"]
print()
print("Pick a random choice from the list [apple, banana, mango, grapes, guava] : ", random.choice(fruits))
# pick multiple items, but they can be duplicate
print("Pick a random choice of value from the list with duplicates : ", random.choices(fruits, k=4))
# pick multiple items, but without duplicates
print("Pick a random choice of value from the list without duplicates : ", random.sample(fruits, k=4))

# shuffle the order of the values in the group
print()
print("The correct order of the values with the list : ", fruits)
random.shuffle(fruits)
print("Shuffle the values within the list : ", fruits)

# Simulating an actual transaction event
cities = ["Banglore", "Mumbai", "Delhi", "Chennai"]
transactions = []

# Create a loop of 5 transactions event where they generate random, custoimer id, city, amount in a list, with each transactions in a dictionary
for transaction_id in range(1, 6):
    transaction = {
            "transaction_id" : transaction_id,
            "customerid" : random.randint(1000, 9999),
            "city" : random.choice(cities),
            "amount" : random.randint(100, 10000)
    }

    transactions.append(transaction)

print()
print("The list of generated trnsactions using random module : ")
print(transactions)
