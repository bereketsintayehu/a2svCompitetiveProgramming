class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        
        for n in nums1:
            if n not in nums2:
                answer[0].append(n)
                
        answer[0] = list(set(answer[0]))
        
        for n in nums2:
            if n not in nums1:
                answer[1].append(n)
                
        answer[1] = list(set(answer[1]))
        
        return answer