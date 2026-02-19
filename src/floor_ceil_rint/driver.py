from util import print_fcr
import numpy
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        val = float(input(f"Enter element {i+1}: "))
        arr.append(val)
    A = numpy.array(arr, float)
    floor, ceil, rint = print_fcr(A)
    print(floor)
    print(ceil)
    print(rint)
