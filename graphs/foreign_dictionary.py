from collections import defaultdict, deque


class Solution:
    def foreignDictionary(self, words):
        # Step 1: Initialize graph and indegree count
        graph = defaultdict(set)
        indegree = defaultdict(int)

        # Create a node for every character in the input words
        for word in words:
            for char in word:
                indegree[char] = 0

        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # Check for an invalid order (e.g., "apple" -> "app")
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            # Compare characters of the two words
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    # If c1 comes before c2, add the edge c1 -> c2
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        # Step 3: Perform topological sort using BFS
        queue = deque([char for char in indegree if indegree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)
            # Reduce the indegree of neighboring characters
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if we have a valid topological order
        if len(order) != len(indegree):
            return ""

        return "".join(order)
