'''
# 8

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_tree(node):
    def post_order_traversal(node) -> (bool, int, int):
        if node.left:
            uni_left, left_val, count_left = post_order_traversal(node.left)
        else:
            uni_left = True
            count_left = 0
            left_val = node.val
        
        if node.right:
            uni_right, right_val, count_right = post_order_traversal(node.right)
        else:
            uni_right = True
            count_right = 0
            right_val = node.val
        
        total = count_left + count_right

        if uni_left and uni_right and (left_val == right_val == node.val):
            return True, node.val, total + 1
        
        return False, node.val, total
    
    _, _, ret = post_order_traversal(node)
    return ret

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

def main(tree_string):
    node = deserialize('0 1 # # 0 1 1 # # 1 # # 0 # #')
    print(count_unival_tree(node))
    node = deserialize('a a # # a a # # a # A # #')
    print(count_unival_tree(node))
    node = deserialize('a c # # b b # # b # b # #')
    print(count_unival_tree(node))

if __name__ == '__main__':
    main('')