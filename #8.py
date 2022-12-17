'''Given an array of size N and you have to tell whether the array is perfect or not. 
An array is said to be perfect if it's reverse array matches the original array. 
If the array is perfect then print "PERFECT" else print "NOT PERFECT".'''

#https://practice.geeksforgeeks.org/problems/perfect-arrays4645/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions



class Solution:
    flag = 0
    def IsPerfect(self,arr,n):
        arr2 = []
        for i in range(n-1,-1,-1):
            arr2.append(arr[i])
        if arr == arr2:
            return True
        else:
            return False
