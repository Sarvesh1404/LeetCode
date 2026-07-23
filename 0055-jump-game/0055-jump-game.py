class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for n in nums:
            if jump < 0:
                return False
            jump = max(jump, n)
            jump -= 1
        return True