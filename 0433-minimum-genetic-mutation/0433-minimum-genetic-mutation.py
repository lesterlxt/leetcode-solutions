class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        if startGene == endGene:
            return 0

        # BFS
        genes = ['A', 'C', 'G', 'T']
        visited = {startGene}
        queue = collections.deque([(startGene, 0)]) # (current_gene, steps_so_far)
        while queue:
            current, steps = queue.popleft()
            for i in range(len(current)):
                for ch in genes:
                    if ch == current[i]:
                        continue
                    
                    next_gene = current[:i] + ch + current[i+1:]
                    if next_gene in bank_set and next_gene not in visited:
                        if next_gene == endGene:
                            return steps + 1
                        visited.add(next_gene)
                        queue.append((next_gene, steps + 1))
        
        return -1



        
