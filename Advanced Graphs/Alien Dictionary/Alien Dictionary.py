
"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

1.You may assume all letters are in lowercase.
2.The dictionary is invalid, if string a is prefix of string b and b is appear before a.
3.If the order is invalid, return an empty string.
4.There may be multiple valid order of letters, return the smallest in normal lexicographical order.
5.The letters in one string are of the same rank by default and are sorted in Human dictionary order.

"""
def alien_order(words):
        adj = {char : set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True
            
            visited[char] = False
            res.append(char)
        
        for char in sorted(adj.keys(), reverse= True):
            if dfs(char):
                return ""
        

        print(res)
        res.reverse()

        return "".join(res)


print(alien_order(["wrt","wrf","er","ett","rftt"]))
print(alien_order(["abc","abdc"]))