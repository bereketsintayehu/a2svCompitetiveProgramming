class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        psum = [0]
        psum.extend(list(accumulate(nums)))
        psum.append(0)

        for i in range(len(nums) ):
            if psum[i] == (psum[-2] - psum[i + 1]):
                return i

        return -1