class Solution:
    def singleNumber(self, n: List[int]) -> int:
        r=0
        for i in n:
            r^=i
        return r