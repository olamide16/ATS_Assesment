shopping_cart = {
    "jean": {"name": "jean", "quantity":5, "size": "xl", "price": 5000},
    "top": {"name": "top", "quantity": 3, "size": "xxl", "price": 2500}
}


def add_item():
    new_value ={}
    new_value['name'] = input("Enter the name of the item: ")
    new_value['quantity'] = int(input('quantity: '))
    new_value['size'] = input("Enter yoor size : ")
    new_value['price'] = int(input("enter the price :  "))
    shopping_cart[new_value['name']] = new_value
    print(shopping_cart)
# add_item()


def remove_item():
    name = input("Enter the name of the item: ")
    del shopping_cart[name]
    print(shopping_cart)
# remove_item()


def update_item():
    name = input("Enter the item name: ")
    # new_name = input('Enter the new item: ')
    shopping_cart[name] = input('Enter the new item: ')
    # shopping_cart[name] = shopping_cart[name]
    shopping_cart[name]['price'] = int(input("Enter the new price: "))
    shopping_cart[name]['size'] = input("Enter the your size: ")
    shopping_cart[name]['quantity'] = int(input("Enter the new quantity: "))
    # shopping_cart[name] = shopping_cart[name]['name']
    print(shopping_cart)
update_item()

def main():
    option = input("""Enter
                   1 - add new item
                   2- remove item 
                   3- update item): """)
    if option == '1':
        add_item()
    elif option == '2':
        remove_item()
    else:
        update_item()
if __name__ == "__main__":

    main()