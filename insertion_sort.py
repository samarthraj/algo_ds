def insertion_sort(list): 
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

    # for i in range(1,len(list)): 
    #     j = i 
    #     while list[j - 1] > list[j] and j > 0: 
    #         list[j-1], list[j] = list[j], list[j-1] 
    #         j = j - 1
    # return list

list = [2,5,1,6,10,3]
result = insertion_sort(list)  
print(result)


