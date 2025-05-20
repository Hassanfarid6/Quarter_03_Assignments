# 18. Property Decorators: @property, @setter, and @deleter Assignment:
# Create a class Product with a private attribute _price. Use @property to get 
# the price, @price.setter to update it, and @price.deleter to delete it.


class  Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        del self._price
        print("price deleted")


res = Product(10)
print(res.price)  # output: 10 
res.price = 15
print(res.price)   # output: 15

del res.price     # price deleted
