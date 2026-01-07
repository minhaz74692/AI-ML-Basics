import threading
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

t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr, ))
if __name__=="__main__":
    # cal_square(arr)
    # cal_cube(arr)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Calculation done after: ", time.time()- t, "seconds")