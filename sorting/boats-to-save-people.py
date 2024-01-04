class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        total = 0
        l, r = 0, len(people) - 1

        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            total += 1

        if l == r:
            total += 1
            
        return total