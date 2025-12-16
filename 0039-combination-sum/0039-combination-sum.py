class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int, remaining: int):
            if remaining == 0:
                res.append(path.copy())
                return 
            
            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remaining:
                    continue
                
                path.append(x)
                dfs(i, remaining - x)
                path.pop()

        dfs(0, target)
        return res
