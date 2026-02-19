from util import list_operations
if __name__ == '__main__':
    num = int(input("Enter Number of operations: "))
    my_list = []
    for _ in range(num):
        operation = input("Enter operation: ")
        if operation == "insert":
            i = int(input("Index: "))
            e = int(input("Element: "))
            my_list = list_operations(my_list, operation, i, e)
        elif operation in ["remove", "append"]:
            e = int(input("Element: "))
            my_list = list_operations(my_list, operation, e)
        else:
            my_list = list_operations(my_list, operation)
    print("Final list:", my_list)
