from Clasess.Product import Product
class Cart:
    def __init__(self):
        self.products = [
            Product("Jabłko", 2.50, 3),
            Product("Chleb", 5.00, 1),
            Product("Mleko", 3.20, 2)
        ]

    def __str__(self):
        if not self.products:
            return "Koszyk jest pusty."

        info = "Zawartość koszyka:\n"
        for p in self.products:
            info += f"- {p.name}: {p.quantity} szt.\n"
        return info.strip()

    def __len__(self):
        return sum(p.quantity for p in self.products)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.products):
            product = self.products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration

    def add(self, name):
        for product in self.products:
            if product.name == name:
                product.quantity += 1
                return

    def remove(self, name):
        for product in self.products:
            if product.name == name:
                if product.quantity > 0:
                    product.quantity -= 1
                return

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def show_cart(self):
        print("Obecny stan koszyka:")
        for product in self.products:
            print(f"- {product}")
        print(f"Całkowita wartość: {self.total_price():.2f} zł\n")
