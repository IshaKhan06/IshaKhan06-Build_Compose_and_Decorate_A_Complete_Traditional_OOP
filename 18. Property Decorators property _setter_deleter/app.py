'''Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.'''

class Product:
    def __init__(self, price):
        self._price = price  

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price can't be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

product = Product(200)
print(f"Price: {product.price}")  # Getting the price using the @property decorator

product.price = 220  # Setting the price using the @price.setter
print(f"Updated Price: {product.price}")

del product.price  # Deleting the price using the @price.deleter
