def list_operations(my_list, operation, *args):
    if operation == "insert":
        i, e = int(args[0]), int(args[1])
        my_list.insert(i, e)
    elif operation == "print":
        print(my_list)
    elif operation == "remove":
        e = int(args[0])
        my_list.remove(e)
    elif operation == "append":
        e = int(args[0])
        my_list.append(e)
    elif operation == "sort":
        my_list.sort()
    elif operation == "pop":
        my_list.pop()
    elif operation == "reverse":
        my_list.reverse()
    return my_list