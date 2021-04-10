name = input("What is your name?:")
print("Your name is " + name)

age = input("What is your age?:")
yearGoal = 100
import datetime
now = datetime.datetime.now()
currentYear = (now.year)
sub=float(yearGoal)-float(age)+float(currentYear)
print("If you are {1} by {2} you will be {0} years old ". format(yearGoal,age,sub) )
