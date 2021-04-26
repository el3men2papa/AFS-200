

# function to check whether 'n'
# is a multiple of 4 or not
def isAMultipleOf4(n):
  
    # if true, then 'n' is
    # a multiple of 4
    if ((n & 3) == 0):
        return "yes it Is multiple by 4"
  
    # else 'n' is not a
    # multiple of 4
    return "no Is not multiple by 4"
  
# Driver Code
if __name__ == "__main__":
  
    n = int(input("What is your number?:"))
    print (isAMultipleOf4(n))
  
