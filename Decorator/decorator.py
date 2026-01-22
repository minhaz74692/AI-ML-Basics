import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + " mil sec")
        return result

    return wrapper


@time_it
def cal_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result



@time_it
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

if __name__ == "__main__":
    array = range(0,100000)
    cal_square(array)
    cal_cube(array)
