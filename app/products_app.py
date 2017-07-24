import csv
import operator

products = []

csv_file_path = "data/products.csv"

# READ PRODUCTS CSV

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

#products = sorted(products, key=operator.itemgetter("id"))

def lookup_product(product_id):
    matching_products = [p for p in products if p["id"] == product_id]
    return matching_products[0]

def handle_index_error():
    print("OOPS. There are no products matching the given identifier. Try listing products to see which ones exist.")

def user_inputs_product_id():
    product_id = input("OK. Please specify the product's identifier: ")
    return product_id

def prompt_user_for_product_info():
    print("OK. Please specify the product's information...")

def handle_index_error():
    print("OOPS. There are no products matching the given identifier. Try listing products to see which ones exist.")

def user_inputtable_headers():
    return [header for header in headers if header != "id"]

def auto_increment_id(products):
    product_ids = list(map(map_id, products))
    if len(product_ids) == 0: next_id = 1
    else: next_id = max(product_ids) + 1
    return next_id

headers = ["id", "name", "aisle", "department", "price"]

menu = """
    Hi.

    Welcome to the products app.

    There are {0} products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format(len(products))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def list_products():
    print("THERE ARE", len(products), "PRODUCTS:")
    for product in products:
        print("  +", product) #product["id"], "product["name"], product["aisle"], product["department"], product["price"])

def show_product():
    while True:
        shown_product = input("Please input a product identifier, or 'DONE' if there are no more items: ")
        if shown_product == "DONE":
            break
        else:
            reveal_product = [product for product in products if product["id"] == shown_product]
            print(reveal_product)

def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    product_aisle = input("aisle is:")
    product_department = input("department is:")
    product_price = input("price is:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)

# def update_product():
#     print("UPDATING A PRODUCT")
#     while True:
#         product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
#         if product_id == "DONE":
#             break
#         else:
#             products[:] = [d for d in products if d.get('id') != product_id]
#             product_name = input("name is:")
#             product_aisle = input("aisle is:")
#             product_department = input("department is:")
#             product_price = input("price is:")
#             new_product = {
#                 "id": int(product_id),
#                 "name": product_name,
#                 "aisle": product_aisle,
#                 "department": product_department,
#                 "price": product_price
#                 }
#             #old_product = []
#             #old_product[:] = [d for d in products if d.get('id') == product_id]
#             #products[:] = [d for d in products if d.get('id') != product_id]
#             products.append(new_product)
#             new_list = sorted(products, key=operator.itemgetter("id"))
#             print(new_list)
# #products = sorted(products, key=operator.itemgetter("id"))
#
#             #products = sorted(products, key=operator.itemgetter("id"))

def update_product(products):               #help from Professor Rossetti
    product_id = user_inputs_product_id()
    try:
        product = lookup_product(product_id)
        prompt_user_for_product_info()
        for header in user_inputtable_headers():
            product[header] = input("    Change {0} from '{1}' to: ".format(header, product[header]))
        print("UPDATING A PRODUCT HERE!")
        print(product)
        return product
    except IndexError as e:
        handle_index_error()

def destroy_product():
    print("DESTROYING A PRODUCT")
    product_ids = []
    while True:
        product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
        if product_id == "DONE":
            break
        else:
            destroyed_item = []
            destroyed_item[:] = [d for d in products if d.get('id') == product_id]
            products[:] = [d for d in products if d.get('id') != product_id] #https://stackoverflow.com/questions/1235618/python-remove-dictionary-from-list
            print(destroyed_item)




if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product(products)
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")


# OVERWRITING INVENTORY CSV FILE

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = headers)
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
