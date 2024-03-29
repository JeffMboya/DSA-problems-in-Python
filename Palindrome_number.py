#Solution 1: CONVERT INTERGER TO TRING AND REVERSE
#This is the easiest way to check if integer is palindrome.
# Convert the number to string and compare it with the reversed string.
def isPalindrome(self, x: int) -> bool:
	if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
		return False
	
	return str(x) == str(x)[::-1]

#SOLUTION 2: REVERSE HALF OF INTEGER
dclass Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        xRev = 0
        while x > xRev:
            xRev = xRev * 10 + x % 10
            x = x // 10
        return True if (x == xRev or x == xRev // 10) else False