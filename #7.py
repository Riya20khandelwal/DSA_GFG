'''Given an unsorted array Arr[] of N integers and a Key which is present in this array.
You need to write a program to find the start index( index where the element is first found from left in the array ) and
end index( index where the element is first found from right in the array ).If the key does not exist in the array then return -1 for both start 
and end index in this case.'''

#https://practice.geeksforgeeks.org/problems/find-index4752/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions

class Solution:
    def findIndex (self,a, N, key ):
        arr = []
        if key not in a:
            rs = [-1 , -1]
            return rs
        else:
            for i in range(N):
                if a[i] == key:
                    arr.append(i)
            rs = [arr[0], arr[-1]]
        return rs
