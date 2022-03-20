# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

y = int(input("How many Fibonacci? "))


def recursion_fib(x):
  if x <= 1:
    return 1
  else:
    return(recursion_fib(x-1) + recursion_fib(x-2))


for i in range(y):
  fib = recursion_fib(i)
  print(fib)


    