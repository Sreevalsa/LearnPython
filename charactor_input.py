import datetime

def charactor_input(name, age):
    year_gap = 100 - int(age)
    year100 = int(datetime.datetime.now().year) + year_gap
    print year100
    # message = "Hi %s you will turn 100 in %s"%(name, str(year100))
    # return message
    message = "Hi {0} you will turn 100 in {1}".format(name, str(year100))
    # message = "You will turn 100 in {!s} and {}".format(year100,name)
    # message = "You will turn 100 in {!s}".format(year100)
    return message

def count_leap_years(year):
    current_year = datetime.datetime.now().year
    count = 0
    for i in range(current_year - year):
        temp_year = year + i
        if 0 == temp_year % 4:
            count += 1
    return count

def print_message(message, repeatation):
    # i = 0
    # for i in range(repeatation):
    #     print message
    print (message + "\n") *repeatation

if __name__== "__main__":
    name = raw_input("enter your name: ")
    dob = raw_input("Enter your date of birth in the format yyyy-mm-dd: ")
    dob_list = dob.split("-")
    year = int(dob_list[0])
    month = dob_list[1]
    day = dob_list[2]
    dob_in_datetime = datetime.datetime(year, int(month), int(day))
    age_in_days_with_time = datetime.datetime.now() - dob_in_datetime
    count = count_leap_years(year)
    age_in_days = age_in_days_with_time.days - count
    age = age_in_days/365
    message = charactor_input(name, age)
    print message
    rept = input("enter the number of times to print the message: ")
    print_message(message, rept)