# def add(n1, n2):
#     return n1 + n2
# my_fav_operation = add
# print(my_fav_operation(4, 2))
# 3 functions multiple,divide,subtract

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# operation 4*8
print(operations["*"](4, 8))

