# MERGE SORT 
>Merge sort is a divide-and-conquer algorithm based on the idea of breaking down a list into several sub-lists until each sublist consists  >of a single element and merging those sublists in a manner that results into a sorated list.

>It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used >for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two >sorted sub-arrays into one.
 
 ![example image](https://github.com/avikjain02/5-lang-polyglot/blob/master/Images/mergesort.jpg)

## Pseudocode
MergeSort(arr[], l,  r)
If r > l
1. Find the middle point to divide the array into two halves:<br>
`middle m = (l+r)/2`
2. Call mergeSort for first half:<br>
`Call mergeSort(arr, l, m)`
3. Call mergeSort for second half:<br>
`Call mergeSort(arr, m+1, r)`
4. Merge the two halves sorted in step 2 and 3:<br>
`Call merge(arr, l, m, r)`

## Algorithm
`void merge(int arr[],int start, int mid, int end)
    {
    //make temporary variable to store starting index of both the arrays
    int p = start, q = mid +1;
    
    }
`
