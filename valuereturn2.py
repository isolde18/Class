def main():
    price= get_price()
    sales_price=price - discount_price(price)
    print("The sales price is: ", sales_price)


def get_price():
    price = int(input("Please enter the price: "))
    return price

def discount_price(price):
    sales_price= price*0.10
    return sales_price

main()
