from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            sub = ''.join(sorted(i))
            if sub in dic:
                dic[sub].append(i)
            else:
                dic[sub] = [i]
        return list(dic.values())


if __name__ == "__main__":
    Input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output =[
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
            ]
    s = Solution()
    res = s.groupAnagrams(Input)
    print(res)
