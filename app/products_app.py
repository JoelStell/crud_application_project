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

# example of manipulating/changing the products list
# example_new_product = {"id": 100, "name": "New Item", "aisle": "snacks", "department": "snacks", "price":1.99}
# products.append(example_new_product)




other_path = "data/other_products.csv"
with open(other_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)

    # writer.writerow({"city": "New York", "name": "Yankees"})
    # writer.writerow({"city": "New York", "name": "Mets"})
    # writer.writerow({"city": "Boston", "name": "Red Sox"})
    # writer.writerow({"city": "New Haven", "name": "Ravens"})

# chosen_operation = input(menu)
# chosen_operation = chosen_operation.title()
#
# def list_products():
#     print("LISTING PRODUCTS")
#
# def show_product():
#     print("SHOWING A PRODUCT")
#
# def create_product():
#     print("CREATING A PRODUCT")
#
# def update_product():
#     print("UPDATING A PRODUCT")
#
# def destroy_product():
#     print("DESTROYING A PRODUCT")
#
# if chosen_operation == "List": list_products()
# elif chosen_operation == "Show": show_product()
# elif chosen_operation == "Create": create_product()
# elif chosen_operation == "Update": update_product()
# elif chosen_operation == "Destroy": destroy_product()
# else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
