
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

def driver():
  num = int(input("Type a number "))
  print_factors(num)

if __name__ == "__main__":
    driver()