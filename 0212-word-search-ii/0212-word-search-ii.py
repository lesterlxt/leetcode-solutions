class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        m, n = len(board), len(board[0])
        res: List[str] = []

        def dfs(i: int, j:int, node: TrieNode) -> None:
            ch = board[i][j]
            if ch not in node.children:
                return

            next_node = node.children[ch]
            if next_node.word is not None:
                res.append(next_node.word)
                next_node.word = None
            
            board[i][j] = "#"
            if i > 0 and board[i-1][j] != "#":
                dfs(i-1, j, next_node)
            if i < m - 1 and board[i+1][j] != "#":
                dfs(i+1, j, next_node)
            if j > 0 and board[i][j-1] != "#":
                dfs(i, j-1, next_node)
            if j < n - 1 and board[i][j+1] != "#":
                dfs(i, j+1, next_node)
            
            board[i][j] = ch
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res
