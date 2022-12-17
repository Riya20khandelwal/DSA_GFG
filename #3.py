#Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)
#https://practice.geeksforgeeks.org/problems/sum-of-series2811/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions



class Solution:

	
	def seriesSum(self,n):
        avg = (1+n)/2
        sum = int(avg * n)
        return sum
