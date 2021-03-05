'''
#4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def swap_implementation(nums):
    if not nums:
        return 1
    for i in range(len(nums)):
        # 0 -> 1
        # Check the nums[i] is at the right place or not and check if it is viable
        while i+1 != nums[i] and 0 < nums[i] <= len(nums):
            num = nums[i]
            nums[i], nums[num - 1] = nums[num - 1], nums[i]
            if nums[i] == num:
                break
    for i, num in enumerate(nums, 1):
        if i != num:
            return i
    return len(nums) + 1
    
def counting_with_append(nums):
    '''
    O(n) speed, O(1) space solution:
    
    Idea: 
    1. Remove everything not within the range [1, length+1]
    2. Count the frequencey of each number between [1, length+1]
    3. Returen the one that has 0 occupancy, or return length+1
    '''
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]//n==0:
            return i
    return n
    
def pure_counting(nums):
    length = len(nums)
    for i in range(length):
        if nums[i] % (length + 1) == 0:
            continue
        if nums[i] % (length + 1) == length:
            nums[0] += length + 1
        else:
            nums[nums[i] % (length + 1)] += (length + 1)
    
    # Start counting from 1
    for i in range(1, length):
        if nums[i] // (length + 1) == 0:
            return i
    
    if nums[0] // (length + 1) == 0:
        return length

    return length + 1

if __name__ == '__main__':
    nums = [2, 3, 0]
    print(counting_with_append(nums))