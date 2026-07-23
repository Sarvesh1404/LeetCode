class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans= []
        for i in arr2:
            for j in arr1:
                if i == j:
                    ans.append(i)

        for j in sorted(arr1):
            if j not in arr2:
                ans.append(j)
        return ans