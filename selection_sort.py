def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j 
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[29,10,14,37,3,17,25]
print(selection_sort(arr))
