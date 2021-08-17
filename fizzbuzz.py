# For each number n from 1 to 1000:
# If n is divisible by 3, print "Fizz"
# If n is divisible by 5, print "Buzz"
# If n is divisible by both 3 and 5, print "FizzBuzz"
# If n is not divisible by either 3 or 5, print n 

def fizzbuzz():
    for i in range(1, 1001):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        print(output or i)

fizzbuzz()