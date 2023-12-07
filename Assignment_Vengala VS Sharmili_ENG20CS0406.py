#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given a string s consisting of words and spaces, return the length of the last word in the string.
def length_of_last_word(s):
    words = s.split()

    if len(words) == 0:
        return 0

    return len(words[-1])

input_string = "Hello World"
result = length_of_last_word(input_string)
print(result)


# In[4]:


#Given an integer numRows, return the first numRows of Pascal's triangle.
def generate_pascals_triangle(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

numRows = int(input("Enter the number of rows for Pascal's triangle: "))
result = generate_pascals_triangle(numRows)
print(result)


# In[12]:


#Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
class TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root or root.val == p.val or root.val == q.val:
        return root

    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    else:
        return root

def build_bst():
    values = input("Enter space-separated values for the BST (use 'null' for null values): ").split()
    root = None
    for val in values:
        if val.lower() == 'null':
            continue
        root = insert(root, int(val))
    return root

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

root = build_bst()

p_val = int(input("Enter the value of the first node: "))
q_val = int(input("Enter the value of the second node: "))

p = TreeNode(p_val)
q = TreeNode(q_val)

lca_node = lowest_common_ancestor(root, p, q)
if lca_node:
    print("Lowest Common Ancestor:", lca_node.val)
else:
    print("No common ancestor found.")


# In[9]:


#Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
def majority_elements(nums):
    if not nums:
        return []

    element1, count1 = None, 0
    element2, count2 = None, 0

    for num in nums:
        if element1 == num:
            count1 += 1
        elif element2 == num:
            count2 += 1
        elif count1 == 0:
            element1, count1 = num, 1
        elif count2 == 0:
            element2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for num in nums:
        if element1 == num:
            count1 += 1
        elif element2 == num:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(element1)
    if count2 > len(nums) // 3:
        result.append(element2)

    return result

nums = list(map(int, input("Enter space-separated integers: ").split()))
result = majority_elements(nums)
print("Elements appearing more than ⌊ n/3 ⌋ times:", result)


# In[14]:


#You are given a string s. You can convert s to a palindrome by adding characters in front of it.
user_input = input("Enter a string: ")

def short_palindrome(s):
    if s == "":
        return ""

    rev_s = s[::-1]
    for i in range(len(s), 0, -1):
        if s[:i] == rev_s[-i:]:
            
            break

    return rev_s[:-i] + s

result = short_palindrome(user_input)
print("Shortest palindrome:", result)


# In[1]:


#Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n
n = int(input("Enter an integer n: "))

def count_digitone(n):
    count = 0
    factor = 1
    i = 1

    while i <= n:
        divisor = i * 10
        count += (n // divisor) * i + min(max(n % divisor - i + 1, 0), i)
        i *= 10

    return count
    
result = count_digitone(n)
print(f"The total number of digit 1 in numbers up to {n} is: {result}")


# In[ ]:




