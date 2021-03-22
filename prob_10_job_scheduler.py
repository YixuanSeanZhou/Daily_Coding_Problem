'''
Prob 10 Medium

Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.

'''

import time


def scheduler(f, n):
    time.sleep(n / 1000)
    f()

def test_func():
    print(1)

if __name__ == '__main__':
    scheduler(test_func, 1)