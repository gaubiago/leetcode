class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulator = 0
        answer = list()
        for i in range(len(nums)):
            accumulator += nums[i]
            answer.append(accumulator)
        return answer