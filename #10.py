'''Given a array of length N, at each step it is reduced by 1 element. In the first step the maximum element would be removed, 
while in the second step minimum element of the remaining array would be removed, in the third step again the maximum and so on. 
Continue this till the array contains only 1 element. And find the final element remaining in the array.'''

#https://practice.geeksforgeeks.org/problems/print-the-left-element2009/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions


class Solution:
    def leftElement(self, arr, n):
        arr.sort()
        rs = n//2
        if n%2==0:
            return arr[rs-1]
        else:
            return arr[rs]
