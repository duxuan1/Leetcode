import collections
from typing import List, Set


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict: return 0
        wordLen = len(beginWord)

        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(wordLen):
                adj[word[:i] + '*' + word[i + 1:]].append(word)

        dq = collections.deque([(beginWord, 1)])
        while dq:
            word, level = dq.popleft()
            for i in range(wordLen):
                dummyWord = word[:i] + '*' + word[i + 1:]
                for newWord in adj[dummyWord]:
                    if newWord == endWord:
                        return level + 1
                    if newWord in wordDict:
                        wordDict.remove(newWord)
                        dq.append((newWord, level + 1))
        return 0
