class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph: dict[str, dict[str, float]] = defaultdict(dict)

        for (a, b), val in zip (equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def bfs(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            q = deque([(src, 1.0)])
            visited = {src}

            while q:
                node, val = q.popleft()
                if node == dst:
                    return val
                
                for nei, weight in graph[node].items():
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, val * weight))
            
            return -1.0
        
        res = []
        for x, y in queries:
            res.append(bfs(x, y))
        return res





