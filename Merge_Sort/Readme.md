# MERGE SORT 
>Merge sort is a divide-and-conquer algorithm based on the idea of breaking down a list into several sub-lists until each sublist consists  of a single element and merging those sublists in a manner that results into a sorated list.

>It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
 
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
>MergeSort(A, p, r)
  If p > r 
     return;
     mergeSort(A, q+1, r)
     merge(A, p, q, r)

>void merge(int A[], int p, int q, int r)
    {
    /* Create L ← A[p..q] and M ← A[q+1..r] */
    int n1 = q - p + 1;
    int n2 =  r - q;
 
    int L[n1], M[n2];

    for (i = 0; i < n1; i++)
        L[i] = A[p + i];
    for (j = 0; j < n2; j++)
        M[j] = A[q + 1 + j];
    
    /* Maintain current index of sub-arrays and main array */
    int i, j, k;
    i = 0; 
    j = 0; 
    k = p; 


    /* Until we reach either end of either L or M, pick larger among elements L and M and place them in the correct position at A[p..r] */
    while (i < n1 && j < n2)
    {
        if (L[i] <= M[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = M[j];
            j++;
        }
        k++;
    }
 
    /* When we run out of elements in either L or M, pick up the remaining elements and put in A[p..r] */
    while (i < n1)
    {
        A[k] = L[i];
        i++;
        k++;
    }
 
    while (j < n2)
        {
        A[k] = M[j];
        j++;
        k++; }
    }
### Foot Notes
With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms.
