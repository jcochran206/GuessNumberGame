#############################
# Title: Collatz Sequence v2
# created by Jonathan Cochran
# date 22 July 2019
#############################
print('Hello this is version 2 of collatz. What is your name?')
name = str(input())
print('Alright ' + name + ' lets get started by giving me a number')

number = int(input('enter int:'))
def collatz2(number):
    while number != 1:
        if number % 2 == 0:
            number = number/2
            print(number)
        else:
            number = (number * 3) +1
            print(number)

collatz2(number)
