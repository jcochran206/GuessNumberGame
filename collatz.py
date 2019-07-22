#############################
# Title: Collatz Sequence v1
# created by Jonathan Cochran
# date 22 July 2019
#############################
print('hello we are going to create the collatz sequence.  What is your name?')
name = input()
print('Okay '+ name + ' give me an integar')

#### function
number = int(input())
def collatz(number):
    if number % 2 == 0:
        print(number)
    else:
        print(3 * number + 1)
    
collatz(number)
