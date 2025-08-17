class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Catalog:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.code] = product

    def get_product(self, code):
        return self.products.get(code, None)

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items)

    def receipt(self):
        lines = ["RECEIPT:"]
        for item in self.items:
            p = item['product']
            lines.append(f"{p.name} x{item['quantity']} @ ${p.price:.2f} = ${p.price * item['quantity']:.2f}")
        lines.append(f"TOTAL: ${self.total():.2f}")
        return '\n'.join(lines)

def main():
    catalog = Catalog()
    # Sample products
    catalog.add_product(Product('001', 'Apple', 0.5))
    catalog.add_product(Product('002', 'Banana', 0.3))
    catalog.add_product(Product('003', 'Orange', 0.7))

    cart = Cart()

    print("Welcome to Simple POS System")
    while True:
        code = input("Enter product code (or 'done' to finish): ").strip()
        if code == 'done':
            break
        product = catalog.get_product(code)
        if not product:
            print("Product not found!")
            continue
        try:
            quantity = int(input(f"Enter quantity for {product.name}: "))
        except ValueError:
            print("Invalid quantity!")
            continue
        cart.add_item(product, quantity)
        print(f"Added {quantity} x {product.name} to cart.")

    print("\n" + cart.receipt())

if __name__ == '__main__':
    main()
