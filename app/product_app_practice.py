import csv

# Read CSV file

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) #each row will be dictionary like
    for row in reader:
        products.append(row)



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
            shown_product = [product for product in products if product["id"] == shown_product]
            shown_product = list(shown_product) #FIX
            print(shown_product) #FIX


def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    product_aisle = input("aisle is:")
    product_department = input("department is:")
    product_price = input("price is:")
    new_prodcut = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODCUT IS", new_prodcut)
    products.append(new_prodcut)


destroyed_ids = []
def destroy_product():
    print("DESTROYING A PRODUCT")
    while True:
        destroyed_products = input("Please input a product identifier, or 'DONE' if there are no more items: ")
        if destroyed_products == "DONE":
            break
        else:
            destroyed_ids.append(int(destroyed_products)
                #print(destroyed_ids)
            #del products["id"] if products["id"] == destroyed_ids
            # destroyed_products = [product for product in products if product["id"] == destroyed_products]
            # del

# def update_product():
#     print("UPDATING A PRODUCT")
    # while True:
    #     shown_product = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    #     if shown_product == "DONE":
    #         break
    #     else:
    #         changed_product = [product for product in products if product["id"] == update_product]
    #         changed_product = list(matching_products) #FIX
    #         print(matching_products) #FIX


if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
