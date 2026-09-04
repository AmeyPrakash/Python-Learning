class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minindex = [0] * n
        maxel = float('-inf')
        minel = float('inf')
        for i in range(n-1, -1, -1): #separately calculate min index in list
            minel = min(minel, nums[i])
            minindex[i] = minel

        for i in range(n):       #max on the go and calculating stability
            maxel = max(maxel, nums[i])
            minel = minindex[i]
            if(maxel - minel <= k):
                return i

        return -1