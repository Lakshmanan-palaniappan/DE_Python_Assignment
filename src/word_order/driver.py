from util import find_word_order
if __name__ == "__main__":
    count = int(input("Enter number of words: "))
    words = []
    for i in range(count):
        word = input("Enter word " + str(i + 1) + ": ").strip()
        words.append(word)

    result = find_word_order(count, words)

    print("Distinct Words:", len(result))
    print("Their Occurrences:", " ".join(str(v) for v in result.values()))
