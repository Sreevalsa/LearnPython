def odd_or_even(number):
    if number % 2 == 0 :
        print "{!s} is even".format(number)
        if number % 4 == 0:
            print "{!s} is a multiple of 4".format(number)
    else:
        print "%d is odd"%number

def check_divisible(number , divisor):
    if number % divisor == 0:
        print "{0} is devisible by {1}".format(number, divisor)
    else:
        print "{0} is not devisible by {1}".format(number, divisor)

number = input("Enter a number: ")
odd_or_even(number)
divisor = input("Enter a number for checking divisible or not: ")
check_divisible(number, divisor)