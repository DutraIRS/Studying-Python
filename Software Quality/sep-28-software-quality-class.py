import sys

sys.path.insert(0, './src')
sys.path.insert(0, './test')

import module_quality as mq
import test_module_quality as tmq

try:
    print(mq.simplest_func(1, 'Hello, world!'))
except AssertionError as error:
    print('Invalid arguments!', error)

print(mq.simplest_func(1, -1))

print(mq.simplest_func(1, 1.0))

print(mq.simplest_func(-1.0, 1.0))

help(tmq)
help(mq)

print(mq.terrible_func('', 42))