import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took " + str((end - start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result


array = range(1, 100000)
out_square = calc_square(array)