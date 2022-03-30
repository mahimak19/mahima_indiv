def swap (x,y):
    q = x
# we set one of our variables to a temporary variable
    x = y
#swap the original two variables
    y = q
#set y equal to the temp
    return x,y


def swaptester():
  x = input ("Type a number ")
  y = input ("Type another number ")
  print (x,y)
  a,b= swap(x,y)
  print(a, b)

if __name__ == "__main__":
    swaptester()