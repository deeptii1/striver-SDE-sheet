class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        rev=num[::-1]
        if rev!=num:
            return False
        return True