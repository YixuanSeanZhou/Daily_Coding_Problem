'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Slow and bad:

from collections import deque


    
def deserialize(s):
    node_queue = deque()
    node_val = ''
    for i in range(len(s)):
        c = s[i]
        if c == '(':
            node = Node(node_val)
            node_queue.append(node)
            node_val = ''
        elif c == ')':
            # Leaf
            if s[i-1] == '(' or s[i-1] == ',':
                continue
            else:
                right_child = node_queue.pop()
                parent = node_queue.pop()
                parent.right = right_child
                node_queue.append(parent)
        elif c == ',':
            left_child = node_queue.pop()
            parent = node_queue.pop()
            parent.left = left_child
            node_queue.append(parent)

        else:
            node_val += c
    
    while node_queue:
        ret = node_queue.pop()
    return ret    

def serialize(root):
    ret = ''
    ret = ret + root.val + '('
    if root.left:
        ret += serialize(root.left)
        ret += ','
    if root.right:
        ret += serialize(root.right)
    ret += ')'
    return ret
'''


'''
Better and cheaper
'''

def serialize(root: Node) -> str:
    ret = []
    def dfs(node):
        if not node:
            ret.append('#')
            return
        ret.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ' '.join(ret)

def deserialize(data):
    def dfs():
        val = next(vals)

        if val == '#':
            return None
        else:
            node = Node(val)
            node.left = dfs()
            node.right = dfs()
        return node
    vals = iter(data.split())
    return dfs()

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'