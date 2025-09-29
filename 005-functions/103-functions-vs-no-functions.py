# Example - Rating calculation for two products

rating_1 = 4.5  # star rating out of 5
sales_1 = 1000  # number of sales
returns_1 = 50  # number of returns
price_1 = 20.0  # price in dollars

rating_2 = 4.0
sales_2 = 1500
returns_2 = 30
price_2 = 25.0

# Example without functions - hard to read and not reusable

score_1 = ((rating_1 * 20) + (sales_1 / (1 + returns_1))) / price_1
score_2 = ((rating_2 * 20) + (sales_2 / (1 + returns_2))) / price_2

# Example with functions - cleaner and more reusable


def rating_comps(rating):
    return rating * 20


def sales_comps(sales, returns):
    return sales / (1 + returns)


def product_score(rating, sales, returns, price):
    comps = rating_comps(rating) + sales_comps(sales, returns)
    return comps / price


score_1 = product_score(rating_1, sales_1, returns_1, price_1)
score_2 = product_score(rating_2, sales_2, returns_2, price_2)
