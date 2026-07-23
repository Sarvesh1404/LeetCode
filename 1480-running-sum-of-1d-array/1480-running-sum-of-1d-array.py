class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        tot=0
        for i in nums:
            tot=tot+i
            result.append(tot)
        return result