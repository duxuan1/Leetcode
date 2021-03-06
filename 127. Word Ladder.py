class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # edge check
        if endWord not in wordList:
            return 0
        str_len = len(beginWord)
        #
        all_comb = {}
        for word in wordList:
            for i in range(str_len):
                temp = word[:i] + "*" + word[i + 1:]
                if temp not in all_comb:
                    all_comb[temp] = []
                all_comb[temp].append(word)
        visited = set()
        queue = [(beginWord, 1)]
        while queue:
            curr_word, count = queue.pop(0)
            for i in range(str_len):
                temp = curr_word[:i] + "*" + curr_word[i + 1:]
                if temp in all_comb:
                    for word in all_comb[temp]:
                        if word == endWord:
                            return count + 1
                        if word not in visited:
                            visited.add(word)
                            queue.append((word, count + 1))
        return 0


if __name__ == "__main__":
    s = Solution()
    ans = s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
