l= list(map(int,input("Enter the elements for selection sort: ").split()))

def SelectionSort(l):
    for start in range(len(l)):
        minpos = start

        for i in range(start,len(l)):
            if l[i] < l[minpos]:
                minpos = i
                (l[start],l[minpos]) = (l[minpos],l[start])
SelectionSort(l)
print("Sorted Array : ",l)