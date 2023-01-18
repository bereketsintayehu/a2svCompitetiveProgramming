from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        nextGreater = [-1] * len(nums1)
        for i in range(len(nums2)):
            
            while len(stack) > 0 and stack[-1] < nums2[i]:
                nextGreater[nums1.index(stack.pop())] = nums2[i]
                
            if nums2[i] in nums1:
                stack.append(nums2[i])
            
        return nextGreater