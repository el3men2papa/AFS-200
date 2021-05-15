
#Will ask the user for the string 
string= input("Enter string thst contains Capital and Lower case:")
#Variables to start the count on 0
count1=0
count2=0

#function to start counting the strings
for i in string:
#it will count the lower case
    if(i.islower()):
            count1=count1+1
#This is going to count the UPPER Case
    elif(i.isupper()):
        count2=count2+1

#ill print out the results
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)