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
    for product in products:
        print(product["id"], product["name"])

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

def update_product():
    print("UPDATING A PRODUCT")

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
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")


# OVERWRITING INVENTORY CSV FILE

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
