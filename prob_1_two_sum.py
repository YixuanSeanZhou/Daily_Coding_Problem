'''
Problem:

Two Sum

Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

'''
Reflection:

READ THE PROBLEM (two sum)

len(array) - 1 = array last index

'''

def main(given, k):
    sort_given = sorted(given)
    small = 0
    big = len(given) - 1       # length - 1
    while small <= big:
        if given[small] + given[big] > k:
            big -= 1
        elif given[small] + given[big] < k:
            small += 1
        else:
            return True
    return False

def one_pass(given, k):
    hash_table = set()
    for num in given:
        if k - num in hash_table:
            return True
        else:
            hash_table.add(num)
    return False

if __name__ == '__main__':
    given = [10, 15, 3, 7]
    k = 17
    print(one_pass(given, k))