class Solution:
    def isPalindrome(self, x: int) -> bool:
        output = str(x)
        return output == output[::-1]