"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class TrieNode:


  def __init__(self):
    ##a hash map for storing all childrens
    self.children = {}

    ##for marking the word end,  as true
    self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()



    def addWord(self, word: str) -> None:
        cur = self.root
        ## add all the chararcters and mark the end of the word character as true
        for c in word:
          if c not in cur.children:
            cur.children[c] = TrieNode()
          cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        ## handles . cases too

        def dfs(j, root):
          cur = root
          ## we iterate over each letter
          for i in range(j, len(word)):
            c = word[i]
            ##if letter is . then we don't have to match just move next character
            ##hence recursive definition
            if c == ".":
              
              ## moving through each individual character chain, until we find 
              ## our mactching word
              for child in cur.children.values():

                ##this ensures we immediately end the statemnt if any mismatch
                ## occurs in traversing the current chain of characters
                ## we switch to next child if any
                if dfs(i+1, child):
                  return True
              
              return False
            
            else:
            
            ## if not in children, we know there is a mismatch at current level
              if c not in cur.children:
                return False
            ##otherwise we just move to the next character in the chain
              cur = cur.children[c]
              
        ##if our end character is endword only then it returns true, else we move to the next child
          return cur.word
        
        
        return dfs(0, self.root)
