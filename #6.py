#Given a list of names, display the longest name.
#https://practice.geeksforgeeks.org/problems/display-longest-name0853/1?page=1&difficulty[]=-2&category[]=Arrays&sortBy=submissions

class Solution:
    def longest(self, names, n):
        l = 0
        arr = []
        for i in range(n):
            arr.append(len(names[i]))
        m = max(arr)
        i = arr.index(m)
        return names[i]
