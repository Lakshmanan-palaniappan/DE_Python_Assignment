def find_percentage(student_marks, query_name):
    if query_name not in student_marks:
        raise ValueError(f"No records found for {query_name}")
    scores = student_marks[query_name]
    return sum(scores) / len(scores)