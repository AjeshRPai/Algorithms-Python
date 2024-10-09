from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create adjacency list using defaultdict to handle destinations
        # defaultdict automatically creates empty list for new keys
        flights = defaultdict(list)

        # Build the graph
        for src, dst in tickets:
            flights[src].append(dst)

        # Sort destinations to ensure lexical smallest comes first
        for src in flights:
            flights[src].sort()

        route = []

        def visit(airport):
            # Visit all destinations from current airport
            while flights[airport]:
                # Get next destination (always takes smallest lexically)
                next_dest = flights[airport].pop(0)
                visit(next_dest)
            # Add current airport to route after visiting all its destinations
            route.append(airport)

        # Start DFS from JFK
        visit("JFK")

        # Route is built in reverse order, so reverse it
        return route[::-1]


# Driver code with multiple test scenarios
def test_itinerary():
    sol = Solution()

    # Test Case 1: Simple linear path
    test1 = [["JFK", "SFO"], ["SFO", "ATL"]]
    print("Test 1:", sol.findItinerary(test1))  # Expected: ["JFK","SFO","ATL"]

    # Test Case 2: Multiple possible paths, should take lexically smallest
    test2 = [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "SFO"]]
    print("Test 2:", sol.findItinerary(test2))  # Expected: ["JFK","ATL","JFK","SFO"]

    # Test Case 3: Complex case with multiple options
    test3 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print("Test 3:", sol.findItinerary(test3))  # Expected: ["JFK","ATL","JFK","SFO","ATL","SFO"]


if __name__ == "__main__":
    test_itinerary()