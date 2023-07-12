import time

a = 1_000_000_000
b = 1_000_000_000

while True:
    print("A: ", round(a), "\tB: ", round(b), "\tRatio: ", round(a/b, 4))
    
    a_delta = 0.3*a
    b_delta = 0.2*b

    a = a - a_delta + b_delta
    b = b - b_delta + a_delta

    time.sleep(1)
