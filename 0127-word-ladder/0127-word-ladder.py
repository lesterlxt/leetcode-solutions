class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        
        q = collections.deque([(beginWord, 1)]) #word, distance
        visited = {beginWord}

        while q:
            word, dist = q.popleft()

            if word == endWord:
                return dist
            
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for next_word in patterns.get(pattern, []):
                    if next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, dist + 1))
                
                patterns[pattern] = []

        return 0
