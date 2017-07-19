print("----------------------------------")
print("PRODUCTS APPLICATION")
print("----------------------------------")
print("Welcome joelstell" + "\n")

menu = """
    Hi.
    Welcome to the products app.

    There are 100 products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation
    """


chosen_operation = input(menu)


if chosen_operation.title() == 'List':
    print("LISTING PRODUCTS")

elif chosen_operation.title() == 'Show':
    print('SHOWING A PROUDCT')

elif chosen_operation.title() == 'Create':
    print('CREATING A PROUDCT')

elif chosen_operation.title() == 'Update':
    print('UPDATING A PROUDCT')

elif chosen_operation.title() == 'Destroy':
    print('DESTROYING A PROUDCT')

else:
    print("OPPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS")
