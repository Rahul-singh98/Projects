from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattdict = dict()
        slist = s.split(' ')
        sdict = dict()

        for a, b in zip(pattern, slist):
            if pattdict.get(a) and pattdict.get(a) != b and sdict.get(a) != a:
                return False

            pattdict[a] = b
            sdict[b] = a
        return True

sol = Solution()

print(sol.wordPattern("abba", "dog cat cat dog"))
print(sol.wordPattern("abba", "dog cat cat fish"))
print(sol.wordPattern("aaaa", "dog cat cat dog"))
print(sol.wordPattern("abba", "cat cat cat cat"))