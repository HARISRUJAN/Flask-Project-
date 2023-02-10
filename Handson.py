# 1) Given an array A[] and a number x, check for pair in A[] with sum as x
	
# 	Input: A[] = [-5, 1, -40, 30, 6, 8, 7 ], K=15
# Output: 7, 8 is the pairs with sum 15

# Input: A[] = [-5, 4, -2, 16, 8, 9], K=15
# Output: There is no pair of elements whose sum is equal to 15

l=[6, 1, -40, 30, 3, 8, 7 ]
dl=l
for i in l:
    remaining=10-i
    if remaining in dl:
        print(remaining ,"and ",i,"are pairs")
        dl.remove(remaining)
        



# 2) Find the missing number in an array 
# Given an array of n-1 distinct integers in the range of 1 to n, find the missing number in it in linear time. 
# For example, consider an array {1, 2, 3, 4, 5, 7, 8, 9, 10} whose elements are distinct and within the range of 1 to 10. The missing number is 6.


# a=[1, 2, 3, 4, 5, 7, 8, 9, 10]
# l=[]
# for i in range (a[0],a[-1]):
#     l.append(i)
    

            


# 3)Merge two Sorted Array
# Input:
# 	a = [1,2,3],  b = [2,5,6]
# output:  [1,2,2,3,5,6]

# a = [1,2,3] 
# b = [2,5,6]
# a.extend(b)
# a.sort()
# print(a)


# Input:
# 	a = None,  b = [2,5,6]
# output:  [2,5,6]

# Input:
# 	a = [1,2,3],  b = None
# output:  [1,2,3]

# 4)Check Two strings are anagram
# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

# s = "anagram"
# t = "nagaram"

# c1=0
# c2=0
# for i in s :
#     if i in t:
#         c1+=1
#     else:
#         b
        

        
# if l1 in l2:
#     print("True")
# else:
#     print("False")


# 5)Reverse Vowels of a String
# Input: s = "hello"
# Output: "holle"






# 6)Find  3rd largest number in an integer array
# Input: nums = [3,2,1]
# Output: 1

# Input: nums = [2,2,3,1]
# Output: 1

# Input: nums = [1,2]
# Output: 2

# Input: nums = [1]
# Output: 1

# nums = [2,2,3,1]
# unique=set(nums)
# ul=list(unique)
# ul.sort(reverse=True)
# print(ul[2],"Is the Third Highest")


# 7)Given an integer array nums, find three numbers whose product is maximum and return the maximum product

# Input: nums = [1,2,3]
# Output: 6

# Input: nums = [1,2,3,4]
# Output: 24

# Input: nums = [-1,-2,-3]
# Output: -6

# 8)Find all duplicates numbers in a list


# a=[1,1,1,2,2,3,3,3,4,5]
# unique=[]
# duplicate=[]

# for i in a :    
#     if i not in unique:
#         unique.append(i)
#     else:
#         duplicate.append(i)
        
        
# print(duplicate)
        



# 9)Transpose Matrix

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output:
    
    
    
# 10) Write a Python program to reverse each word in a string?
# Case 1:-
# 	Input:- this is javatpoint
# 	Output:- siht si tnioptavaj
# Case 2:-
# 	Input:- this
# 	Output:- siht
# Case 2:-
# 	Input:- “”
# 	Output:- “”


# s=None
# x=s.split()

# for i in x:
#     print(i[::-1],end=" ")