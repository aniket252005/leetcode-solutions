class Solution(object):
    def runningSum(self, nums):
        runningSum = []

        for i in range(len(nums)):
            runningSum.append(sum(nums[0:i+1]))
        return runningSum
        