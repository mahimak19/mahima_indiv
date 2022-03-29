# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Mahima",
    "LastName": "Krovvidy",
    "DOB": "November 19",
    "Email": "mahikro@gmail.com",
    "Favorite Books":["Harry Potter and the Chamber of Secrets","One of Us Is Lying","Sherlock Holmes","Everything,Everything", "Inferno"]
})
InfoDb.append({
    "FirstName": "Dora",
    "LastName": "The Explorer",
    "DOB": "September 40th",
    "Email": "delicioso@swiper.com",
    "Favorite Books":["Harry Potter and the Chamber of Secrets","One of Us Is Lying","Sherlock Holmes","Everything,Everything", "Inferno"]
})

#InfoDb.append({
#"FirstName": "Sunny",
# "LastName": "Naidu",
#"DOB": "August 2",
# "Residence": "San Diego",
#"Email": "snaidu@powayusd.com",
#  "Owns_Cars":["A","B","C"]
# })


def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print(InfoDb[n]["DOB"], InfoDb[n]["Email"])  # using comma puts space between values
    print("\t", "Favorite Books: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite Books"]))  # join allows printing a string list with separator
    print()


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)


def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
for_loop()
#print(InfoDb[1]["FirstName"])


def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
while_loop(0)


def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition
recursive_loop(0)


def ll():
  print("For loop")
  for_loop()
  print("While loop")
  while_loop(0)  
  print("Recursive loop")
  recursive_loop(0)  


if __name__ == "__main__":
    ll()