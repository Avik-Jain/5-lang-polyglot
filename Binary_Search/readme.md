Binary search is the most popular Search algorithm.It is efficient and also one of the most commonly used techniques that is used to solve problems.
Binary search works only on a sorted set of elements. To use binary search on a collection, the collection must first be sorted.
When binary search is used to perform operations on a sorted set, the number of iterations can always be reduced on the basis of the value that is being searched.

Algorithm
int binarySearch(int low,int high,int key)
{
   while(low<=high)
   {
     int mid=(low+high)/2;
     if(a[mid]<key)
     {
         low=mid+1;
     }
     else if(a[mid]>key)
     {
         high=mid-1;
     }
     else
     {
         return mid;
     }
   }
   return -1;                //key not found
 }

Time Complexity:
The time complexity of Binary Search can be written as

T(n) = T(n/2) + c 
