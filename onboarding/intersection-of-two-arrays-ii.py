class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        return [num for num, count in c1.items() for _ in range(min(count, c2[num])) ]