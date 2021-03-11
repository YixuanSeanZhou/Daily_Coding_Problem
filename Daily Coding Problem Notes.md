# Daily Coding Problem Notes



## Problem 1

### Problem:

Two Sum

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

### Notes

READ THE PROBLEM (two sum)

len(array) - 1 = array last index



## Problem 2

### Problem:

Given an array of integers, return a new array such that each element 

at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 

the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 

the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

### Notes:

Question to ask: what should happen when empty input or only have one input

When accessing a list in reverse order, need to do len(list) - i - i because the indexing problem.

Becuase only excluding one entry, it is linear to find all its prefix and suffix.



## Problem 3

### LeetCode # 297. Serialize and Deserialize Binary Tree

### Problem

This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following `Node` class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

### Notes:

Question to ask: What character is allowed to be used (reserved)

Approach: DFS + Reserve space for None

Note: Think about who is in charged of the checks during recursive calls!

#### Iterator  

An iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable *containers* which you can get an iterator from.

All these objects have a `iter()` method which is used to get an iterator:

Use `raise StopIteration` to stop the iterator in the `for-in` loop.



## Problem 4

### Leetcode # 41. First Missing Positive

### Problem: 

Given an unsorted integer array `nums`, find the smallest missing positive integer.

**Example 1:**

```
Input: nums = [1,2,0]
Output: 3
```

**Example 2:**

```
Input: nums = [3,4,-1,1]
Output: 2
```

**Example 3:**

```
Input: nums = [7,8,9,11,12]
Output: 1
```

**Constraints:**

* `0 <= nums.length <= 300`
* `-231 <= nums[i] <= 231 - 1`

**Follow up:** Could you implement an algorithm that runs in `O(n)` time and uses constant extra space?

### Notes:

Think about what is the range of possible answers: Only [1,...,n+1] where n = length of the array. 

Positive numbers VS 0-starting index. How to use hash map to count occurrences of each number. 

​	Positive number starts from one, so it would be better to iterate from 1 instead of 0.

Think about how to handle special case. 



## Problem 5

### Problem

This problem was asked by Jane Street.

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement `car` and `cdr`.

### Notes:

This problem is about functional programming. 

We pack the result in a pair, which would take in a function to extract the result. 

```python
def car(pair):
  def left(a, b):
    return a
	return pair(left)

car(cons(1, 2))
```

This would print 1.

The way to interoperate is as following:

Cons return the pair, which currently return the result of an annonymous function f applied to the numbers a, b. 

Thus, to unpack this object, we need to create a function as pass this in to pair. 

```python
def f(a):
    def g(b):
        return a+b
    return g
>>> f(1)
<function f.<locals>.g at 0x10d4cd280>
>>> f(1)(2)
3
```



## Problem 6

### Problem XOR Linked List

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding `next` and `prev` fields, it holds a field named `both`, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an `add(element)` which adds the element to the end, and a `get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to `get_pointer` and `dereference_pointer` functions that converts between nodes and memory addresses.

### Note:

Using XOR to store the pre xor next address

In python, the address can be found by `id(obj)`, and with `ctypes` being imported, we can dereference the address by the following. 

```python
import ctypes

ctypes.cast(address, ctypes.py_object).value
```

However, python has its own garbage collector, thus to maintain the object not being collected, we need to store them into a list or somewhere that we can access. 



## Problem 7

### Leetcode # 91. Decode Ways

### Problem

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 

count the number of ways it can be decoded.

For example, the message '111' would give 3, 

since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

### Notes:

Need to consider all the possible base case (*EMPTY STRING* and length 1 case).

Need to keep in mind when the string is not invalid (it can be invalid in the middle of recursion)

This is easy to come up with $O(n)$ space $O(n)$ time dp, but a smatter way only use $O(1)$ space, which his a loop based solution so even better.  



## Problem 8

### Problem 

\# 8

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0

  / \

 1   0

​    / \

   1   0

  / \

 1   1

### Related Problem

### Leetcode #965. Univalued Binary Tree

A binary tree is *univalued* if every node in the tree has the same value.

Return `true` if and only if the given tree is univalued.





## Problem 9 Hard

### Problem

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2, 6`, and `5`.` [5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

Follow-up: Can you do this in O(N) time and constant space?

