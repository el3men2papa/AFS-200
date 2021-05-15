
#Function for maximus number 
def maximum(a, b, c): 
#will create a list for the numbers
    list = [a, b, c] 

#will choose the max number
    return max(list) 

#will ask the user for the numbers input
x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
z = int(input("Enter Third number: "))

#will print out the max number 
print("Maximum Number is ",maximum(x, y, z)) 