class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)   # graph[pre] = [course1, course2...]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque()
        for course in range(numCourses):
            if indeg[course] == 0:
                q.append(course)

        taken = 0
        while q:
            cur = q.popleft()
            taken += 1

            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        return taken == numCourses 

