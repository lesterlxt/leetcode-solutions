class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i in range(n):
            for j in range(n - i - 1):
                if citations[j] < citations[j + 1]:
                    citations[j], citations[j + 1] = citations[j + 1], citations[j]

        
        for idx, cites in enumerate(citations):
            if cites < idx + 1:
                return idx

        return len(citations)