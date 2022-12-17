#Given a sorted array Arr of size N and a value X, find the number of array elements less than or equal to X and elements more than or equal to X. 

#https://practice.geeksforgeeks.org/problems/smaller-and-larger4005/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions

class Solution:

	def getMoreAndLess(self,arr, n, x):
		less = 0
		more = 0
		for i in range(n):
		    if x>=arr[i]:
		        less += 1
		    if x<=arr[i]:
		        more += 1
		return less,more
