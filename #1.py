#Second Largest
#Given an array Arr of size N, print second largest distinct element from an array.
# https://practice.geeksforgeeks.org/problems/second-largest3735/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions

class Solution:

	def print2largest(self,arr, n):
	    arr.sort()
	    m = max(arr)
	    if n < 2:
	        return -1
	    for i in range(n-1,-1,-1):
	        if arr[i] != m:
	            return arr[i]
	            break
	    else:
	        return -1
