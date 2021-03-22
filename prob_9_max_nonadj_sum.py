'''
# 9 Hard

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

'''


'''
This is 2n, but this is wrong
'''
def max_non_adj_sum(num_list):
    
    # Sep by 1
    ones = [0, 0]
    for i, num in enumerate(num_list):
        ones[i%2] += num
    
    # Sep by 2
    twos = [0, 0, 0]
    for i, num in enumerate(num_list):
        twos[i%3] += num
    
    one_max = max(ones)
    two_max = max(twos)
    ret = max(one_max, two_max)
    return ret

'''
This is n, tho both O(n), but this is better, but this is also wrong.
'''
def max_non_adj_sum_faster(num_list):
    
    twos = [0, 0, 0]
    ones = [0, 0]
    for i, num in enumerate(num_list):
        ones[i%2] += num
        twos[i%3] += num
    
    one_max = max(ones)
    two_max = max(twos)
    ret = max(one_max, two_max)
    return ret



'''
After reading prob + solution
'''
def max_non_adj_sum_correct(num_list):
    # There are two cases, whether the prevous iteration used the last one, or not.
    # For example:
    # Whne the array is [1, 2]. Then we return 2 because we should return the one that consider the last one.
    # When the array is [2, 3, 5, 6], we should return 2+5 t not consider the last one.

    if not num_list:
        return 0

    if len(num_list) < 2:
        return max(0, max(num_list))
    
    no_last = max(0, num_list[0])
    with_last = max(no_last, num_list[1])

    for num in num_list[2:]:
        tmp = with_last

        with_last = max(with_last, no_last + num)
        no_last = tmp
    
    return max(with_last, no_last)


if __name__ == '__main__':
    assert max_non_adj_sum([2, 4, 6, 2, 5]) == 13
    assert max_non_adj_sum([5, 1, 1, 5]) == 10
    assert max_non_adj_sum([5, 1, 2, 1, 5]) == 12
    assert max_non_adj_sum([]) == 0
    assert max_non_adj_sum([1]) == 1
    assert max_non_adj_sum([1,2]) == 2

    assert max_non_adj_sum_faster([2, 4, 6, 2, 5]) == 13
    assert max_non_adj_sum_faster([5, 1, 1, 5]) == 10
    assert max_non_adj_sum_faster([5, 1, 2, 1, 5]) == 12
    assert max_non_adj_sum_faster([]) == 0
    assert max_non_adj_sum_faster([1]) == 1
    assert max_non_adj_sum_faster([1,2]) == 2

    assert max_non_adj_sum_correct([2, 4, 6, 2, 5]) == 13
    assert max_non_adj_sum_correct([5, 1, 1, 5]) == 10
    assert max_non_adj_sum_correct([5, 1, 2, 1, 5]) == 12
    assert max_non_adj_sum_correct([]) == 0
    assert max_non_adj_sum_correct([1]) == 1
    assert max_non_adj_sum_correct([1,2]) == 2
