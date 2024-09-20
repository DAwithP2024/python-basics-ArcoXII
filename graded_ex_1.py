# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        products_list.sort(key = lambda x : x[1])
        return products_list
    elif sort_order == "desc":
        products_list.sort(key = lambda x : x[1], reverse = True)
        return products_list

def display_products(products_list):
    print("No.\tName\tPrice")
    count = 1
    for name, price in products_list:
        print(f"{count}\t{name}\t{price}")
        count += 1


def display_categories():
    count = 1
    category_selection_flag = True
    for key in products.keys():
        print(count, key)
        count += 1
    while category_selection_flag:
        categories_index = input("Enter the number of category: ")
        try:
            categories_index = int(categories_index) - 1
            return categories_index
        except Exception as e:
            print("Invalid in put, please try again")
            return None

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))


def display_cart(cart):
    total_cost = 0
    count = 1
    for name, price, quantity in cart:
        print(f"{name} - ${price} x {quantity} = ${price*quantity}")
        count += 1
        total_cost = total_cost + (price * quantity)
    print(f"Total cost: ${total_cost}")
    


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Name: {name}\tEmail: {email}\nCart:\n", display_cart(cart), f"\nTotal cost: {total_cost}\nDelivery address: {address}\nThe order will be delivered in 3 days.")


def validate_name(name):
    try:
        name = name.strip().split(' ') 
        if name[0].isalpha() and name[1].isalpha():
            return True
        else:
            return False
    except Exception as e:
        return False


def validate_email(email):
    if email.find('@') != -1:
        return True
    else:
        return False



def main():
    
    cart = []

    print("Welcome! ")

    user_name = input("Please enter your name: ")
    while not validate_name(user_name):
        user_name = input("Invalid name, please enter your name again: ")
        

    e_mail_address = input("Please enter your e-mail address: ")
    while not validate_email(e_mail_address):
        e_mail_address = input("Invalid email adress, please enter your e-mail address again:")
    
    arr_categories = []
    for key in products.keys():
        arr_categories.append(key)

    category_index = display_categories()


    shopping_flag = True
    display_product_flag = True

    while shopping_flag:

        while display_product_flag:
            try:
                if category_index < len(products) and category_index > -1:
                    display_product_flag = False
                    display_products(products[arr_categories[category_index]])
                else:
                    print("Invalid input, please try again.")
                    continue
            except Exception as e:
                print("Invalid input, please try again!")
                continue

        option = input("""1. Select a product to buy
2. Sort the products according to the price.
3. Go back to the category selection.
4. Finish shopping
>""")
        try:
            option = int(option)
        except Exception as e:
            print("Invalid input, please try again.")
            continue
        if option == 1:
            product_number = int(input("Enter the number corresponding to the product: "))
            quantity = int(input("Enter the quantity you want to buy: "))
            product = [products[arr_categories[category_index]][product_number - 1]]
            add_to_cart(cart, product, quantity)
            continue
        elif option == 2:
            sort_order = input("Sorting ascending(asc) or descending(desc): ")
            print(display_sorted_products(products[arr_categories[category_index]], sort_order))
            continue
        elif option == 3:
            category_index = display_categories()
            display_product_flag = True
            continue
        elif option == 4:
            if cart == []:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day")
            else:
                total_cost = display_cart(cart)
                delivery_address = input("Please enter your delivery address: ")
                generate_receipt(user_name, e_mail_address, cart, total_cost, delivery_address)
            shopping_flag = False
            break
        
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
