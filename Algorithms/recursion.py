import time
import sys
from math import factorial

sys.setrecursionlimit(10000000)

def iterative_factorial(n):
    fact = 1

    for i in range(2, n + 1):
        fact *= i
    
    return fact

#LIFO: Last in, first out

def recursive_factorial(n):
    # slower
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n - 1)

def recursive_permutation(string, pocket=''):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[:i]
            back = string[i + 1:]
            together = front + back
            recursive_permutation(together, letter + pocket)

def iterative_permutation(items_list):
    for p in range(factorial(len(items_list))):
        print(''.join(items_list))
        i = len(items_list) - 1
        
        while i > 0 and items_list[i - 1] > items_list[i]:
            i -= 1
        
        items_list[i:] = reversed(items_list[i:])

        if i > 0:
            q = i

            while items_list[i - 1] > items_list[q]:
                q += 1

            temp = items_list[i - 1]
            items_list[i - 1] = items_list[q]
            items_list[q] = temp

if __name__ == '__main__':

    start = time.time()
    iter_fact = iterative_factorial(100000)
    end = time.time()
    iter_fact_time = end - start

    start = time.time()
    recur_fact = recursive_factorial(100000)
    end = time.time()
    recur_fact_time = end - start

    start = time.time()
    recur_perm = recursive_permutation('abcde')
    end = time.time()
    recur_perm_time = end - start

    start = time.time()
    iter_perm = iterative_permutation(list('abcde'))
    end = time.time()
    iter_perm_time = end - start

    print(iter_fact_time, end = '\n\n')
    print(recur_fact_time, end = '\n\n')
    print(iter_fact == recur_fact, end = '\n' + '-' * 42 + '\n')

    print(iter_perm_time, end = '\n\n')
    print(recur_perm_time, end = '\n\n')