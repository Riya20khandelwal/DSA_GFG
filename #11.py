'''Given a number N. Your task is to check whether it is fascinating or not.

Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3 ,and when both these products are concatenated with the original number,
then it results in all digits from 1 to 9 present exactly once.'''

#https://practice.geeksforgeeks.org/problems/fascinating-number3751/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions



class Solution:

	def fascinating(self,n):
	    num = sorted(list(map(int, ' '.join(str(n) + str(n*2) + str(n*3)).split())))
	    return num == [1,2,3,4,5,6,7,8,9]
