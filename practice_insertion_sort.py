def insertion_sort(list): 
 #print(' '.join([str(i) for i in arr]))  use this for hacker rank 
    for index in range(1,len(list)): 
        value = list[index]
        i = index - 1 
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break
    return list

list = [3,5,10,40,12,1]
#list = ['sam', 'apple', 'banana', 'date', 'fig','samosa', 'cherry']
#list = ['B', 'Z', 'L', 'A', 'C', 'c', 'a']
#tuples_list = [(1, 'banana'), (3, 'apple'), (2, 'cherry'), (5, 'date'), (4, 'fig')]
#dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]

result = insertion_sort(list)
print(result) 

