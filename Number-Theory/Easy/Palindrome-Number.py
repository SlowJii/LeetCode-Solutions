class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        elif (x >= 0 and x < 10):
            return True
        else:
            return str(x) == str(x)[::-1]
