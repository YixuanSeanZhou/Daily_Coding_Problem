'''
Problem:

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all 
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

'''
Reflection:

- Question to ask: what should happen when empty input or only have one input

When accessing a list in reverse order, 
need to do len(list) - i - i because the indexing problem.

Becuase only excluding one entry, 
it is linear to find all its prefix and suffix.

'''

def devision(given):
    ret = []
    product = 1
    for i in range(len(given)):
        product *= given[i]
    for i in range(len(given)):
        ret.append(product // given[i])
    return ret

def fixes(given):
    prefix = []
    for num in given:
        if prefix:
            prefix.append(prefix[-1] * num)
        else:
            prefix.append(num)
    
    suffix = []
    for num in reversed(given):
        if suffix:
            suffix.append(suffix[-1] * num)
        else:
            suffix.append(num)
    
    ret = []
    for i in range(len(given)):
        if i == 0:
            ret.append(suffix[len(given)-i-2])
        elif i == len(given) - 1:
            ret.append(prefix[i-1])
        else:
            ret.append(prefix[i-1] * suffix[len(given)-i-2])
    
    return ret

if __name__ == '__main__':

    test_1 = [1, 2, 3, 4, 5]
    print(fixes(test_1))
    test_2 = [3, 2, 1]
    print(fixes(test_2))
    test_3 = [1]
    print(fixes(test_3))

