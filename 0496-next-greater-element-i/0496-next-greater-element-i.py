class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = []
        for i in range(len(nums1)):
            nextGreater.append(-1)
            
            for j in range(nums2.index(nums1[i]) + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    nextGreater.pop()
                    nextGreater.append(nums2[j])
                    break
            
                    
        
        return nextGreater