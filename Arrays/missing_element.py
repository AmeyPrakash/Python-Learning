from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        minel = min(nums)
        maxel = max(nums)
        ans=[]
        for i in range(minel, maxel+1):
            if i not in nums:
                ans.append(i)
        return ans