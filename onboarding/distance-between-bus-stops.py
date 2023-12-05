class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        forw = backw = 0
        curr = start

        while curr != destination:
            forw += distance[curr]
            curr = (curr + 1) % n
        
        curr = start
        while curr != destination:
            curr = (curr-1) % n
            backw += distance[curr]

        curr = (start - 1) %n
        return min(forw, backw)