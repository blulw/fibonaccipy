import time
import sys

sys.set_int_max_str_digits(0)

filename = "time.txt"

def fibonacci(num1, num2, iterations):
    
    print(num1)
    print(num2)
    for i in range(iterations):
        result = num1+num2
        print(result)
        num1 = num2
        num2 = result




def fibonacciArray(num1, num2, iterations):
    
    print(num1)
    print(num2)
    
    
    n = 2
    fibnums = [num1, num2]
    
    
    for i in range(iterations):
        fibnums.append(fibnums[n-1]+fibnums[n-2])
        print(fibnums[n])
        n+=1
        


start_time = time.time()
fibonacci(0, 1, 100)
normal_time= ("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
fibonacciArray(0, 1, 100)
array_time = ("--- %s seconds ---" % (time.time() - start_time))

hundred = f"No Arrays: {normal_time}\nUsing Arrays: {array_time}"

start_time = time.time()
fibonacci(0, 1, 1000)
normal_time= ("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
fibonacciArray(0, 1, 1000)
array_time = ("--- %s seconds ---" % (time.time() - start_time))

thousand = f"No Arrays: {normal_time}\nUsing Arrays: {array_time}"

start_time = time.time()
fibonacci(0, 1, 10000)
normal_time= ("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
fibonacciArray(0, 1, 10000)
array_time = ("--- %s seconds ---" % (time.time() - start_time))

tenthousand = f"No Arrays: {normal_time}\nUsing Arrays: {array_time}"


# !!100k takes 5+ minutes, uncomment it if you want a full test!!

# start_time = time.time()
# fibonacci(0, 1, 100000)
# normal_time= ("--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# fibonacciArray(0, 1, 100000)
# array_time = ("--- %s seconds ---" % (time.time() - start_time))

# hundredthousand = f"No Arrays: {normal_time}\nUsing Arrays: {array_time}"


with open(filename, "w") as f:
    f.write(f"100 iterations:\n{hundred}\n1000 iterations:\n{thousand}\n10000 iterations:\n{tenthousand}\n")
    
# with open(filename, "w") as f:
#     f.write(f"100 iterations:\n{hundred}\n1000 iterations:\n{thousand}\n10000 iterations:\n{tenthousand}\n100000 iterations:\n{hundredthousand}")
