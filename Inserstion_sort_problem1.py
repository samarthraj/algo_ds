#You are given a list of student objects, each containing the 
#attributes name, roll_number, and marks. You need to sort the list of students based on their marks in descending order using the insertion sort algorithm. 
#If two students have the same marks, their order should be based on their roll_number in ascending order.
def sort_students(students_list): 
    for index in range(1,len(students_list)):
        inner_index_marks = 2
        inner_index_roll = 1
        #print(students_list[index][inner_index])
        value = students_list[index]
        marks_value = students_list[index][inner_index_marks] 
        roll_value = students_list[index][inner_index_roll]
        i = index - 1 
        while i >= 0: 
            if marks_value < students_list[i][inner_index_marks]:
                students_list[i+1] = students_list[i]
                students_list[i] = value
                i = i - 1 
            elif marks_value == students_list[i][inner_index_marks]:
                if roll_value < students_list[i][inner_index_roll]:
                    students_list[i+1] = students_list[i]
                    students_list[i] = value
                i = i - 1 
            else:
                break
    return students_list

students_list = [
    ('Alice', 101, 85),
    ('Bob', 102, 78),
    ('Charlie', 103, 92),
    ('David', 104, 85),
    ('Emma', 105, 92),
    ('Frank', 106, 78),
    ('Bisu', 112, 35),
    ('Aa', 1, 35)]
# its in order Name, Roll No, Marks
results = sort_students(students_list)
print(results)
