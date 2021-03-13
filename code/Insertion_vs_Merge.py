import timeit
import math
import sys
import collections




def InsertionSort(array):
    index = 1
    while index < len(array):
        key = A[index]
        # insert
        i = index - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i+1] = key
        index += 1


def Merge(array,p,q,r):
    n_1 = q - p + 1
    n_2 = r - q
    L = [0]*(n_1+1)
    R = [0]*(n_2+1)
    i = 1
    j = 1
    while i < n_1:
        L[i] = array[p + i - 1]
        i += 1
    while j < n_2:
        R[j] = array[q+j]
        j+=1
    L[n_1] = sys.maxsize
    R[n_2] = sys.maxsize
    i = 0
    j = 0
    k = p
    while k < r:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1



def MergeSort(array,p,r):
    if p < r:
        q = math.floor((p + r)/2)
        MergeSort(array,p,q)
        MergeSort(array,q+1,r)
        Merge(array,p,q,r)

j = 0
max_i = 0
frequency_array = []   
while j < 100:             
    i = 1
    while i < (sys.maxsize / 5):
        A = [5,2,4,3,6,8,1]*i
        B = [5,2,4,3,6,8,1]*i
        start_1 = timeit.default_timer()
        InsertionSort(A)
        stop_1 = timeit.default_timer()
        start_2 = timeit.default_timer()
        MergeSort(B,0,len(B))
        stop_2 = timeit.default_timer()
        # print(A)
        InsertionSort_Time = stop_1 - start_1
        MergeSort_Time = stop_2 - start_2
        # print('Insertion Sort Time: ', InsertionSort_Time)
        # print('Merge Sort Time: ', MergeSort_Time)
        if InsertionSort_Time <= MergeSort_Time:
            # print('Insertion Sort is faster')
            # print('i = ', i)
            max_i = i
        else:
            # print('Merge Sort is faster')
            # print('i = ', i)
            max_i = i
            frequency_array.append(max_i)
            break
        i += 1
       
    j += 1

print('Max i is: ', max_i)
counter = collections.Counter(frequency_array)
print(counter)
