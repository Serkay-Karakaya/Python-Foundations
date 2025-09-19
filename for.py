"""
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)
"""
"""
names = ["seko","beko","ege"]
for name in names :
    print("my name is "+name)
"""
from unicodedata import digit


numbers = [1,3,5,7,9]
"""
for num in numbers:
    if num % 3 == 0: # 3 ün katı 
        print(num)
"""
"""
result = 0
for num in numbers:
    result += num # dizi içinin toplamı
print(result) 
"""
"""
for num in numbers:
    if num % 2 == 1: # tek sayı
        print(num**2)
"""
"""
cities = ["izmir","rize","alanya","manisa","canakkale"]
for city in cities:
    if len(city) <= 5:
        print(city)
"""
products = [
    {"name":"S5", "price":"3000"},
    {"name":"S6", "price":"4000"},
    {"name":"S7", "price":"5000"},
    {"name":"S8", "price":"6000"}
]
"""
total = 0
for product in products:
     price = int (product["price"])
     total += price
print(total)
"""