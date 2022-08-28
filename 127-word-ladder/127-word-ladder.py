class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        hmap = collections.defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                hmap[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        result = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neigh in hmap[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
            result += 1
        return 0
        
        
        
        
                
        