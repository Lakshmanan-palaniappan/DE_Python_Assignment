from util import second_max
if __name__ == "__main__":
    n = int(input("Enter Size: "))
    arr = []
    for i in range(n):
        temp = int(input(f"Enter Element {i}: "))
        arr.append(temp)
    res = second_max(arr)
    print(res)
