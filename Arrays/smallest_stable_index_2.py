class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minindex = [0] * n
        minel = float('inf')
        maxel = float('-inf')
        for i in range(n-1, -1,-1):
            minel = min(minel, nums[i])
            minindex[i] = minel

        for i in range(n):
            maxel = max(maxel, nums[i])
            minel = minindex[i]
            if(maxel - minel <= k):
                return i

        return -1