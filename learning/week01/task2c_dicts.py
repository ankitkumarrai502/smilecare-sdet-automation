product = {
    "name": "Primobol Methelone Enanthate",
    "price": 10724.20,
    "stock": 85,
    "category": "METHENOLONE ENANTHATE",
    "brand_name": "PRIMOBOL",
}

print(product["name"])          
print(product.get("price"))    
product["stock"] = 80           
product["in_stock"] = product["stock"] > 0  

for key, value in product.items():
    print(f"{key}: {value}")