#SOLUTION 1: TYPE CONVERSION
#Lists are not a convenient way to deal with integers.
# Therefore, we convert the list of integers into a form we can directly manipulate.
# We convert the list into a string and use the string join operation to convert the result into a single string.
# We cannot use normal addition on a string, so we convert the string into an integer then add one.
# Then we reverse the process. 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        str_digits = ''.join(str(i) for i in digits)
        int_digits = int(str_digits) + 1
        str_digits = str(int_digits)
        for i in str_digits:
            result.append(int(i))
        return result

#SOLUTION 2: DIRECTLY CONVERT THE LIST INTO AN INTEGER
#We're given a list of digits, and the idea here is to convert that list to an integer, num. 
# So each digit is multiplied by the proper place value and added to num. 
# For example, if digits = [3, 8, 2, 5] then on the first iteration 3 is multiplied by 10 to the power of 4-1-0 = 3, so this results in 3000, which is added to num. 
# Then 8 is multiplied by 10^2 and added to num, and so on. The last step is to add 1 to num, convert it to a list and return that list.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
        
#SOLUTION 3: REVERSE LIST ADDITION
#Loop through the list in reverse order
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] +=1
                return digits
        return [1] + digits 


