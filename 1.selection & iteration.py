def factorial(number):
    if number==0:
        return 1
    else:
        return number * factorial(number-1)
def palindrome(number):
    num2 = str(number)
    rev_num = num2[::-1]
    rev_num= int(rev_num)
    if number == rev_num:
        print("The given number is a palindrome")
    else:
        print("The given number is not a palidrome")
def count_digits(number):
     return len(str(number))
number = int(input("Enter a number :"))
if number%2 ==0:
    print("the number is even")
    palindrome(number)
else:
    print("The number is odd")
    fact = factorial(number)
    print("the factorial is :",fact)
    no_digits = count_digits(fact)
    print("The no of digits in the factorial is :",no_digits)