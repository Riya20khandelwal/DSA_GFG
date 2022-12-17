#Given an array Arr of size N, swap the Kth element from beginning with Kth element from end.
#https://practice.geeksforgeeks.org/problems/swap-kth-elements5500/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions

class Solution:
	
	def swapKth(self,arr, n, k):
		arr[k-1], arr[n-k] = arr[n-k], arr[k-1]
		return arr
