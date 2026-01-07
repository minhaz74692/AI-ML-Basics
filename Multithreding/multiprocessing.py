from multiprocessing import Process
import time

def cal_square(numbers):
    print("start calculating squares:")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ", n*n ,"\n")

def cal_cube(numbers):
    print("start calculating cubes:")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ", n*n*n, "\n")

arr = [2,3,4,5]
t=time.time()

if __name__=="__main__":
    p1 = Process(target=cal_square, args=(arr,))
    p2 = Process(target=cal_cube, args=(arr,))
    print("Calculation done after: ", time.time()- t, "seconds")
