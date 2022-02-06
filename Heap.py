def swap_and_compare(arr,j):
    le=len(arr)-1
    large=j
    if (j * 2 + 1) <= le and arr[j * 2 + 1] > arr[j]:
        large=j * 2 + 1
    if (j * 2 + 2) <= le and arr[j * 2 + 2] > arr[j] and arr[large]<arr[j*2+2]:
        large = j * 2 + 2
    if arr[large] != arr[j]:
        arr[large], arr[j] = arr[j], arr[large]
        swap_and_compare(arr,large)
    else:
        return

def heapify(arr,j,n):
    large=j
    if (j * 2 + 1) <= n and arr[j * 2 + 1] > arr[j]:
        large=j * 2 + 1
    if (j * 2 + 2) <= n and arr[j * 2 + 2] > arr[j] and arr[large] < arr[j * 2 + 2]:
        large = j * 2 + 2
    if arr[large] != arr[j]:
        arr[large], arr[j] = arr[j], arr[large]
        print(arr,arr[large],arr[j])
        heapify(arr,large,n)
    else:
        return


def heap_sort(arr):
    print(arr)
    i=0;
    leng=len(arr)-1
    while i<=leng:
        arr[0],arr[leng-i] = arr[leng-i],arr[0]
        print(arr)
        heapify(arr,0,leng-i-1)
        print("after sorign: ",arr,i)
        i+=1

if __name__ == '__main__':
    array=[1,2,3,4,5,6,7,8,9,10,11,12,18,99,-11,0,66,-44,-9999,-6,-6,-6,-1,0]
    i=len(array)-1
    while i >= 0:
        swap_and_compare(array,i)
        #print(array)
        i-=1
    print("Array after Sorting:", array)
    heap_sort(array)

