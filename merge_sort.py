def merge_sort(arr):
    if len(arr) > 1: 
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #do recursion, for all the numbers that are split 
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge the two lists that are sorted 
        i = 0 #left arr index
        j = 0 #right arr index
        k = 0 #merged arr index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1 
                k = k + 1 
            else:
                arr[k] = right_arr[j]
                j = j + 1
                k = k + 1
        while i < len(left_arr): 
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    return arr

arr = [2,4,3,5,6,1,7,0,3] 
res = merge_sort(arr)
print(res)


