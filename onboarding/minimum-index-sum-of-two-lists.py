class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = defaultdict(list)

        for i, s in enumerate(list1):
            if s in list2:
                d[i+list2.index(s)].append(s)
        
        return d[min(d)]
        
        