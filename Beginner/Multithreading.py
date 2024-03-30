import time
import threading

def cal_square(nums):
    for num in nums:
        time.sleep(0.2)
        print('Square: ', num*num)


def cal_cube(nums):
    for num in nums:
        time.sleep(0.2)
        print('Cube: ', num * num * num)


arr = [2,3 ,4 ,9, 10]

t = time.time()

t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ", time.time() - t)
