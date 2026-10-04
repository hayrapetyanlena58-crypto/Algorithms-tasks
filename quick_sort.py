def quick_sort(arr):
    if len(arr)<1:
        return arr
    left=[]
    middle=[]
    right=[]
    pivot=arr[len(arr)//2]
    for x in arr:
        if x<pivot:
            left.append(x)     
        elif x==pivot:
            middle.append(x)
        else:
            right.append(x)
    return(quick_sort(left)+middle+quick_sort(right))
arr=[8,15,9,8,27,34,12]
print(quick_sort(arr))
