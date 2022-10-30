import datetime
def age(): 

    birth_year = int(input("please type your birth year "))
    today = datetime.date.today()
    year = int(today.year)
    your_age = year - birth_year
    print( "your age is " + str(your_age))
def best_stocks():
    return ("the best stocks can be found on : investors.com")


def best_books():
    return("U can find best books of the year at : https://time.com/6178674/best-books-2022-so-far/")
name = input("what is your name? ")
print ("hello " + name)
answer = input("do you want to know your age? ")
if(answer == "yes"):
    age()
elif(answer == "no"):
    print ("than look at that:" + best_stocks() + best_books())
