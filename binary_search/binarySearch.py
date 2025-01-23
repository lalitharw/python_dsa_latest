def binarySearch(arr,target):
    l = 0
    r = len(arr) - 1

    
    while(l <= r):
        mid = (l  + r) // 2
        if(arr[mid] > target):
            r = mid - 1
        elif(arr[mid] < target):
            l = mid + 1
        else:
           return arr[mid]

    return -1


print(binarySearch([1,2,3,4,5,6,7,8,9],3))
