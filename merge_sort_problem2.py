def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recurresion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # do your actual merge
        i = 0  # left index
        j = 0  # right index
        k = 0  # merge index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return (arr)


arr = [8, 4, 2, 1]
res = merge_sort(arr)
print(res)
