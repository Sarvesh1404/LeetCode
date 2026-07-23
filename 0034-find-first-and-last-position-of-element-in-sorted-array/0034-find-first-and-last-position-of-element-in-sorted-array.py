class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        n = len(nums)
        if target not in nums:
            return [-1,-1]
        for i,j in enumerate(nums):
            if j == target:
                res.append(i)
        if len(res) == 1:
            res.append(res[0])
            return res
        elif len(res) > 2: 
            m = min(res)
            n = max(res)
            res.clear()
            res.append(m)
            res.append(n)
            return res
        else:
            return res


                    

          
        