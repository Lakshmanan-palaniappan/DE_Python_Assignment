from util import time_delta

if __name__ == "__main__":
    count = int(input("Enter Count: "))
    results = []
    for i in range(count):
        t1 = input("Enter first time: ")
        t2 = input("Enter second time: ")
        delta = time_delta(t1, t2)
        results.append(delta)
    with open("output.txt", "w") as fptr:
        for i in results:
            fptr.write(i+ "\n")