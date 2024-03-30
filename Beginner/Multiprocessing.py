import time
import multiprocessing

def cal_square(nums):
    for num in nums:
        time.sleep(5)
        print('Square: ', num*num)

def cal_cube(nums):
    for num in nums:
        time.sleep(5)
        print('Cube: ', num * num * num)

if __name__ == '__main__':
    arr = [2, 3, 4, 9, 10]

    t = time.time()

    t1 = multiprocessing.Process(target=cal_square, args=(arr,))
    t2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done in", time.time() - t, "seconds")
