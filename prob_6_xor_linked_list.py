'''
Daily Coding Problem: Problem #6 [Hard]

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, 
it holds a field named both, 
which is an XOR of the next node and the previous node. 
Implement an XOR linked list; 
it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.
'''

import ctypes

def get_pointer(obj):
    return id(obj)

def dereference_pointer(ptr):
    return ctypes.cast(ptr, ctypes.py_object).value

class Node:
    def __init__(self, element):
        self.data = element
        self.both = 0

class XorList:
    def __init__(self):
        self.head = self.tail = None
        self.__nodes__ = [] # used to prevent mem leak
    
    def add(self, element): 
        # Check for empty list
        if not self.head:
            self.head = Node(element)
            self.tail = self.head
            self.__nodes__.append(self.head)
            return
        
        node = Node(element)
        node.both = get_pointer(self.tail)
        self.tail.both ^= get_pointer(node)
        self.tail = node
        self.__nodes__.append(self.tail)
    
    def get(self, idx):
        # Check for empty list
        if not self.head:
            return None
        
        count = 0
        pre = 0
        curr = self.head
        while count < idx:
            
            next_ptr = curr.both ^ pre
            
            if next_ptr == 0:
                return None
            
            pre = get_pointer(curr)
            curr = dereference_pointer(next_ptr)
            count += 1

        return curr.data



