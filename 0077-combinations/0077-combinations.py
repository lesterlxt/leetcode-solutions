class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start):
            if len(path) == k:
                res.append(path.copy())
                return 
            
            # n = 3, k = 2
            # [1 2 3]; choose 2
            # start = 1
            # path[1]
            # dfs(i+1)=dfs(1+1)=(2)
            # len(path) = 1
            # path[1, 2]
            # dfs(2+1)=(3) i ==3
            # len(path) = 2 == k
            # res.append([1, 2])
            # return to start == 2
            # path.pop -> path = [1]
            # len(path) = 1 < k
            # i == 3
            # path.append(3)
            # path = [1,3] res.append
            # 


            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()
        
        dfs(1)
        return res