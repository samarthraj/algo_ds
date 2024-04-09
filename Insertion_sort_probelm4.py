# You are given a list of employees with their names, departments, and salaries. Your task is to sort the list of employees based on the department in lexicographic (alphabetical) order first. If two employees are from the same department, their order should be based on their salaries in descending order.
# Write a program that implements the insertion sort algorithm to sort the list of employees according to the specified criteria and prints the sorted list as output.
def department_salary_sort(list2, list1):
    department_name2, salary2 = list2[1], list2[2]
    department_name1, salary1 = list1[1], list1[2]
    # print(department_name2, salary2, department_name1, salary1)
    if department_name2 != department_name1:
        return department_name2 < department_name1
    else:
        return salary2 > salary1


def insertion_sort_employees(employees_list):
    for index in range(1, len(employees_list)):
        value = employees_list[index]
        i = index - 1
        while i >= 0 and department_salary_sort(value, employees_list[i]):
            employees_list[i+1] = employees_list[i]
            employees_list[i] = value
            i = i - 1
    return employees_list

# def compare_employees(emp1, emp2):
#     dept1, salary1 = emp1[1], emp1[2]
#     dept2, salary2 = emp2[1], emp2[2]

#     if dept1 != dept2:
#         return dept1 < dept2
#     else:
#         return salary1 > salary2  # Compare salaries in descending order if departments are the same


# def insertion_sort_employees(employees):
#     for i in range(1, len(employees)):
#         key = employees[i]
#         j = i - 1
#         while j >= 0 and compare_employees(key, employees[j]):
#             employees[j + 1] = employees[j]
#             j -= 1
#         employees[j + 1] = key
#     return employees
employees_list = [
    ("Alice", "HR", 50000),
    ("Bob", "Finance", 60000),
    ("Charlie", "IT", 55000),
    ("David", "Finance", 70000),
    ("Emma", "IT", 45000),
    ("Frank", "HR", 48000),
]

res = insertion_sort_employees(employees_list)
print(res)
