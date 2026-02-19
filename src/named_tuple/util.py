from collections import namedtuple

def named_tuple(n, columns=None, data=None):
    if columns is None:
        print("Enter column names one by one:")
        col_count = int(input("How many columns? "))
        columns = []
        for i in range(col_count):
            col = input(f"  Column {i+1} name: ").upper()
            columns.append(col)
    Student = namedtuple("Student", columns)
    if data is None:
        records = []
        for i in range(n):
            print(f"Enter details for student {i+1}:")
            values = []
            for col in columns:
                val = input(f"  {col}: ")
                values.append(val)
            records.append(Student(*values))
    else:
        records = [Student(*row) for row in data]
    total_marks = sum(int(record.MARKS) for record in records)
    average = total_marks / n
    print(f"Average: {average:.2f}")
    return average