class Solution:
    def isPalindrome(self, s: str) -> bool:
        A=[]
        for i in s:
            if i.isalnum():
                A.append(i.lower())
        return A==A[::-1]
