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

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
    print("\t", "DOB: ", end="") 
    print(InfoDb[n]["DOB"]) 
    print("\t", "EMAIL: ", end="") 
    print(InfoDb[n]["Email"]) 
# using comma puts space between values
    print("\t", "FAV BOOKS: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite Books"]))  # join allows printing a string list with separator
    print()

def for_loop():
  for n in range(len(InfoDb)):
    print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop0(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop0(n):
  if n < len(InfoDb):
      print_data(n)
      recursive_loop0(n + 1)
  return # exit condition

def while_loop():
  while_loop0(0)

def recursive_loop():
  recursive_loop0(0)
  
if __name__ == "__main__":
    for_loop()
    #while_loop()
    #recursive_loop()