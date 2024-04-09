#You are given a list of integers representing the arrival time of tasks in a queue. Each task has a priority level represented by a positive integer. Your task is to reorder the tasks based on their priority levels using the insertion sort algorithm. If two tasks have the same priority level, their order should be based on their arrival time in ascending order.
#Write a program that implements the insertion sort algorithm to reorder the tasks according to the specified criteria and prints the reordered list as output.

def insertion_sort(tasks): 
    priority_index = 1
    time_index = 0
    for index in range(1,len(tasks)):
        value_whole = tasks[index]
        value_p_index = tasks[index][priority_index]
        value_t_index = tasks[index][time_index]
        i = index - 1 
        while i >= 0: 
            if value_p_index < tasks[i][priority_index]: 
                tasks[i+1] = tasks[i] 
                tasks[i] = value_whole
                i = i - 1 
            elif value_p_index == tasks[i][priority_index]: 
                if value_t_index < tasks[i][time_index]: 
                    tasks[i+1] = tasks[i]
                    tasks[i] = value_whole
                i = i - 1 
            else:
                break
    return tasks

tasks = [
    (1, 3),  # Task 1 arrived at time 1 with priority level 3
    (2, 2),  # Task 2 arrived at time 2 with priority level 2
    (3, 1),  # Task 3 arrived at time 3 with priority level 1
    (4, 3),  # Task 4 arrived at time 4 with priority level 3
    (5, 2),  # Task 5 arrived at time 5 with priority level 2
    (1, 4),
    (10, 4),
    (3, 4),
    (4, 4)
]
result = insertion_sort(tasks)
print(result) 