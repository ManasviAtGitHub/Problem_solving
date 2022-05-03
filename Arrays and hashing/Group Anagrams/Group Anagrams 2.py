

from collections import defaultdict


def groupAnagrams(slist):

    ans = defaultdict(list)
    for s in slist:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
