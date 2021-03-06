##############################################################
# date: 2019/01/17
# name: Jan Brekke
# description: Calculates how many days there are left until
# your birthday. How many days you have lived, and what day of
# the week you were born on.
#
##############################################################
# The script will ask question regarding Birthday details.   #
# If you don't know your city of birth, just type unknown.   #
##############################################################

import datetime
from os import system, name

def clear(): 
  
    # Windows terminal
    if name == 'nt': 
        _ = system('cls') 
  
    # Linux terminal
    else: 
        _ = system('clear') 

clear()

print("\n\n")
print("*"*35)
print("How many days have gone by since you were born?\nAnd what day of the week you were born on?")
print("Find out by entering your birthday..\n")
day = input("What day were you born on? Ex: 7 or 26\n")
month = input("\n\nWhat month were you born in? Ex: 3 or 12\n")
year = input("\n\nAnd finally; What year were you born in? Ex: 1989\n")
city = input("\n\nOkay, last one I promise; What city were you born?\n")

now = datetime.date.today()
yeardate = now.strftime("%Y") 
birthday = datetime.date(int(yeardate),int(month),int(day))
born = datetime.date(int(year),int(month),int(day))
dayname = born.strftime("%A") 
daysago = now - born
left = birthday - now
nextyr = datetime.timedelta(days=365)

clear()
if daysago.days < 0:
    print("Oh C'mon! You haven't enven been born yet!\nNice try..")
    

elif left.days < 0:
    negativeyr = left + nextyr
    print("*"*35)
    print("\nYour birthday isn't until next year, but there are", negativeyr.days,"days left until your birthday!!\n")
    print("You were born on",born,"in the city of",city+".")
    print("This day",daysago.days,"days ago (HOLY sh%t you're old), was a",dayname+".\n")
    print("*"*35)
    print("\n\n")

else:
    print("*"*35)
    print("\nThere are", left.days,"days left until your birthday!!\n")
    print("You were born on",born,"in the city of",city+".")
    print("This day",daysago.days,"days ago (HOLY sh%t you're old), was a",dayname+".\n")
    print("*"*35)
    print("\n\n")
