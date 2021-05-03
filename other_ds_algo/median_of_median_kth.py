
"""
Problem: find the k'th order statistic. (Note: k could be n//2 and this is to get median or some other percentile)

Methods:

1. Onlogn: sort array
2. Use min heap: get heap of n; pop k times O(n+klogn)
3. Use max heap: the sol I apply: O(nlogk)
4. Quick select: pivot is last elem: the select with pivot method O(n**2) but most of time O(n); assume distinct elems.
5. Expected linear time quick select: pivot select randomly (method from bootcamp); that is why swap to first elem; it mimics this "last elem picked as pivot"
- really it mimics a "fisrt element oicked as pivot"
6. For worst case O(n) - median of medians to pick pivot


N
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-3-worst-case-linear-time/
# this is buggy - just this is the general idea.

"""

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         """makes the assumption arrays are distinct; Implement median of medians
        
#         Key point; select pivot for O(n) worst case time.
#         Pivot = median(arr of median(1/5th chunks))
        
#         """ 
#         def _get_median(a, left, n):
#             """get median of a small chunk left to left+n in array a"""
#             arr = a[left:left+n]
#             arr.sort()
#             return arr[n//2]
        
#         def _partition(a, left, right, pivot):
#             """swaps with right elem in the partition process"""
#             # find pivot
#             for i in range(left, right): # notice right not included here
#                 if pivot == a[i]:
#                     a[i], a[right] = a[right], a[i]
#                     break
#             # swap right elem with pivot elem
#             x = a[right]
#             i = left # this is the cloud boundary
#             # partitions array comparing to right elem
#             # this is easier because this way we do one cloud bounary progress
#             # rather then the full dnf as in the bootcamp
#             for j in range(left, right):
#                 if a[j] <= x:
#                     a[i], a[j] = a[j], a[i]
#                     i += 1
#             a[i], a[right] = a[right], a[i]
            
#             return i
        
#         def _kthsmallest(a, left, right, k):
#             """this is used to get the actual kth order stat
#             - note that to get the median of medians pivot it is called recursive
#             General:
#             1. Split in len 5 arrays
#             2. Get medians; consider incomplete last chunk
#             3. Recu _kth to get medOfmedians
#             4. Use as pivot to partition
#             5. return or call on lower half or upper half
#             """
            
#             if 0 < k < right - left + 1:
#                 n = right - left + 1
                
#                 medians = []
#                 i = 0
#                 while i < n// 5:
#                     medians.append(_get_median(a, left+i*5, 5))
#                     i += 1
                    
#                 if i * 5 < n: # last chunk
#                     medians.append(_get_median(a, left + i*5, n%5))
#                     i += 1
                    
#                 if i == 1:
#                     medofmed = medians[i-1]
#                 else:
#                     medofmed = _kthsmallest(medians, 0, i-1, i//2)
#                     #pivot
                    
#                 pos = _partition(a, left, right, medofmed)
#                 if pos - 1 == k - 1:
#                     return a[pos]
#                 if pos - 1 > k - 1:
#                     return _kthsmallest(a, left, pos - 1, k)
#                 return _kthsmallest(a, pos + 1, right, left + k - pos - 1)
                
            
#             return 999999999999
            
            
#         return _kthsmallest(nums, 0, len(nums)-1, k)
            
            




    return n 
# the geeks version is not correct or at least it has clumsy python code; this works though


    

def main():
    

if __name__ == '__main__':

    main()
    
        













