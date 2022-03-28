# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input



def recursion_fib(x):
  if x <= 1:
    return 1
  else:
    return(recursion_fib(x-1) + recursion_fib(x-2))


def fib():
  y = int(input("How many Fibonacci? "))

  for i in range(y):
    fib = recursion_fib(i)
    print(fib)
  
if __name__ == "__main__":
  fib()

    