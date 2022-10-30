import datetime
def age(): 

    birth_year = int(input("please type your birth year "))
    today = datetime.date.today()
    year = int(today.year)
    your_age = year - birth_year
    print( "your age is " + str(your_age))
def best_stocks():
    print ("the best stocks can be found on : investors.com")

name = input("what is your name? ")
print ("hello " + name)
answer = input("do you want to know your age? ")
if(answer == "yes"):
    age()
else:
    best_stocks()