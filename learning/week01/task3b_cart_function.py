cart1 = [
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
 
]

cart2 = [
    {
    "name": "Ivervid 3mg Ivermectin Tablet",
    "price": 10,
    "quantity": 10,
    },

    {
    "name": "Dolo Tablet",
    "price": 50,
    "quantity": 10,
    }
 
] 

# cart_total = cart1_total + cart2_total 
# cart1_total = 0 
# cart2_total = 0 

# for item in cart1:
#     line_total1 = item['price'] * item['quantity']
#     cart1_total += line_total1

# for item in cart2:
#     line_total2 = item['price'] * item['quantity']
#     cart2_total += line_total2

def calculate_cart_total(cart):
    total = 0
    for item in cart:
        total += item["price"]*item["quantity"]
    return total


cart1_total = calculate_cart_total(cart1)
cart2_total = calculate_cart_total(cart2)
cart_total = cart1_total + cart2_total 


print(cart1_total,cart2_total,cart_total)