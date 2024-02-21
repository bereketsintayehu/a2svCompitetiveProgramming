class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums1)
        index = {num : i for i, num in enumerate(nums1)}

        for i in range(len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                ans[index[stack.pop()]] = nums2[i]
                
            if nums2[i] in index:
                stack.append(nums2[i])
            
        return ans