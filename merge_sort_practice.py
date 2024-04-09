def merge_sort(arr):
    #Split your array
    if len(arr) > 1: 
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #do recursion on all the arrays and sub arrays that are split 
        merge_sort(left_arr)
        merge_sort(right_arr)

        #actual merge, where we compare left most elements of both the lists
        i = 0 #index of left arr 
        j = 0 # index of right arr
        k = 0 #index of merged arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
                k = k + 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    return arr

arr = [2,4,3,5,6,1,7,0,3] 
res = merge_sort(arr)
print(res)