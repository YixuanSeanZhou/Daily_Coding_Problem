'''
This problem was asked by Twitter.

Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, 
given the query string de and the set of strings [dog, deer, deal], 
return [deer, deal].
'''

from typing import List


class Node:
    def __init__(self, val):
        self.children = []
        for i in range(26):
            self.children.append([])
        self.val = val
        self.leaf = False
    
    def insert(self, word):
        
        if len(word) == 0:
            self.leaf = True
            return

        pre = word[0]
        rest = word[1:]
        pre_idx = ord(pre) - ord('a')

        if not self.children[pre_idx]:
            self.children[pre_idx] = Node(pre)
        
        self.children[pre_idx].insert(rest)
        
    def find(self, word):
        
        if len(word) == 0:
            return self
        
        pre = word[0]
        rest = word[1:]
        pre_idx = ord(pre) - ord('a')

        if not self.children[pre_idx]:
            return None
        else:
            return self.children[pre_idx].find(rest)
        
    def dfs(self):
        ret = []
        for i in range(25):
            if self.children[i]:
                ret += self.children[i].dfs()
        for i in range(len(ret)):
            ret[i] = self.val + ret[i]
        if self.leaf:
            ret.append(self.val)
        return ret

class MultTrie:
    def __init__(self):
        self.root = Node('')
    
    def insert(self, word):
        word = word.lower()
        self.root.insert(word)
    
    def find(self, word):
        word = word.lower()
        return self.root.find(word)
    
    def dfs(self, node):
        return node.dfs()


def autocomplete(trie, prefix: str) -> List[str]:
    words = trie.dfs(trie.find(prefix))
    rets = [prefix[:-1] + r for r in words]
    return rets


def main(strings: List[str], prefix_lists: List[str]):
    trie = MultTrie()
    for s in strings:
        trie.insert(s)
    
    for p in prefix_lists:
        print('Prefix: ' + p)
        r = autocomplete(trie, p)
        print(r)

if __name__ == '__main__':
    main(['dog', 'deer', 'deal'], ['d', 'de'])    
