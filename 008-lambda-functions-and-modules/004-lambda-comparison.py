apply_discount_lambda = lambda price, discount: price * (1 - discount)


def apply_discount_def(price, discount):
    mult = 1 - discount  # Permite varias lineas de codigo
    return price * mult


print(apply_discount_lambda(100, 0.2))  # 80.0
print(apply_discount_def(100, 0.2))     # 80.0
