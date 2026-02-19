from util import find_percentage
if __name__ == '__main__':
    n = int(input("Enter Count: "))
    student_marks = {}
    for _ in range(n):
        name = input("Enter student name: ")
        count = int(input(f"How many scores for {name}? "))
        scores = []
        for i in range(count):
            score = float(input(f"Enter score {i+1}: "))
            scores.append(score)
        student_marks[name] = scores
    query_name = input("Enter query name: ")
    try:
        result = find_percentage(student_marks, query_name)
        print(f"Query result: {result:.2f}")
    except Exception as e:
        print(e)