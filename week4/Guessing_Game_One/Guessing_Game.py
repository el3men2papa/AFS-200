import random


#This is the function for creating a Random Number
def generateNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

#This is the function to ask the user to guess the number
def askUserForNumber(message = "Guess the number: "):
    userNumber = int(input(message))
    return userNumber

#This function will check or compare the random Number and the user Number to see if match
def checkUserNumber( userNumber, randomNumber):
    if userNumber > randomNumber:
        return "Your Number Is Too high"

    elif userNumber < randomNumber:
        return "Your Number Is Too Low"

    else:
        return "Congratulations!"

#The main is require to call the functions
def main():
    userCongratulation = False
    letsStart = True

    while userCongratulation or letsStart:
#this will storage the count of input when is a new game it will start with 0
        userNumberOfGuesses = 0
        randomNumber = generateNumber()
        #print("Random Number tesing: " , randomNumber)
        userNumber = askUserForNumber()
#this will count the input evry time they get it wrong
        userNumberOfGuesses = userNumberOfGuesses + 1
        message = checkUserNumber(userNumber, randomNumber)
        

        while message != "Congratulations!":
            print(message)
            userNumber = askUserForNumber("Try again: ")
#This will count the final input when they win
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber(userNumber, randomNumber)

#This print out the message with the count of inputs
        print(message, "It took you", userNumberOfGuesses, "guesses to get the right number")
        userCongratulation = True
#This will ask the user to see if they would like to continue the game or exit
        answer = input("Do you want to continue? Y or N :" )
        if answer.lower().startswith("y"):
            print("ok, carry on then")
        elif answer.lower().startswith("n"):
            print("ok, Thank you for playing")
            exit()

main()
        
