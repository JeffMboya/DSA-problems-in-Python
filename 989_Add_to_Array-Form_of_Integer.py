#SOLUTION 1: TYPE CONVERSION
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res= []
        str_num =''.join(str(i) for i in num)
        int_num = int(str_num) + k
        str_num = str(int_num)
        for i in str_num:
            res.append (int(i))
        return res
    

    #SOLUTION 2:
    class Solution:
     def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans, i = [], len(A) - 1
        while K > 0 or i >= 0:
            K, rmd = divmod(K + (A[i] if i >= 0 else 0), 10)
            ans.append(rmd)
            i -= 1
        return reversed(ans)