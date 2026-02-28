class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * numCourses

        order = []
        q = deque()
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a
            indeg[a] += 1
        
        for course in range(numCourses):
            if indeg[course] == 0:
                q.append(course)
        
        while q:
            cur = q.popleft()
            order.append(cur)

            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        
        return order if len(order) == numCourses else []

