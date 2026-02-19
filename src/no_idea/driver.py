from util import calculate_happiness

if __name__ == "__main__":
    n = int(input("Size of array: "))
    arr = []
    for i in range(n):
        element = int(input("Array element " + str(i + 1) + ": "))
        arr.append(element)

    size_a = int(input("Size of liked set: "))
    set_a = set()
    for i in range(size_a):
        liked_element = int(input("Liked element " + str(i + 1) + ": "))
        set_a.add(liked_element)

    size_b = int(input("Size of disliked set: "))
    set_b = set()
    for i in range(size_b):
        disliked_element = int(input("Disliked element " + str(i + 1) + ": "))
        set_b.add(disliked_element)

    score = calculate_happiness(arr, set_a, set_b)
    print("Your Happiness Score is:", score)