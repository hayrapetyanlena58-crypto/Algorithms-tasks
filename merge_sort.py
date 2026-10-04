def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    out=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<= right[j]:
            out.append(left[i])
            i+=1
        else:
            out.append(right[j])
            j += 1
    out += left[i:]
    out += right[j:]
    return out
            
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
