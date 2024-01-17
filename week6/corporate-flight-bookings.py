class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * n

        for f, l, s in bookings:
            flights[f - 1] += s
            if l != n:
                flights[l] -= s
        
        return list(accumulate(flights))