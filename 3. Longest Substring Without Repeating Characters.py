class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        d = {}
        i = 0
        for j in range(len(s)):
            if s[j] in d:
                i = max(d[s[j]], i)

            count = max(count, j - i + 1)
            d[s[j]] = j + 1
        return count


    def sliding_window(self, s: str) -> int:
        count, i, j = 0, 0, 0
        strlen = len(s)
        strset = set()
        while i < strlen and j < strlen:
            if s[j] not in strset:
                strset.add(s[j])
                count = max(count, j - i + 1)
                j += 1
            else:
                strset.remove(s[i])
                i += 1
        return count


if __name__ == "__main__":
    s = Solution()
    ans = s.lengthOfLongestSubstring("abcabcbb")
    res = s.sliding_window("abcabcbb")
