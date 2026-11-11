class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0

        while nums != sorted(nums):
            s = nums[0] + nums[1]
            pos = 0

            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < s:
                    s = nums[i] + nums[i+1]
                    pos = i

            nums[pos] += nums[pos+1]
            nums.pop(pos+1)
            count += 1

        return count