class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        res = []

        for start, end in intervals:
            if end < newStart:
                res.append([start, end])
            elif start > newEnd:
                res.append([newStart, newEnd])
                newStart, newEnd = start, end
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        
        res.append([newStart, newEnd])
        return res


            