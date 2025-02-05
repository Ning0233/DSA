import timeit, random, sys
import numpy as np

def sum_arr(arr):
    total = 0
    for i in arr:
        total += i
    return total

def sum_matrix(A, B):
    matrixA = np.array(A)
    matrixB = np.array(B)
    return matrixA + matrixB

def get_user_input(max_attempt = 5):
    attempt = 0
    while True:
        try:
            user_input = input("Please enter a non_zero integer: ")
            n = int(user_input)
            if n != 0 and n <= 1000000:
                print(f"your input is {n}. ")
                return n
            else: print("please put a non-zero integer")
        except ValueError:
            print("please put a non-zero integer")
        attempt += 1
            
# generate array or matrix 
def generate_arr(n):
    arr = [random.randint(0,100) for _ in range(n)]
    # print(arr)
    return arr

def generate_matrix(n):
    matrix = np.random.randint(0, 10, size=(n,n))
    # print(matrix)
    return matrix

def measure_memory(func, *args):
    array_mem = sys.getsizeof(args)
    result = func(*args)
    sum_mem = sys.getsizeof(result)

    return array_mem, sum_mem

if __name__ == "__main__":
    with open("lab_1_log.txt", "a") as file:
        file.write("Lab1 Output\n")
        file.write("================\n")
        while True:
            user_input= input(f"choose the program: A for Array, M for Matrix. Q for quit.\n")
            program = user_input.lower()
            if program == "a": 
                number = get_user_input()
                random_arr = generate_arr(number)
                execution_time = timeit.timeit('sum_arr(random_arr)', globals=globals(),number=100)
                file.write(f"Exceution time for 100 runs for array size {number}: {execution_time}s \n")
                before_mem, result_mem = measure_memory(sum_arr, random_arr)
                file.write(f"Memory used for array: {before_mem} bytes\n")
                file.write(f"Memory used for result: {result_mem} bytes\n")
                #print(f"Exceution time for 100 runs for array size {number}: {execution_time} s")
                
            elif program == "m": 
                number = get_user_input()
                random_matrix_A = generate_matrix(number)
                random_matrix_B = generate_matrix(number)
                execution_time = timeit.timeit('sum_matrix(random_matrix_A, random_matrix_B)', globals=globals(),number=100)
                file.write(f"Exceution time for 100 runs for matrix size {number}: {execution_time}s \n")
                before_mem, result_mem = measure_memory(sum_matrix, random_matrix_A, random_matrix_B)
                file.write(f"Memory used for array: {before_mem} \n")
                file.write(f"Memory used for result: {result_mem}\n")
                #print(f"Exceution time for 100 runs for matrix size {number}: {execution_time} s")
            elif program == "q":
                break
            else:
                print("invalid input. please try again")

