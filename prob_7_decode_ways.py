'''
Problem #7 [Medium]

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, 
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

'''


'''
Initial Idea:

Recursive dp

O(n) time
O(n) space
'''
def num_decodings(s: str) -> int:
        
    seq_map = dict()
    
    seq_map['0'] = 0
    return counting(s, seq_map)
        

def counting(s: str, seq_map):
    if len(s) > 0 and s[0] == '0':
        return 0
    
    if s in seq_map:
        return seq_map[s]

    if len(s) <= 1:
        seq_map[s] = 1
        return 1
    
    if int(s[:2]) <= 26:
        two_off_way = counting(s[2:], seq_map)
    else:
        two_off_way = 0
    
    one_off_way = counting(s[1:], seq_map)
    
    ret = two_off_way + one_off_way
    seq_map[s] = ret

    return ret

'''
Recursive method 

That might be great... but I just don't really know I can come up with.

O(n) time
O(1) space
'''
def better_dp_sol(s: str) -> int:
    prev_prev = prev = result = int(s[0] != '0')
    for i in range(1, len(s)):
        last_two = int(s[i-1:i+1])
        if not last_two or (last_two >= 30 and not last_two % 10): 
            # If the string is 30, then we can not decode it
            return 0
        
        if (last_two not in [10, 20]):
            # If we add a 10 or 20, there is only one way which is treat them as a whole
            result += prev
        
        if 10 <= last_two <= 26:
            # This means we can count the last_two as one letter
            result += prev_prev
        
        # Clearner way:
        # result = (last_two not in [10, 20])*prev + (10 <= last_two <= 26)*prev_prev


        prev_prev, prev = prev, result



if __name__ == '__main__':
    print(num_decodings('1234'))
    print()

