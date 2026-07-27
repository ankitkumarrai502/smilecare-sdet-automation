cart = [
    {
    "name": "Primobol Methelone Enanthate",
    "price": 10724.20,
    "quantity": 10
    },

    {
    "name": "Anavar Oxandrolone Tablets",
    "price": 95.65,
    "quantity": 10
    },

    {
    "name": "Ivervid 3mg Ivermectin Tablet",
    "price": 24.15,
    "quantity": 10,
    }
]

print()

total = 0
for item in cart : 
    line_total = item['price'] * item['quantity']
    print(f"{item["name"]}: {line_total}")
    total += line_total

print(total)