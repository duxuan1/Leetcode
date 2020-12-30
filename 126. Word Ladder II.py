from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # edge check
        if endWord not in wordList:
            return []
        str_len = len(beginWord)
        # build up
        all_comb = {}
        for word in wordList:
            for i in range(str_len):
                temp = word[:i] + "*" + word[i + 1:]
                if temp not in all_comb:
                    all_comb[temp] = []
                all_comb[temp].append(word)
        res = []
        visited = set()
        queue = [(beginWord, [beginWord])]
        while queue:
            curr_word, ladder = queue.pop(0)
            for i in range(str_len):
                temp = curr_word[:i] + "*" + curr_word[i + 1:]
                if temp in all_comb:
                    for word in all_comb[temp]:
                        if word == endWord:
                            ladder.append(word)
                            res.append(ladder)
                            break
                        if word not in visited:
                            visited.add(word)
                            ladder.append(word)
                            queue.append((word, ladder))
        return res


if __name__ == "__main__":
    s = Solution()
    ans = s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
