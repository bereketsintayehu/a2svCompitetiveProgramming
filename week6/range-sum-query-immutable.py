class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.psum = [0] * (n + 1)

        for i in range(n):
            self.psum[i + 1] = self.psum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right + 1] - self.psum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)