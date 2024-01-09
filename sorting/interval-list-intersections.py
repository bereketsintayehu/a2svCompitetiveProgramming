class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l = r = 0
        n1, n2 = len(firstList), len(secondList)
        ans = []

        while l < n1 and r < n2:
            st1, end1 = firstList[l]
            st2, end2 = secondList[r]
            
            if st1 <= st2 <= end1 or st2 <= st1 <= end2:
                ans.append([max(st1, st2), min(end1, end2)])
            
            if end1 < end2:
                l += 1
            else:
                r += 1
 
        return ans