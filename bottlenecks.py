t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    arr.sort()
    i,j=0,1
    while(i<len(arr) and j<len(arr)):
        if arr[i]<arr[j]:
            arr.pop(i)
            i=0
        elif arr[i]==arr[j]:
            j+=1
    print(len(arr))
