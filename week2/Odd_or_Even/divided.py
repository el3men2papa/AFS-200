num = int(input("imput your first number:"))
check = int(input("input your second number:"))

n = ('Division (floor) : ', num // check)

# function to check whether 'n'
# is a multiple of 4 or not
def isAMultipleOf4(n):
  
    # if true, then 'n' is
    # a multiple of 4
    if ((n & 3) == 0):
        return "Yes"
  
    # else 'n' is not a
    # multiple of 4
    return "No"
  
# Driver Code
if __name__ == "__main__":
  
    #n = int(input("What is your number?:"))
    print (isAMultipleOf4(n))
  
