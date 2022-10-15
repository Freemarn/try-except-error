# writing a try/ exception code, to output a desired string on error
from unicodedata import name


try:

   x =  int(input("Enter an integer :"))
   print(x)

except:
    print("Invalid input, enter a number ")

#Targeting specific errors

name
try:
    y =  int(input("Enter an integer : "))
    print(y)

except ValueError:
    print("wrong value " )

#wether or not there is an error, this is going to run
finally:
    print("finished")
