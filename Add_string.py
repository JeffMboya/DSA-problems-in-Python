#What we need to do in this problem is to perform usual schoolbook addition. 
# We need to start to add numbers from the last elements and take care of carry and cases when one number has more digits that another. 
# Imagine that we want to add two numbers: 986 and 47. Then we have the followint steps:
# Add 6 and 7, so we have digit 3 and carry equal to 1.
# Add 8 and 4 and 1, so we have 3 and carry equal to 1.
# Add 9 from first number, and we do not have anything from second, so we choose 0 from second. Also we have curry equal to 1, finally we have digit 0 and carry equal to 1.
# We still have carry, but no digits left, so we evaluate 0 + 0 + 1 = 1. 
# And now we can stop, we do not have digits and we do not have carry.
# Final number we constructed is 1033.

#Complexity
#Time complexity is O(m + n), where m and n are lengths of our linked lists
# space complexity is O(max(m, n)) if we count answer as memory or O(1) if we do not.

#SOLUTION 1: USE UNICODE
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            result  = 0
            for n in num:
                result = result * 10 + ord(n) - ord('0')
            return result
        return str(str2int(num1) + str2int(num2))
    
#SOLUTION 2: USE DICTIONARY
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        def str2int(num):
            numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            output = 0
            for d in num:
                output = output * 10 + numDict[d]
            return output
        
        return str(str2int(num1) + str2int(num2)) 
#SOLUTION 3:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        i1, i2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while i1 >= 0 or i2 >= 0 or carry > 0:
            if i1 >= 0:
                carry += ord(num1[i1]) - ord('0')
                i1 -= 1
            if i2 >= 0:
                carry += ord(num2[i2]) - ord('0')
                i2 -= 1
            ans.append(chr(carry % 10 + ord('0')))
            carry //= 10
        return "".join(ans)[::-1]
# NOTE
#We can add two numbers represented as strings by adding digits from the given numbers in each place. 
# The sum of two digits must be between 0 and 18. 
# The ones place is added to the result while the tens place is carried and summed with the next pair of digits. 
# When summing two numbers, the carried digit will always be zero or one. 
# This process can be repeated for each digit.