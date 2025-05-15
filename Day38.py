import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    print(n*5)

print(fx(20))
print('Done for 20')
print(fx(2))
print('Done for 2')
print(fx(20))
print('Done for 20')
