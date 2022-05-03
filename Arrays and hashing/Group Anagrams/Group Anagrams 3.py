def groupAnagrams(slist):

    dict ={}
    for s in slist:
        x=''.join(sorted(s))
        if x not in dict:
            dict[x] = [s]
        else:
            dict[x].append(s)
                
    return dict.values() 

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
