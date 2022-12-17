'''Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. 
Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.'''
#https://practice.geeksforgeeks.org/problems/palindromic-array-1587115620/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions



def PalinArray(arr ,n):
    flag = 1
    for i in range(n):
        if flag == 1:
            num = arr[i]
            temp = num  
            rev = 0  
            while(num > 0):  
                dig = num % 10  
                rev = rev * 10 + dig  
                num = num // 10  
            if(temp == rev):
                flag = 1
            else :
                flag = 0
    return flag
