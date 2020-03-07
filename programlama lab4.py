def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=j-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
    arr[j+1]=key

def ShellSort(arr):
    n=len(arr)
    gap=n//2

    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while j>gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap//2
